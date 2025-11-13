
# Work Types 

## Creating a new work type - Jira (Global)
A work type (formerly Issue type) are types of requests that can be made by the customer of the team .e.g. Support, Change request, Critical issue, Task etc. 
Work types are created at a Global level in Jira Settings > Work Items > Work types
https://zero1commerce.atlassian.net/jira/settings/issues/issue-types

Jira already has lots of default issue types created. 

Before an Issue type can be used, you need to add it to a Work type scheme. 

## Work type scheme - Jira (Global)
A work type scheme is a group of issue types that are grouped together to form a scheme. This scheme can be used across multiple projects that need to use exactly the same issue types e.g. All retainer projects can use the same work type scheme as they should all need the same work types, so we have created a scheme called **'Retainer work type'** into which I have added the following work types: 

- Support
- Change request
- Critical Issue

Once you have created the scheme you need to associate the scheme to your project

## Associating a work type scheme to a project - Jira (Project)
To associate a work type scheme to your project navigate to Project > Project Settings > Summary > click on Issue type. You can change the scheme from there. 

# Workflows - Jira (Global)
Each Work type needs to have an associated workflow. 
You can create a new workflow at Global level I think we can limit it to 3 workflows for retainers [here](https://zero1commerce.atlassian.net/jira/settings/issues/workflows) 

1. [Critical-issue workflow](https://zero1commerce.atlassian.net/secure/admin/workflows/WorkflowDesigner.jspa?workflowMode=draft&wfName=Critical-Issue%20workflow) 
2. [Change request workflow](https://zero1commerce.atlassian.net/secure/admin/workflows/WorkflowDesigner.jspa?workflowMode=live&wfName=Non%20SRE%20Retainer%20Workflow)
3. [Support workflow](https://zero1commerce.atlassian.net/secure/admin/workflows/WorkflowDesigner.jspa?workflowMode=draft&wfName=Support%20Workflow)


## Workflow schemes - Jira (Global)
I have created a new Workflow scheme [Retainer workflow scheme](https://zero1commerce.atlassian.net/secure/admin/EditWorkflowScheme.jspa?schemeId=10104) into which, the 3 new workflows have been added.

At a Project level I have switched the workflow scheme to 'Retainer workflow scheme'
Project > Project Settings > Summary > Workflows. You can change the scheme from there. 


# Portal groups - Jira Service Management (Project)
Project > Project Settings > Channels & Self Service > Portal
This is where you can make request types show in the customer portal. We have configued 2 portal groups: 

- Support
- Request a change

# Request types - Jira Service Management (Project)
A request type is a form that we build that customers can fill out to submit a request. You can build a form [here](https://zero1commerce.atlassian.net/jira/servicedesk/projects/AC/settings/forms)
Before your form can be used you need to ensure your form has the following:
- Work type Allocated
- Portal group allocated
- Workflow allocated
- You can allocate Work types, change the portal group and workflow [here](https://zero1commerce.atlassian.net/jira/servicedesk/projects/AC/settings/request-types/category/incidents)
- Note: Until a work type has been allocated, your form will sit under Request types > Unallocated

# Screens
There are various screens available. To identify which screen is being used for a particular work type .i.e 'Support' requests, follow these steps: 

1. Go to the JSM project > Settings > Request types > find the work type you are looking for (Support) and click on it > Make a note of the 'Request type'
2. Go to Jira global settings > Work items > Issue type screen schemes > Locate the scheme being used by your project .e.g 'Jira service management issue type screen scheme' > Click configure > 
# DO I need to create schemes for JSM, or can I add JSM requests to the Jira schemes????? 


# Done
1. Basic forms created in JSM
2. Work types allocated in JSM
3. Work type scheme created in JSM and the work types allocated to the scheme
4. Basic forms created , added to the portal, associated with work type scheme
5. Basic portal groups created
6. Workflows created for each work type - Not fully set up - needs further discussion on statuses and transitions
7. Tempo time tracker set up
8. Tempo Financial Manager set up (using custom filters to pull time logs from JSM & Jira)
9. Teams created

 
# To Do: 
1. Polish the basic forms & Map all the fields to the screen being used 
2. Understand whether the work types in Jira need to match the JSM work types exactly - Can they both use the same Work type scheme? 
3. Understand the Screens required in both JSM & Jira. Can we just use 1 screen for everything and put that in a screen scheme that both JSM and Jira uses? 
4. Understand how the assignee makes the transitions that change the status - I had seen on a video a fied where the assignee selected the transition on the task screen, which I'm guessing moves the task to the relevant status according to the workflow. How do we set this up? 
5. Configure & Document the workflows
6. Check that all form fields are associated with the fields in the screens being used so the assignee can see all the relevant information
7. Decide whether we use a project template plug in per https://zero1hq.slack.com/archives/C6UDMQSBD/p1746196972564329
8. Decide whether we have 1 global board only
9. Create a support email for all customers to use & add address to wiki
10. Make a decision on how we are going to manage retainer budgets
11. Set up automations for task notifications, Tasks transitioning etc
12. Document the permissions we need to set up 
13. Document Tempo settings and processes for reconciling budgets, buying additional hours, crediting time, writing off time etc. 
14. Understand & document workload planning
15. Prepape some staff training videos / sessions 


# Running an end to end support ticket test to identify gaps

## Report a problem

###  Ticket creation and receipt
- Raising request - Ticket requested via the portal - Success
- Received in 'Problem' queue in ACME JSM - Success
- Team notification - **FAIL**
- Client acknowledgement email - Success
- Linked ticket created in ACME 25hr retainer - Sucess

### Ticket info showing correctly in ACME JSM? 
- Form needs to ask for replication steps but otherwise all info captured - success
- The ticket is showing a 4 hr SLA. This needs removing - **FAIL**
- Default priority is showing as 'Medium' - this needs removing - **FAIL** 
- There are a load of irrelevant fields showing - remove these - **FAIL**

### Ticket info showing correctly in ACME 25hr retainer? 
- There are more tickets in the retainer than there are in the service project. Can we automate deletion of the linked tickets when a ticket is deleted, or closed? We need either an automation of a fail safe process to avoid ticket misalignment. - **FAIL**
- The ticket type icon is the same for Change request and support, this needs changing for visual identification - **FAIL**

### Ticket showing on the Kanban board? 
- Nope, This is because there is no workflow **FAIL**
- Yes, now showing. And the transitions work in board view and issue view screen

### Ticket showing in the backlog
- Yes

### Ticket showing and logging time in Tempo? 
- Showing? Yes
- Logging time? Yes

### Updating the client on a ticket
- Sending canned response - Success
- Receiving the update as a customer - success
- Replying as a customer - Success
- Receiving notification of the response as an assignee - **FAIL**

# FAIL - Actions required
- Set up internal notification for ticket received
- Amend support form to include a request for replication steps
- Remove the 4 hr SLA from the support ticket JSM view issue screen
- ~~Change Default Priority to low~~ 
- Remove unrequired fields from support ticket JSM view issue screen
- Investigate why the no. of tickets differ between the 2 Acme projeccts
- Make the ticket type icons for support and change request differ from each other (JIRA)
- ~~Create a Support workflow~~
- ~~Associate the worklfow to the project~~ 
- ~~Map the workflow status's to the Kanban board~~ 
- Allocate a permisisons scheme - DONE
- ~~Add permissions to allow assignee & PM to be able to transition a ticket~~ 
- Add comment received notifications when client adds a comment to a ticket
 

