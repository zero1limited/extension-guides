import os, glob, re, json
from atlassian import Confluence
from markdown import markdown
import yaml

BASE_URL = os.environ["CONFLUENCE_BASE_URL"].rstrip("/")
USER = os.environ["CONFLUENCE_USER_EMAIL"]
TOKEN = os.environ["CONFLUENCE_API_TOKEN"]
SPACE = os.environ["CONFLUENCE_SPACE_KEY"]
PARENT_ID = os.environ.get("CONFLUENCE_PARENT_ID", "").strip() or None
MD_GLOB = os.environ.get("MD_GLOB", "docs/**/*.md")

# --- Helpers ---------------------------------------------------------------

def split_frontmatter(md_text):
    """
    Returns (frontmatter_dict, body_md).
    Supports optional YAML frontmatter delimited by --- lines.
    """
    if md_text.startswith("---"):
        parts = md_text.split("\n", 2)
        if len(parts) > 2:
            # find closing '---'
            m = re.search(r"\n---\s*\n", md_text[4:], re.M)
            if m:
                end = 4 + m.start()
                front = md_text[4:end]
                body = md_text[end+5:]  # skip closing '---\n'
                data = yaml.safe_load(front) or {}
                return (data, body)
    return ({}, md_text)

def md_to_storage_html(md_text):
    """
    Convert GitHub-flavored Markdown to HTML suitable for Confluence 'storage' format.
    For most content, standard HTML is accepted by Confluence's storage representation.
    """
    # Extensions can be expanded if you need tables/TOC/etc.
    return markdown(md_text, extensions=['tables', 'fenced_code'])

def find_page_by_title(conf, space, title):
    results = conf.get_page_child_by_title(space=space, title=title)
    return results  # None if not found

def create_or_update(conf, title, html_body, labels=None, ancestor_id=None, page_id=None):
    labels = labels or []
    if page_id:
        # Update by explicit page_id
        page = conf.get_page_by_id(page_id, expand='version,body.storage')
        if not page:
            raise RuntimeError(f"Page id {page_id} not found.")
        conf.update_page(
            page_id=page_id,
            title=title,
            body=html_body,
            representation='storage',
            parent_id=ancestor_id or page.get('ancestors', [{}])[-1].get('id'),
            minor_edit=True
        )
        if labels:
            conf.set_page_labels(page_id, labels)
        print(f"Updated page: {title} (id={page_id})")
        return page_id
    else:
        # Try to find by title in space first so repeated runs are idempotent
        page = find_page_by_title(conf, SPACE, title)
        if page:
            page_id = page["id"]
            conf.update_page(
                page_id=page_id,
                title=title,
                body=html_body,
                representation='storage',
                parent_id=ancestor_id or page.get('ancestors', [{}])[-1].get('id'),
                minor_edit=True
            )
            if labels:
                conf.set_page_labels(page_id, labels)
            print(f"Updated page: {title} (id={page_id})")
            return page_id
        else:
            page_id = conf.create_page(
                space=SPACE,
                title=title,
                body=html_body,
                parent_id=ancestor_id,
                type='page',
                representation='storage'
            )["id"]
            if labels:
                conf.set_page_labels(page_id, labels)
            print(f"Created page: {title} (id={page_id})")
            return page_id

# --- Main ------------------------------------------------------------------

def main():
    conf = Confluence(
        url=BASE_URL,
        username=USER,
        password=TOKEN,
        cloud=True,
    )

    files = glob.glob(MD_GLOB, recursive=True)
    if not files:
        print("No Markdown files matched; nothing to publish.")
        return

    for path in files:
        with open(path, "r", encoding="utf-8") as f:
            raw = f.read()

        fm, body_md = split_frontmatter(raw)
        title = fm.get("title") or os.path.splitext(os.path.basename(path))[0].replace("-", " ").title()
        labels = fm.get("labels") or []
        page_id = fm.get("confluence_page_id")  # optional explicit id for guaranteed updates
        ancestor_id = fm.get("parent_id") or PARENT_ID

        html = md_to_storage_html(body_md)

        # (Optional) simple cleanup: convert <pre><code class="language-xxx"> to {code:xxx}
        # If you prefer Confluence macros for code blocks, uncomment below.
        # html = re.sub(
        #     r'<pre><code class="language-([^"]*)">(.*?)</code></pre>',
        #     r'<ac:structured-macro ac:name="code"><ac:parameter ac:name="language">\1</ac:parameter><ac:plain-text-body><![CDATA[\2]]></ac:plain-text-body></ac:structured-macro>',
        #     html,
        #     flags=re.S
        # )

        create_or_update(
            conf,
            title=title,
            html_body=html,
            labels=labels,
            ancestor_id=ancestor_id,
            page_id=page_id
        )

if __name__ == "__main__":
    main()
