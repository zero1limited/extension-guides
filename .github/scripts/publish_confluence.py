import os, glob, re
from atlassian import Confluence
from markdown import markdown
import yaml

BASE_URL = os.environ["CONFLUENCE_BASE_URL"].rstrip("/")
USER = os.environ["CONFLUENCE_USER_EMAIL"]
TOKEN = os.environ["CONFLUENCE_API_TOKEN"]
SPACE = os.environ["CONFLUENCE_SPACE_KEY"]
PARENT_ID = os.environ.get("CONFLUENCE_PARENT_ID", "").strip() or None
MD_GLOB = os.environ.get("MD_GLOB", "docs/**/*.md")

# --- helpers ---------------------------------------------------------------

def split_frontmatter(md_text):
    """Returns (frontmatter_dict, body_md) for optional YAML frontmatter."""
    if md_text.startswith("---"):
        # find closing '---' after the first line
        m = re.search(r"^---\s*$", md_text.split("\n", 1)[1], re.M)
    # simpler robust approach:
    lines = md_text.splitlines(True)
    if lines and lines[0].strip() == "---":
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                front = "".join(lines[1:i])
                body = "".join(lines[i+1:])
                data = yaml.safe_load(front) or {}
                return (data, body)
    return ({}, md_text)

def md_to_storage_html(md_text):
    """Convert Markdown to HTML for Confluence storage representation."""
    return markdown(md_text, extensions=['tables', 'fenced_code'])

def find_page_by_title(conf, space, title):
    """Return a page dict if found, else None. Tries helper then CQL."""
    # Try library helper
    try:
        page = conf.get_page_by_title(space=space, title=title)
        if page and page.get("id"):
            return page
    except AttributeError:
        pass

    # Fallback to CQL (exact title match)
    cql = f'type=page and space="{space}" and title="{title}"'
    res = conf.cql(cql, limit=1, expand="content.version,content.body.storage,content.ancestors")
    results = (res or {}).get("results", [])
    if results:
        content = results[0].get("content", {})
        return {
            "id": content.get("id"),
            "title": content.get("title"),
            "version": content.get("version"),
            "body": content.get("body"),
            "ancestors": content.get("ancestors", []),
        }
    return None

def preflight(conf, space_key, parent_id=None):
    """Early, explicit checks so permission errors are clearer."""
    space = conf.get_space(space_key)
    if not space or not space.get('key'):
        raise RuntimeError(
            f"Confluence preflight: cannot access space '{space_key}'. "
            "Check that the API user has a Confluence license and space permissions."
        )
    if parent_id:
        page = conf.get_page_by_id(parent_id, expand='id,title,ancestors,space')
        if not page or not page.get('id'):
            raise RuntimeError(
                f"Confluence preflight: parent page id '{parent_id}' not found or not visible to this user."
            )

def create_or_update(conf, title, html_body, ancestor_id=None, page_id=None):
    """Create or update a page without labels."""
    if page_id:
        page = conf.get_page_by_id(page_id, expand='version,body.storage,ancestors')
        if not page:
            raise RuntimeError(f"Page id {page_id} not found.")
        parent_for_update = ancestor_id or (page.get("ancestors")[-1]["id"] if page.get("ancestors") else None)
        conf.update_page(
            page_id=page_id,
            title=title,
            body=html_body,
            representation='storage',
            parent_id=parent_for_update,  # leave None if you don't want to move it
            minor_edit=True
        )
        print(f"Updated page: {title} (id={page_id})")
        return page_id
    else:
        page = find_page_by_title(conf, SPACE, title)
        if page:
            page_id = page["id"]
            parent_for_update = ancestor_id or (page.get("ancestors")[-1]["id"] if page.get("ancestors") else None)
            conf.update_page(
                page_id=page_id,
                title=title,
                body=html_body,
                representation='storage',
                parent_id=parent_for_update,
                minor_edit=True
            )
            print(f"Updated page: {title} (id={page_id})")
            return page_id
        else:
            created = conf.create_page(
                space=SPACE,
                title=title,
                body=html_body,
                parent_id=ancestor_id,
                type='page',
                representation='storage'
            )
            page_id = created["id"]
            print(f"Created page: {title} (id={page_id})")
            return page_id

# --- main ------------------------------------------------------------------

def main():
    conf = Confluence(url=BASE_URL, username=USER, password=TOKEN, cloud=True)

    # Optional but helpful
    preflight(conf, SPACE, PARENT_ID)

    files = glob.glob(MD_GLOB, recursive=True)
    if not files:
        print("No Markdown files matched; nothing to publish.")
        return

    for path in files:
        with open(path, "r", encoding="utf-8") as f:
            raw = f.read()

        fm, body_md = split_frontmatter(raw)
        title = fm.get("title") or os.path.splitext(os.path.basename(path))[0].replace("-", " ").title()
        page_id = fm.get("confluence_page_id")  # optional to force updating a specific page
        ancestor_id = fm.get("parent_id") or PARENT_ID

        html = md_to_storage_html(body_md)
        create_or_update(conf, title=title, html_body=html, ancestor_id=ancestor_id, page_id=page_id)

if __name__ == "__main__":
    main()
