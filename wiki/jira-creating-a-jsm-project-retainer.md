#Creating a JSM Retainer Project

Responsibility: Project Manager
Project Type: <50 hour Retainer Project 

## Creating the JSM Project
- Open Jira > Select the Jira Service Management Product
- Click 'Create Project'
- Choose the template 'Service Management' > Advance IT Service Management > Use template
- Add project Details 'Company name - website url SUP' e.g. Divine Trash - divinetrash.co.uk SUP
- Add Project Key, use the first 3 letters of the client company name + SM' e.g Divine Trash would be 'DIVSM', Abakhan could be 'ABASM', epicmilitaria could be 'EPISM'
- Team Type: Software Development
- Access: Restricted
- Click to select 'Share settings from another project > ACME (AC)

## Configuring the JSM Project
 

## JSM Queues
## JSM Portal Forms
- Go to the ACME (AC) project > Project Settings > Forms > Click on the 3 dots and select 'Copy to Project'. You will need to do this for all forms.
- Go to the new proect you have just created > Project Settings > Forms > Click on the 3 dots and select 'Copy to Project'. You will need to do this for all forms.
- Click into each form and click on each form question to check it is mapping to the fields in Jira Summary > Summary, Description > Desctiption etc
- Go to Project Settings > Request type 'Problem' The form 'report a problem' should show there. You need to associate it with the request type group 'Support'
- Go to Project Settings > Request type 'Change request' The form 'report a Request a change' should show there. You need to associate it with the request type group 'Change request'
- Go to Project Settings > Request type 'Critical Issue' The form 'Report a critical issue'should show there. You need to associate it with the request type group 'Critical issue'









### Automations
### Portal settings
## Customer Users, Permissions & Settings
### Adding the client company to Organizations
- Global settings > Product > JSM > Organizations > Add Organization
### Adding the organization to the JSM Project
- JSM Project > Customers > Organizations > Add Organization > Select Organization
### Adding customers to their Organization
- JSM Project > Customers > Organizations > Add Customers > Enter customer email address.

# Creating Tempo Project to track time
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

# Allocating the Team
## JSM
- Go to the Jira project > Project Settings > Permissions > check the team has permission to 1. Browse Projects, 2. Work on Issues
## Tempo
- Go to Tempo > Teams > click on the team you want to use > Add links to Project, select the MC & SUP projects
