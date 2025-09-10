## Quality Assurance Department
Our values here are to invest in scalable testing for a very focussed Market Ie Magento merchants using Hyvä

• Write as many small tests as possible
• Write a custom Magento module which can help an Automation Suite know which tests to run (in progress)
• Market / Share the tests

[TOC]



## Onboarding New Customers

1. PRA steps
  * ii - RECaptcha
  * iii - Mailcatcher - prevent it being caught so it will go to GI
  * iiii - Sandbox payments as per what the client has [wiki link here](https://wiki2.zero1.co.uk/docs/main/guide-payments)
  * iiii - Mail sending settings - Mail sending was active and sent a live email from our test yesterday - an option to get around this might be us being able to get around it with a PRA to change the order email contact (on instances) though
2. install this extension `composer require zero1/ghost-inspector`
3. Create the ghost-inspector.yml in the root [according to the docs](https://github.com/zero1limited/magento2-ghost-inspector)


## Task Enters QA

QA team members are responsible for: 

- Checking the [QA Board](https://zero1.teamwork.com/#/people/30115/boards/link-here-suz) for any tasks assigned to 'Anyone' or the "Quality Assurance" team (Once we have Dept Slack Channels Arron plans to drop notes in, staff will be measured on their ability to take tasks promptly whilst avoiding spinning too many plates).
- Assign tasks to yourself.
- Quickly review the task to understand the requirement (bug fixed, CR document clearly detailing whats expected in the acceptance box or a developer explanation of work carried out). If none of these are present, pass back to the developer requesting a work explanation.
- Confirming with the developer if the work will require a downtime release (they should include this in their explanation of work carried out. If they don't, ask them in the clients Slack channel).
- Ensuring the instance is at the client acceptance stage or following the review process if its failed regression testing.
- Test the recreated instance against the requirements outlined (either CR Doc or clear outline of issue).

## Automated Regression Testing
If the instance fails regression testing, it is up to a member of the QA team to determine if this issue was caused by the development or if it was a false negative. (i.e an issue with the test).
- Alert the QA team that your instance has failed regression testing by sending them a message with the instance link in the clients Slack channel.

#### QA Review process for failed tests
1. Go to the suite that failed in Ghost Inspector and find the result corsponding to the instance that failed.
2. Review each test that failed to determine if it failed due to the development work or the test itself.
3. Review all the videos of the tests in the suite (inlcuding the passing ones) to ensure there aren't any issues the tests failed to pickup.
4. If the cause of the fail is down to the development, you need pass the task back to the developer with a comment stating the issues.

4b. If the cause of the fail is down to the regression test, this needs to be flagged to 1st line, by putting an internal comment in the task. "Instance failed regression test [link to regression test result]. I believe this to be an issue with the test, rather than the work". The instance can then be pushed forward to the next stage of the I'm done process, then manually QA'd and handed over to the client for approval.

## Manual QA
1. Carry out a manual regression test of the site. [Intial QA regression testing doc](https://docs.google.com/spreadsheets/d/1LfUVlcbOLwi2gdHH_zaS67Kdd6rb47kQzYP4Gb4NJQs/edit?usp=sharing).
2. Test all the work carried out on the instance (as per the destription of the work in the task).
3. Review all the files in var/log to ensure there's no exceptions been thrown by the work.
- If the tests are not successful please pass back to the developer. (making sure to add key info of all errors found to the ticket).
- If the tests are successful please add a comment "manual regression testing completed".
4. Handover the instance links to the client and ask them to approve the work.
5. Once approved click "client accepted" and create a tag based on the current date. Example: 3.2025.32.00 then 3.2025.32.01 then 3.2025.32.02 etc...
6. Organise a time and date with the client for the work to go live. 


#### Requirements NOT met / QA Failed
- If the test fails QA will move the task back to the assignee that carried out the work (making sure to add key info of all errors found to the ticket) and move it to the department from which it originated. SUZ TO CHECK THIS IS POSSIBLE WITH CURRENT BOARD VIEW RESTRICTIONS!!!!

#### Requirements met / task accepted
- Organise a release for the work with the client (release cutoff time for each day is 3pm, try and avoid Friday releases if possible).

## Pass to Ready for Release
**Visit https://wiki.zero1.co.uk/docs/main/guide-deployment-process for process**


## Ghost Inspector Test Improvement Plan for Hyva Sites
- TODO, dicussion required with Arron.


## Creating new tests
Try to keep the test as isolated as possible, relevant only to the module in question. If other components are required try and Import them from [___ Global Hyva Site Modules](https://app.ghostinspector.com/suites/63bfdc1faf1e488d25edd887) as steps rather than duplicate steps.
Attempt to write the test using https://demo.hyva.io/
- Suite for Hyva tests: [___ Global Hyva Site Tests](https://app.ghostinspector.com/suites/657f3c136e489be528424c9e)

## Misc

### Test Name Conventions
Naming conventions for tests are simple but critical

Vendor_ModuleName-TestName

Example Magento_GroupedProduct-Default - this test might specifically run default tests to interact with the grouped product
Example Hyva_Checkout-Default - this test might specifically run default tests to test the Hyvä Checkout features

## How to locate where your tests belong/module names
- Visit FE and inspect code where the button lives that you want to find (for example click and collect option or instore delivery)
- While in inspect, attempt to find something unique - id selector is always a good option
- Once you have your chosen selector, copy to your clipboard
- Visit MDOQ and go to code editor (Visual Store Code)
- When in code editor, go to the 2 page icon in the left hand area. Explorer
- Find app in the menu and press control and click
- A box should appear and select Find in Folder
- In the search box - paste your unique selector you copied
- See what results appear, if no results
- In the files to include box where is stating ./app change this to say ./vendor
- If still no results, refine the copied selector that is in the search box
- For example - a selector could be shipping-type-click_and_collect and amend this to click_and_collect
- With the text amended you should hopefully see results
- Once this has been performed and you have reviewed the results - click on the di.xml, located under the item name line and then follow the name of the module back through the folders - for example vendor/zero1/magento2-click-and-collect-hyva-checkout/etc/di.xml to find this within the code editor
- Go back to the Explorer icon again - 2 page icon in the top left area
- Click on vendor > zero1 > magento 2 > click and collect hyva checkout > etc > registration and you should find the concrete information ie the EXACT name of the module that triggers the button click on the FE of the site. For this wiki example it would be this - Zero1_ClickAndCollectHyvaCheckout
- Take the module name you've found and open app/etc/config.php then compare the module name with what's in app/etc/config.php. For this wiki example it would be this - Zero1_ClickAndCollectHyvaCheckout
- Now you've got the name, example: Zero1_ClickAndCollectHyvaCheckout go to the [spreadsheet](https://docs.google.com/spreadsheets/d/1BQFovZGSemKuc7SwmSh9zjrpEKHcMjSGlpEwENv68uM/edit?gid=817744772#gid=817744772) Everything that is infront of the underscore will go in Vendor - in this case it would be: Zero1 then everything after the underscore will go in Module - in this case it would be: ClickAndCollectHyvaCheckout
- Finally the Test section of the name can be a descriptor of the test which can be anything.

### Testing website
- https://miami-zero1-co-uk-19929.30.mdoq.io/
- Customer account login credentials
- user - testing@zero1.co.uk
- password - Testing321

### Role and Responsibilities

Arron = Manage Test Exclusions - for now (to pass over to Craig going forward once set up)
list of exclusions - https://docs.google.com/spreadsheets/d/1BQFovZGSemKuc7SwmSh9zjrpEKHcMjSGlpEwENv68uM/edit#gid=1510622110

Craig = Take charge of creating new test based on clinets needs/custom modules.
*Take charge of the Exclusion Sheet
*Provide a daily update of what cell number we are on 

### Test Case

[___ Global Hyva Site Tests](https://app.ghostinspector.com/suites/657f3c136e489be528424c9e)
API `5ea993e7ab90be6bdeb7b0397904273e68b3b43d` SUITE `657f3c136e489be528424c9e`

Paste the following command into your local terminal application
```
CURL "https://api.ghostinspector.com/v1/suites/657f3c136e489be528424c9e/execute/?apiKey=5ea993e7ab90be6bdeb7b0397904273e68b3b43d&startUrl=https://miami-zero1-co-uk-19929.30.mdoq.io/"
```
the observe the [test progress here](https://app.ghostinspector.com/suites/657f3c136e489be528424c9e)

### Ghost Inspector Variables
You can find a list of variables that can assist you with creating GI tests. 

You can find the variables situated under the test in a small drop down menu. After console output.

If you view the results of any test which MDOQ has triggered you will see variables at the bottom

Variables has a small arrow to the right side of it and has a little drop drop arrow that will expand when pressed to give you a list  - for example here is a list obtained in this way from a test

*adminUrl

*magento_admin_password

*magento_admin_username

*random

*startUrl

*storeCode

*testName
