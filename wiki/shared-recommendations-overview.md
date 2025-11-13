# Shared Recommendations

Be good to automate an index here of the pages within, perhaps they will show on the left?


### Old list of WIKIs

https://support.zero1.co.uk/hc/en-us/categories/202922967-Internal-EPIC-WIKIs




## Index
- [Please refer to the Master Spreadsheet](https://docs.google.com/spreadsheets/d/1PvYKQiEU02H4BaQjbl-iCycD_7B7_5mcs9gk_01EGdc/edit#gid=0)

## Process for creating new-style recommendations
Working notes - Arron and Sean developing in NABIT meetings

For now, all our recommendations will be internal, whilst we justify the business model of profitability potential of an agency working with Magento.


## WIKI Structure/Headings
- Pitch Email (with video)
  -- Text intro
  -- Video pitch product in Vidyard/Loom TBC
  -- Requirements (Eg New In feature requires Elasticsuite)
- Instructions
- QA
- Handover - ensure that the 'owner' provides a personal handover to the client




---

Hidden under comments below, is the original concept that this would be the public vids, we will facilitate these once Brandon is achieving over 6 hours billables per day PLUS there is still a solid backlog of tasks in Operations. Both these 2 suggest we are ready to scale, add a staff member and invest in public WIKIs.


<!--
All this content is for the old video recommendations which is phase 2


### Applications
TBC
- quicktime
- OBS - Arron investigating

### Acme Organisation
- the instances are not rolling up - arron will review
Arron to update once instances roll up.

### Format
- do we top and tail the video or just note in every WIKI that we have already created an instance, and link after to the deploy process?

Start the tuturial with an Acme Instance ready
audio - noise reduction filter - review options
Finish the tutorial with..... now commit your changes and you are ready to deploy

#### Check List for recording - screen-cast and face-cam
- Always use Google Chrome
- Always hide your bookmarks bar
- Always use the same resolution
- Always login to MDOQ as wile.e.coyote@acme-stuff.co.uk / Password123


TODO before we are ready

clean up deleting instances - Adam


Reuben working on SMTP Extension
Arron working on [sub-category listings])https://wiki.zero1.co.uk/en/services/consultancy/shared-recommendations/gb116)

-->
### Task handling process
Shared/Global recommendations will be created in the project 'Recommendations' task list. They require no triage process. The 'Recommendations' task list defaults are set to add the following tags: 

- Recommendation
- Awaiting client

When a client comments on a task, automation (A15) will remove the Awaiting client tag. The removal of the Awaiting client tag from any task in **this task list specifically** will then trigger automation (A12), which will fire a comment into the 'Recommendations' channel of Slack with instructions:

"Client has responded to this recommendation - PM to review immediately"

Action required by: PM

Actions required:

**Non critical recommendation ACCEPTED**
1. Acknowledge... "Thanks for your instruction. We will discuss the scheduling of this during our next catch up call"
2. Update task Estimation
3. Assign the task (Likely assignee should be detailed in the task description)
4. Move task to prioritise column

**Non critical recommendation DECLINED**
1. Acknowledge... "Thanks for your instruction. I will close this recommendation task"
2. Close task

**Critical recommendation ACCEPTED**
1. Check client isn't 200%+ overused
2. Acknowledge... "Thanks for your instruction. We will progress this as a high priority"
3. Update task Estimation
4. Mark as High priority
5. Assign the task (Likely assignee should be detailed in the task description)
6. Move task to not started column

**Critical recommendation DECLINED**
1. Acknowledge... "Thanks for your instruction. I will close this recommendation task"
2. Close task







