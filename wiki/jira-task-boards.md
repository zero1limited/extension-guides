All retainer Projects should use the workflow '[New Simplified workflow](https://zero1commerce.atlassian.net/secure/admin/workflows/ViewWorkflowSteps.jspa?workflowMode=live&workflowName=New%20Simplified%20workflow)

[TOC]

# Board Governance - Transitions and statuses(Actions & board Columns) 

## Create -> Backlog
- Is where all new issues will be placed automatically
- Is a container for all sssues that are not ready to be moved forward, such as 'On-hold' issues
- This column will be regularly groomed by the PM & PO
- Any issues that are 6+months old should be closed, as they will likely be out of date or irrelevant
- issues can be moved to this status  
- All status's can transition to this status
- 
## Prioritise
- Is a container for all issues that the PO would like to achieve within the next 3 months
- The PO & PM will regularly review this column and decide which issues are to be scoped/Estimated, or scheduled if already estimated
- All status's can transition to this status


## Estimate
(could be called Selected for Review)
IMO This is where many of our headaches could be mitigated. Issues we need to overcome include but are not limited to: 
- Unclear requirements ends up with tasks awaiting client, which leads to stalled tasks and instance blockers
- Lack of clarify on delivery plan, often means tasks pass betweeen team members unexpectedly causing client frustrations and scheduling problems

We need to educate clients to start planning well in advance. There shouldnt be any 'critical issues' in Jira cloud, so we need to be firm and not be so keen to get ourselves into a mess because the client hasnt planned well. 
I propose that all issues should be categorised for size by the Team leader as follows.... 

ALL ESTIMATIONS SHOULD INCLUDE A MMINIMUM OF 1 HR FOR ROLLUP, QA AND DEPLOYMENT

### Small (upto 4hrs)
#### Single assignee
1. Ensure that client requirements are clear 
2. Comments to client on Linked JSM ticket if clarification is required
3. Adds detail of their delivery plan and any specific tests that QA need to perform and add their estimation. 
4. If pre-agreed with the client on a call, the assignee can choose to move the issue into the next stage 'Selected for developemt'. 
5. If not pre-agreed, the assignee would move the issue back to 'Prioritise' for the PO & PM to review in the next planning session

#### Multiple assignees e.g FE & BE
1. Ensure that client requirements are clear 
2. Comments to client on Linked JSM ticket if clarification is required
3. Call required between assigness 
4. Sub tasks created and assigned (1 for each assignee)
5. Sub tasks are estimated
6. Parent task is updated with the overall plan and any specific tests required from QA
7. One of the assignees takes responsibility for adding the total estimation to the parent task
8. If pre-agreed with the client on a call, the assignee can choose to move the issue into the next stage 'Selected for development'. 
9. If not pre-agreed, the assignee would move the issue back to 'Prioritise' for the PO & PM to review in the next planning session

### Medium (Upto 8 hrs)

#### Single assignee
1. Ensure that client requirements are clear 
2. Comments to client on Linked JSM ticket if clarification is required
3. Send client a CR doc via Linked JSM ticket (adjust until client agrees requirements)
4. Add Approved CR doc to the Jira cloud task, Add detail of delivery plan and any specific tests that QA need to perform and add their estimation. 
5. If pre-agreed with the client on a call, the assignee can choose to move the issue into the next stage 'Selected for developemt'. 
6. If not pre-agreed, the assignee would move the issue back to 'Prioritise' for the PO & PM to review in the next planning session

#### Multiple assignees e.g FE & BE
1. Ensure that client requirements are clear 
2. Comments to client on Linked JSM ticket if clarification is required
3. Call required between assigness to write CR doc - one assignee takes respomsibility for sending the CR doc to the client via JSM ticket (adjust until client agrees requirements)
4. Assignee adds Approved CR doc to the Jira cloud task
4. Add detail of delivery plan and any specific tests that QA need to perform and add their estimation.
4. Sub tasks created and assigned (1 for each assignee)
5. Sub tasks are estimated
6. Parent task is updated with the overall plan and any specific tests required from QA
7. One of the assignees takes responsibility for adding the total estimation to the parent task
8. If pre-agreed with the client on a call, the assignee can choose to move the issue into the next stage 'Selected for development'. 
9. If not pre-agreed, the assignee would move the issue back to 'Prioritise' for the PO & PM to review in the next planning session
## NEED TO ADD A TRANSITION TO MOVE TASK BACK TO PRIORITISE

### Large (8+ hrs)
1. Meeting required with PM to assess whether this requires an Epic


@suz this is where I get confused, you have already listed this board title above and put 'not required at this stage'. I need to understand your plan clearly but can't.

## Ready to do -> Selected for development
- Contains all issues that scoped, estimated, tasked out correctly and are 'Ready to do'
- Assignees can pull issues from this column into 'In progress'

## In Progress
- Contains active issues
- Assignees can transition these issues to: 
## NEEDS TRANSITION TO BYPASS QA IF WORK DEPLOYED BY DEV

## Ready for testing -> Acceptance
- Contains all work for QA
- Trasitions incldue: 
    - Failed testing -> In progress
    - Ready to deploy -> Done

## Done
- Development has passed QA and is, work is ready for deployment to either: 
    - Non Prod 
    - Prod
    - No deployment required
    ## NEEDS DISCUSSION

## Deployed to Prod





## NEEDS DISCUSSION
## WE NEED TRANSITIONS TO RECORD WHY A TASK WAS DONE (DEPLOYED, NOT PROGRESSED, CONFIG ETC)
## WE NEED TO ADD 'RESOLVED' SOMEWHERE TO ACTUALLY CLOSE THE ISSUE


