# Request lifecycle summary

- All requests come through JSM and are categorized by work type based on how they are submitted.
- Critical issues remain and are resolved in JSM by the SRE team.
- Support and Change requests are automatically mirrored as linked tasks in the appropriate Jira Software project.
- The Product Owner and Project Manager triage and prioritise these tasks in the Jira backlog for future development.

# Non-Critical requests

There are 3 request types availble: 
1. Support
2. Change request
3. Critical-issue

Methods 1 & 2 will trigger [this](https://zero1commerce.atlassian.net/jira/servicedesk/projects/AC/settings/automate#/rule/27977333) which will create a linked task in the clients Jira project. 

WHAT HAPPENS TO THEM FROM HERE? 

# Critical requests
Can be submitted via:
1. A form completed by the client from the Portal in the portal group 'Critical Support'
2. An email submitted by the client (sent to the clients dedicated email address ADD ADDRESS

WHAT HAPPENS TO THEM FROM HERE? 
 

What is missing? 

1. https://github.com/zero1limited/wiki/blob/main/Jira/jira_conguration
2. Deciding on Project types required. ie Scrum for 50+ and Kanban for anything lower?
3. Review of workflow for Non Critical requests
4. Board configuration - Swimlane for 'Planned this month'?
5. Creating automations for task actions
6. Workload planning process
7. Budget management process
8. Communication process, canned responses
9. Setting up the correct permissions
10. Notifications
11. Staff Training 
12. Selecting a Project & Migrating tasks & Time from TW 













      
# Status Critical triggers an automation to:
    - Add comms to client
    - Notifies Slack
    - Create linked issue in the the Jira project and adds Highest priority and a label 'Critical Support'























# Requests submitted via email 
- Work Type request = Emailed request
- Queue = Unassigned issue (Once assigned it moves to the 'All open' Queue

# Notification of a new request





- Critical issue
- Epic
- Story
- Task
- Sub task
- Recommendation
