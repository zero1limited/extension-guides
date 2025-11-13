# Proactive Module Upgrade Process

[TOC]


There are 2 main approaches to this process, either looking at specific modules (Ie if we have learnt there is a new critical module upgrade or new feature and need to roll it out to everyone using it (using route 1 below), or by being told we have a customer who we are concentrating on because they are new, have loads of spare time or simply been asked by management, this is route 2.

## Route 1 - raising recommendations based on specific module

Load the ‘All’ view from airtable.com
Sorting by the package column, and seek out the modules which are most prevalent and have a range of installed version numbers (suggesting definitely upgrades available)
Pick the website lowest version number
Some other checks TBC, customer is MC, has time, has access to upgradable version.
run `composer show -o m2epro/magento2-extension | grep 'latest\|versions'` - this will return the current version installed and the latest version available. If there is a new version available you can proceed.


## Route 2 - raising recommendations based on specific client

Identify clients suitable for recommendations using the [Scrum Master Doc](https://docs.google.com/spreadsheets/d/1Hgeg2-OXvyz2UDRRcbKSHqrWQzVCoTKTWsOs4zIGpo8/edit?pli=1#gid=800896216). Load the menu item data > filter for 'Proactive module upgrades'. If the client is on this filtered view AND does NOT have any form of large upgrade in progress, they are a candidate for recommendations.

Find an unused MDOQ development instance (usually TEST) for the client and login via SSH.
Run `cd ~/htdocs && composer show -o` which will return the current version installed and the latest version available .
What you are looking for here are updatable versions which are in the ‘require’ part of the composer.json files NOT including core Magento one starting ‘magento/’

At this point you should have a list of extensions, please run these via Arron (for now) in the customers slack channel. Once Arron confirms

## Proceed with steps - both routes

### Checks for overrides

This is an extremely important step. Basically if we are upgrading an extension which has lots of front-end template overrides, then there could be risks. So we must first identify this.

`composer show m2epro/magento2-extension | grep 'path'`

1. get the path value then view the extensions `etc/module.xml` file to get the proper Module Name Ie Ess_M2ePro with that module name you can see if there are theme overrides with `grep -R "Ess_M2ePro" app/design/`


### Email customer via teamwork messages

Instructions for ZERO-1.
NOTE: If the client is really behind with modules, it might be that you are best selecting the 'multiple' recommendation route/template below.

1. Go to the Teamwork MC Project, then Messages
2. Click ‘Add a Message’ then ‘Select People’ (under ‘Who should be notified’)
3. Select the ‘Teams’ tab then tick the checkbox next to ‘Product Owner’ under ‘Teams only on this project’ (VERY important). You can check the members also to ensure they look like customer contacts, the Project manager is also part of this team for visibility purposes)
4. Copy the Subject below replacing the extension name and FROM/TO version numbers and paste it into the field ‘Message subject line’
5. Copy the main message below (between the lines) into the main message box ensuring the bold extension names/versions are correct. Click ‘Post Message’.


### Template Subject - single recommendation:

Recommendation to upgrade EXTENSION_NAME from CURRENT_VERSION to NEW_VERSION
### Template Content:

This is a recommendation to update one of your Magento Extensions.

We've noticed that your website isn't up to date with the latest version of EXTENSION_NAME.

Your current installed version is CURRENT_VERSION, the latest available version is NEW_VERSION -link to release notes if applicable

We'd like to upgrade this extension so that you can take advantage of new features and fixes, also ensuring you are more prepared for future upgrades.
Let us know if you're happy to proceed simply by responding to this email. We ask to allocate approximately 1 hour for extension upgrades. Sometimes this can escalate if the extension is complex or contains customisations. If this is the case a member of our team will reach out to you.

Kind Regards,
Brandon - ZERO-1 Operations Team


### Template Subject - multiple recommendation:

Recommendation to upgrade VENDOR_NAME modules

### Template Content:

This is a recommendation to update some of your Magento Extensions from VENDOR_NAME since we've noticed that you have outdated versions installed.

Your current installed versions are:
VENDOR_NAME EXTENSION_NAME: CURRENT_VERSION
VENDOR_NAME EXTENSION_NAME: CURRENT_VERSION

The latest available versions are:

VENDOR_NAME EXTENSION_NAME: NEW_VERSION  - https://link.com/

VENDOR_NAME EXTENSION_NAME: NEW_VERSION  -  https://link.com/


We'd like to upgrade these extensions so that you can take advantage of new features or fixes, also ensuring you are more prepared for future upgrades.

Let us know if you're happy to proceed simply by responding to this email. We ask to allocate approximately 1 hour for extension upgrades. Sometimes this can escalate if the extension is complex or contains customisations. If this is the case,  a member of our team will reach out to you.

Kind Regards,
Brandon, ZERO-1 Operations Team

---




_N.B: If the customer declines please inform the project account manager._

### Creating a task when the client has accepted the recommendation.

As the Project Manager is also part of the Product Owner Team, they will receive notification of any communications relating to the recommendation messages, including when the message is raised and any subsequent responses or discussions on the messages. It is the Project Managers responsibility to create the task once the recommendation has been approved. The process to add a task is as follows: 
1. Client adds a comment to approve the recommendation.
2. PM copies the subject title of the approved recommendation.
3. PM navigates to the 'List' view on the project and opens the 'Recommendations' task list.
4. Click 'Add task'and paste the copied subject in as the task title
5. Copy the body of the recommendation email message into the task description
6. Add Brandon Morgan as the assignee
7. Add the estimation outlined in the recommendation message
8. Add start date as Today
9. Add due date as +2 days
10. Add to 'Not started' board
11. Add task (MAKE SURE THE CLIENT ISNT NOTIFIED OR IS SET AS A FOLLOWER OF CHNGES OR COMMENTS)
12. Add the following as private comment to the task - Instructions https://wiki2.zero1.co.uk/docs/main/dept-operations/composer#content-upgrading-magento-modules
13. Copy the task URL


### Messaging the client to acknowledge approval
This will be actioned by the Project Manager once the task has been created

1. Go back to the recommendation message and add the following comment:

Hi [Client name], 

Thank you for approving our recommendation. We have now created a task for this piece of work [task url]. 
Please note: Any further updates relating to this work will be sent directly from the task. Should you have any questions please feel free to ask in the comment section of the task.

Many thanks
[Your name]
2. Notify the product owner team of the comment


## Route 3 - rennovate bot upgrades
We are using rennovate bot to determine modules that can be updated. This service should determine what modules can be upgraded and automatically install them.
This process is detailed here: [renovate](/dept-operations/renovate.md)