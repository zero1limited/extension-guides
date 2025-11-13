# Creating a new Retainer Project In JIRA
- Open Jira > Select the Jira product
- The list of existing projects will be displayed. Click 'Create Project'
- From the list of Project Templates choose 'Software Project' > Kanban > Use template > Select Company Managed Project
- Add project Details 'Company name - website url MC'
- Add Project Key, use the first 3 letters of the client company name + MC' e.g Divine Trash MC would be 'DIVMC', Abakhan MC could be 'ABAMC', epicmilitaria could be 'EPIMC'
- Click to select 'Share settings from another project > Jira ACME Reatiner'. This is going to be our template for schemes. Click 'Next'
- Invite teammates can be skipped
- Connect confluence Page and name it with the website url for the project you have just created > Click Create > Continue
Your project is now created but needs further configuration.

## Configuring your Jira Project 
- Go back to Project
- Go to Project settings > Summary
This page is a summary of the project configuration check the schemes are as below.

### Schemes
Schemes in use should be:
1. Issue Type Scheme: AC: Jira Service Management Issue Type Scheme
2. Priorities default: Lowest
3. Workflow scheme: Retainer workflow scheme
4. Screens scheme: ACME: Kanban Issue Type Screen Scheme
5. Fields scheme: System Default Field Configuration
6. Settings: Application Links: Configure Project Links, JIRA Mobile Connect: Disabled
7. Versions: This project has no unarchived versions
8. Componenets - SEE ACTIONS
9. Roles - SEE ACTIONS
10. Permissions - SEE ACTIONS
11. Notifications - SEE ACTIONS
12. Development Tools - SEE ACTIONS

Now that your Jira Project is set up, we need to set up a service Project where the client can raise requests. 


# Creating a filter for Tempo
Before you can create the Tempo project you need to create a filter in JIRA that will filter everything from the 2 projects you have just created. The Tempo project that you are about to create will use this filter to pull information from these 2 projects, including Assignees, tasks, timelogs etc. 
- Open Jira > Filters > Create a filter
- Click the 'Project' search for and select the 2 projects you have already created
- Save filter as 'Company MC MASTER' e.g 'Divine Trash MC MASTER'
Now you are ready to create the Tempo project

# Creating Tempo Project
- Open Jira > Apps > Tempo
- In the left hand column click on Projects > Create Project
- Name the project 'Company MC MASTER' e.g 'Divine Trash MC MASTER'
- Scope > find and select
- Project type: Time baes
- Revenue tracking: OFF
- Create & Configure
- Timeframe: Must ALWAYS start from the 1st of a month and end on the last day of the month
- Project Status: In progress
- Project type: Time-based
- Budget: = the number of monthly hours the customer has selected under their retainer contract
- Revenue Tracking: OFF
- Auto Sync scope: OFF
- In the left hand panel select 'Sharing'
- General Access: Users with Tempo Project Access
- Individuals with Access: Editor 'Suzanne Moss' & Arron Moss'
- Click on Scope > Sync scope

# Allocating the Team to all 3 projects
## Jira
- Go to the Jira project > Project Settings > Permissions > check the team has permission to 1. Browse Projects, 2. Work on Issues
## Tempo
- Go to Tempo > Teams > click on the team you want to use > Add links to Project, select the MC & SUP projects




