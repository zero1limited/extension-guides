# Renovate Bot - Overview

1. Go through each client in the [Renovate Configured Projects](#Projects) list
2. Open the Github PRs link and look for a PR titled `Update Bug Fixes`. If there are none, go to next in the list.
3. If the modules listed for upgrade include anything with `hyva` see [cleaning up previous config](#cleaning-up-previous-config], then proceed to the next in the list.
4. If there is a PR create task in teamwork for the client with:
  - title: "Investigate: Minor module updates".
  - Tag the task with "OPS-Renovate"
  - Create the task in Inbox
  - Make the task private (so the client cannot see it)
  Log your time as unbillable, when working on this task.
5. Open the PR, at the top under the title you will see something like "zero1renovatebot wants to merge 1 commit into master from renovate/bug-fixes". Copy the "from" part (in this example: `renovate/bug-fixes`) create an instance in MDOQ with this as the ticket number. The decription doesn't matter.
6. Once the instance is rolled up, click "I'm Done" and let the regression tests run. If the instance is behind master see [Git Merge Process](#git-merge-process)
7. If the regression tests fail for a valid reason i.e something is actually broke go to [Difficult Update](#difficult-update)
  If they pass go to [Simple Update](#simple-update)


### Arrons Temp notes - to update docs when happy

An existing branch name `renovate/bug-fixes` will stop Renovate continuing to do its thing, if a branch has been left for ages, delete the branch




### Simple Update
Make the task visible to the client.
Using the template below send a message to the client.

```text
Hi @productOwner,

We have identified that some modules you have installed have minor updates available.
Minor updates include bug fixes and security improvements, they don't include changes to functionality.
It's recommended to always stay up to date with all minor updates.

The following modules have fixes available
{{ USE THE INFO THE PR TO POPULATE MOULDE UPDATES }}

Our automated testing hasn't identidied any issues.
Please could you review and let us know if you are happy for us to create a deployment and release this work.
{{ INSTANCE URLs }}

_N.B_ this task will consume 1 hour of MC time, excluding unexpected issues.

Many thanks
{{ YOUR NAME}}
```

**If they approve**
- Log one hour of billable time to the task. (Other time actually spent working on the task is still unbillable)
- Click client accepted, and organise a release time with the client.
  For now we will assume these releases will always be downtime. (Expected downtime <10mins)

**If they don't approve**
STOP ASK ADAM TO TAKE A LOOK

### Difficult Update
1. Log a quick summary of the test which failed and possibly action required to mitigate. 
2. Close the task.
3. Delete the instance.
4. Implement the fixes on the failing tests.
5. Once tests are confirmed passing we can open a new task and retry until we can get a instance that passes and can be a simple update.


## Projects

| Client | Github PRs |
|-|-|
| Roys | [PRs](https://github.com/zero1limited/roys.co.uk/pulls) |
| Abakhan | [PRs](https://github.com/zero1limited/magento2-Abakhan/pulls) |
| Barr Display | [PRs](https://github.com/zero1limited/magento2-BarrDisplay/pulls) |

### Not Configured Projects

To install / configure renovate bot see: [Renovate Bot](/docs/main/blogs/rennovate-bot#content-adding-new-reposiorties)
  
| Client | Github PRs |
|-|-|
| Custom Netting | [PRs](https://github.com/zero1limited/REPO/pulls) |
| Toolstoday | [PRs](https://github.com/zero1limited/REPO/pulls) |
| British Hardwood | [PRs](https://github.com/zero1limited/REPO/pulls) |
| iBottles | [PRs](https://github.com/zero1limited/REPO/pulls) |
| Crucial BMX | [PRs](https://github.com/zero1limited/REPO/pulls) |
| CycloMarket | [PRs](https://github.com/zero1limited/REPO/pulls) |
| TweeksCycles | [PRs](https://github.com/zero1limited/REPO/pulls) |
| Divine Trash | [PRs](https://github.com/zero1limited/REPO/pulls) |
| Elms Marketing | [PRs](https://github.com/zero1limited/REPO/pulls) |
| Epic Militaria | [PRs](https://github.com/zero1limited/REPO/pulls) |
| KJ Golf | [PRs](https://github.com/zero1limited/REPO/pulls) |
| Mercy Robes | [PRs](https://github.com/zero1limited/REPO/pulls) |
| Paddocks | [PRs](https://github.com/zero1limited/REPO/pulls) |
| Professional Books | [PRs](https://github.com/zero1limited/REPO/pulls) |
| Fierce PC | [PRs](https://github.com/zero1limited/REPO/pulls) |
| Regatta | [PRs](https://github.com/zero1limited/REPO/pulls) |
| Regatta | [PRs](https://github.com/zero1limited/REPO/pulls) |
| Go Fish | [PRs](https://github.com/zero1limited/REPO/pulls) |
| Rompa | [PRs](https://github.com/zero1limited/REPO/pulls) |
| SDS London | [PRs](https://github.com/zero1limited/REPO/pulls) |
| Thomas And Anchor | [PRs](https://github.com/zero1limited/REPO/pulls) |
| Imagin Fires | [PRs](https://github.com/zero1limited/REPO/pulls) |
| Minky | [PRs](https://github.com/zero1limited/REPO/pulls) |


### Cleaning Up Previous Config

- Close all renovate PRs
- When looking at the PR there should be a button at the bottom of the page "Close pull request" click this.
- Delete all renovate branches
- close all renovate issues

### Git Merge Process
If your branch is behind master carry out these steps to pull in the changes from master so I'm done can be set off.
1. Click the "GitHub" icon in MDOQ
2. Open the dropdown that says "Please select a branch..." and select "master".
3. Click the merge button.
4. If the merge passes move to step 5. If it fails due to conflicts see [Resolving Merge Conflicts](https://docs.mdoq.io/hc/en-gb/articles/9832737324561-Resolving-Merge-Conflicts).
5. Click the "GitHub" icon again.
6. Click the "Git Pull" button.
7. If that passes, you can click "I'm done" and set off that process. If it fails due to files that would be overwritten, go into code editor and delete those files. Then you can git pull again and it should pass.
