# Setting up Retainer project budgets

## Before Setting up the Project Budget
Before you can create the Tempo Budget you need to create a filter in JIRA for the projects that your the budget manager application should pull time logs from .e.g Jira and JSM, or just Jira.

- Open Jira > Filters > Create a filter
- Click the 'Project' search for and select the 2 projects you have already created
- Save filter as 'Tempo budget ACME'(replacing ACME with the client company name)

## Setting up the budget
- Open Jira > Apps > Tempo > Financial Manager
- In the left hand column click on Projects > Create Project
- Name the project 'Client company name - Retainer' e.g 'ACME Retainer'
- Scope > Filter > Select the filter you have just made in Jira
- Revenue tracking: OFF
- Create & Configure
- Budget start date: Must ALWAYS start from the 1st of a month and end on the last day of the month 
- Budget end date: Retainers are subject to 90 days notice so the end date should be the last day of the 3rd month. Eg Start 1st Feb, End 30th April  
- Project Status: In progress
- Project type: Time-based
- Budget: = the number of monthly hours the customer has selected under their retainer contract
- Revenue Tracking: OFF
- Auto Sync scope: OFF
- In the left hand panel select 'Sharing'
- General Access: Users with Tempo Project Access
- Individuals with Access: Editor 'Suzanne Moss' & Arron Moss'
- Click on Scope > Sync scope - This pulls all time logs and tasks into the budget manager

## Monitoring the budgets
Jira > Apps > Tempo > Financial Manager > Portfolios > [Retainer budgets overview](https://zero1commerce.atlassian.net/plugins/servlet/ac/io.tempo.jira/tempo-app#!/financial-manager/portfolio/43c13caf-7ddb-4508-944a-4df73e0b664d/summary
)
This should be reviewed daily by the Project/Financial Manager 
## Adjusting the budget
The initial budget is set as a 3 month budget (Notice period), At the end of month 1 we extend the budget period by 1 month. This will be reflected in the budget [overview page](https://zero1commerce.atlassian.net/plugins/servlet/ac/io.tempo.jira/tempo-app#!/financial-manager/project/cd6ba62d-6ec8-46f3-a928-7ac350637df9/overview)

### Borrowing time 
If a client asks to borrow hours we can adjust the budget period by [adding](https://zero1commerce.atlassian.net/plugins/servlet/ac/io.tempo.jira/tempo-app#!/financial-manager/project/cd6ba62d-6ec8-46f3-a928-7ac350637df9/configuration/general) a 4th month early making a note of this in the [project confluence doc](https://zero1commerce.atlassian.net/wiki/spaces/AKB1/pages/edit-v2/9765148)

We need to agree and document the borrowing limit! 
### Banking time
If a client isnt consuming their hours and is effectively 'banking time' they will still have their budget adjusted each month, but we need to agree and document the agreed process for triggers & comms e.g

|Underused by  |Trigger               |Comms                                                                                                         |
|:------------:|:---------------------|:-------------------------------------------------------------------------------------------------------------|
|1 month       |Raise recommendations |You have x hours banked, we will raise some recommendations, but please feel free to raise any requests       |
|2 Months      |PM Call               |PM to discuss (& document) the risk of lost hours if they reach 30 hrs underused                              |
|3 months      |Email or call         |Due to lack of use of the service you have now lost the hours banked in month 1 (escalate to Account Manager) |

If we are going to update the project confluence doc each month then we could use that to record comms to the client




### Crediting time / Invoiving off time
We can simply adjust budget for the relevant month (effectively increasing the budget) and we update budget summary in the confluence doc 


## Monthly budget reconciliation
At the end of each month, a new month is added to the budget and the budget period increased by 1 month

## Reporting the budget to the client
JSM users without Confluence licenses can view linked Confluence pages, including those in knowledge base spaces.
Confluence doesnt natively link to Tempo financial manager, so as an MVP we could have a confluence page for each project and manually produce a budget summary at the end of each month. eg https://zero1commerce.atlassian.net/wiki/spaces/AKB1/pages/edit-v2/9765148



