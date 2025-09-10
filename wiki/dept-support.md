
[TOC]

## Canned responses
Client communication is KEY to ensuring customer satisfaction. Please use the canned responses provided in this link. PLEASE USE COMMON SENSE BEFORE SENDING THE CANNED RESPONSE. IS THE WORDING APPROPRIATE FOR THE ISSUE BEING REPORTED????
[Canned Responses](http://wiki.zero1.co.uk/e/en/Support/1stline/Canned-responses)

## Airtable 
Airtable is used to store information in a database and for our purposes, we use Airtable to keep track of all the modules across/for each client.

https://airtable.com/appf5J9IhMYLrMjqw/tbl8pMEWqmVdpToiO/viweGcT0BjieHilDQ

It can be filtered by client, module/package name, or even version number. This is a key part of the process, as it will help us understand/find modules easier. 

**Use Case**: If there is a module that has an issue on a specific version, we can filter that module and version to see which clients have that module, and it will assist with the proactive module process to raise recommendations for issues that are visible to us.

If you are wanting to refer to Known Issues, refer to this document: [Known Issues](https://wiki2.zero1.co.uk/docs/main/dept-support/known-issues)

# Ticket Ownership/Process

1st Line Tickets

Keeping hold of tickets until you know there is a patch to be applied, then when its available you can get the junior dev on the project (Junior Dev) to implement the patches, same could be the case for all bugs (core and vendor extensions) so rather than just escalating, you retain control, keep comms up, liaise with vendor or keep checking for fixes, keep the client updated (canned responses whatever) until such time its ready for a dev to implement a patch.
This is a loose brain-dump of a new support process, the Support (juniors) keep the ticket for as long as possible rather than simply escalating it (to no-mans land) in these, the most common cases
1. vendor bug - chase up vendor for solution
2. core bug - find reported bug on magento github and keep client informed waiting for a patch or whatever
3. bug with our code - since these are almost never S1's (and clients are continually tricking us by declaring something a bug), its simply prioritised and scheduled.
1,2,3 above will soon be in the technical skills set for our Junior Support team to fully manage, tasks will ONLY then flow out to Engineering for 1 a patch to be implemented (junior dev) or 2 a development because ‘something’ needs to work differently (standard task)
S1’s are therefore the ONLY cases where proper planning goes out of the window.

# Replication Process

Replication Process for quick reference:
- Ensure you have clear replication steps before beginning the task (ask the client if necessary)
- If the client has one, try to replicate the issue on the TEST instance initially
- Once replicated, you can proceed to the [Investigation Process](#content-investigation-process)
- If you are unable to replicate, proceed to the [Unable to replicate](#content-unable-to-replicate) section


## Ticket Severities
<details>
  <summary>For more information regarding Ticket Severities...</summary><br>
Depending on the severity of the issue, you may need to replicate the issue in different locations.
  
### S1
The S1 process is as follows:
- Replicate (if possible) the issue on the prod/live site (**No instance is to be rolled up unless stated otherwise**)
- Once replicated, detail clearly as a comment, the replication steps within the task. If you have been unable to replicate, detail everything you've done to attempt the replication.
- Let Suz and 2nd line know you've replicated the issue in the respective slack channel and escalate to 2nd line (**unless the issue can be resolved only by a developer**)

**ENSURE THE CLIENT IS KEPT UPDATED THROUGHOUT THE REPLICATION!**

For example, if the task is "Site Down"
- Can you replicate on the Zero1 VPN?
- Can you replicate off the Zero1 VPN?
- Can you replicate on your phone/tablet?

### S2 & S3 
Ideally, you would first attempt to replicate on a TEST instance on MDOQ:
- If a client has no test instance, only then roll up an instance.
- If there is no instance space on MDOQ, check other instances to see if they are active first.
- If by this point you have checked that the instances are in use, ask Suz if you can roll on Crystal within the respective slack channel.
</details>

## Unable to replicate
<details>
  <summary>For more information regarding not being able to replicate...</summary><br>
It is very important that you replicate the issue before progressing with investigation OR escalation. Follow these steps as a last resort:

* Confirm you have all the information you think the client can offer - refer to [Canned Responses](#content-canned-responses) for assistance if needed.
* Ensure your instance has recent code/DB snapshots at least since the last release
* Test on live if it does not involve placing an order or MAP access
* Detail what you've done thus far and check TW to see if this issue has been reported before to assist replication
</details>
<br>

# Investigation Process

Investigation process for quick reference:
- Check logs on the development instance. Refer to [Log Investigation](#content-log-investigation) for more information
- Disable the theme in admin and ensure cache has been cleared. Refer to [Disabling the theme](#content-disabling-the-theme) for more information
- Disable ALL 3rd Party modules on the instance. Refer to [Disabling 3rd Party Modules](#content-disabling-3rd-party-modules) for more information

By this point, you should now have a root cause for the issue, from doing the steps above.

**DETAIL THE INVESTIGATION INTO THE COMMENT SECTION OF THE TASK - This makes it easier for 2nd/3rd line to pick up when the issue has been escalated**

## Log Investigation

<details>
<summary>For more information for investigating logs...</summary>

### Reviewing Logs in Var/Log
There are generally 2 crucial files in this location. These are **exception.log** and **system.log**. 

Exception.log will generally log the critical issues and system.log will generally log any application changes/issues, such as static deployment, etc. 

Bear in mind, that if there are other issues such as payment issues, some vendors may have put logs in their own folders within var/log, so be sure to check those as well

### Log Investigation Methods

Here are some methods for reviewing logs. They will provide the same outcome, but the options are here to make it as simple/easy for you as possible.

#### Via SSH
- Open the Web SSH container and run this command which will give you the file sizes: `cd htdocs/var/log && ls -lath`.
- Next, to view the last 5000 lines of a log file, run this: `tail -5000 ~/htdocs/var/log/exception.log` but change the log name respectively.

#### Via VS Code
- Go to your current instance. Click Support and then Visual Studio Code
- Once logged in, you need to go to Var/Log and then open exception.log and/or system.log.

#### Via MDOQ
- Download the code snapshot (good if the logs files are too large to load using the above methods) to your desktop (Live Connector > Tool Belt > Snapshots > Code Backup > Manage, then click the Download Icon on the latest one checking that you have a recent enough backup pertaining to the issue you are working on. Once downloaded, unpack it and review the files

#### Via Pimp My Logs
- Go to Support > Logs Viewer on your current instance. Credentials can be found under Settings > Helper Scripts

#### Searching the WIKI & Checking Online 
If you have noticed any errors from the logs, you can attempt to correlate them by searching the WIKi for previous references or searching online for instances of the issue:

- [Magento Known Issues](https://github.com/magento/magento2/issues)
- [Magento Stack Exchange](https://magento.stackexchange.com/)
- [Magento Community Forums](https://community.magento.com/)

</details>

### Cron Schedule
Some issues will occur due to Cron not working correctly/as intended. These steps will provide some insight into how to investigate cron issues:
- Go to the client’s TEST instance
- Click the Support tab
- Click on MySQL UI
- Run this SQL query: `SELECT * FROM cron_schedule;`
- This will filter all the records from the cron table, that have run, failed, or pending. This manages many areas of Magento, such as sending out emails, catalog price rules, and most things chronological to do with a store.
- **If the table is empty, this is an issue and needs to be escalated**


### Disabling 3rd Party Modules

<details>
<summary>For further information regarding disabling 3rd party modules process...</summary><br>
This process is designed to assist with disabling all 3rd party extensions are simply as possible. Adam found a way to disable all 3rd party modules, excluding modules prepended with `Magento_`:
- <br>Open up the SSH window and run this: 
  
 <br> `cd ~/htdocs && php bin/magento module:disable -- $(php bin/magento module:status --enabled | grep -v Magento_ | tr '\n' ' ')` <be>

<strong>N.B: Before you run the above command, copy the current config.php file and save it somewhere, so once you've finished with this process, you can restore the modules back to their initial states, which should line up with master</strong>

Need to speak to Adam/Callum about a git command to revert the config.php changes

#### Manually Disabling 3rd Party Modules
Sometimes disabling all 3rd party modules on a site will break it so disabling module manually by vendor will be a safer option.
1. Go into the code editor on your instance.
2. Go to app/etc/config.php.
3. Set modules from one vendor (anyone other than Magento) to "0" for example all Amasty modules.
4. Login into SSH. If you need to setup SSH refer to: [Setting up SSH](https://wiki.zero1.co.uk/docs/main/dept-operations/SSH)
5. Run `cd htdocs`
6. Run `bin/magento setup:upgrade`
7. Run `bin/magento deploy:mode:set developer`
8. Now you can test for whatever the issue was on the site. If the issue is fixed you'd have to go back to app/etc/config.php and start reenabling modules to see which one causes the issue. If the issue is not fixed, reenable the modules you disabled then disable the next set of vendor modules, then repeat steps 6 and 7 then retest the site. Continue doing this until the issue is fixed which will confirm which modules are causing the issue. If the issue is still present after disabling all the modules then the issue isn't caused by a 3rd party module, contiue on the next part of the first line process.
</details>

### Template Path Hints
<details>
<summary>For more information regarding template path hints... </summary>
<br>
Template Path Hints are commonly used to find specific files that may contain the cause of the issue.

You **MUST** make sure the instance is in developer mode before following these steps. This can be done by doing either of these options:
- SSH into the instance and enter this command: `cd htdocs && bin/magento deploy:mode:set developer`
-  Use the SAK Tool Belt on MDOQ by going to Actions > Deploy Mode and selecting Developer

Once it's in developer mode, follow these steps to enable them:

- Go into the admin of your instance and go to Stores > Configuration > Advanced > Developer > Debug. You should see "Enable Template Path Hints for Storefront".
- Change the scope from Default Config to the respective store view you are using
- Then, set "Enable Template Path Hints for Storefront" to Yes and flush cache

You could even enable Template Path Hints by SSH'ing into the instance and entering this command:

- `cd htdocs && bin/magento dev:template-hints:enable`

If you refresh your page on frontend, it should show up.


> If it doesn't show up after flushing browser cache, check if there is an IP in the "Allowed IPs" field in Developer Client Restrictions. If there's an IP in the field that IS NOT the office IP `"213.105.127.200"`, remove it and click Save Config



To disable them, set "Enable Template Path Hints for Storefront" to No or enter this command instead:

- `bin/magento dev:template-hints:disable && bin/magento cache:flush`

**Make sure cache is cleared/flushed before and after using Template Path Hints, otherwise it won't show up on frontend and/or disappear after use**

Here is the offical Magento documentation on Template Path Hints: https://docs.magento.com/user-guide/system/template-path-hints.html
</details>

### Disabling the Theme
<details>
  <summary>For more information regarding disabling the theme...</summary>
  <br>
To easily rule out if the theme is influencing the issue, you can disable the theme of your current instance:
- Go to admin and then go to Content > Design > Configuration
- Select the theme for the respective store level you are using
- Change it to Magento Luma and select Save Configuration
- Flush Caches and retest on frontend

If you have found that the issue isn't relevant to the theme, you can revert it back using the "Use Default Value" button next to the theme option. Make sure to flush caches after reverting it back as well.
</details>


### Switch PHP versions
Try switching the version of PHP - there are known issues with customisations or extensions of they are not officially supporting the version of PHP on production.


### Quick references for common SSH commands and config:set commands
<details>
  <summary>For more information regarding quick references for SSH commands...</summary>
When using Magento, you may come across some times where you need to enter SSH commands/SQL statements to find out more information about an issue. Here are some quick references:
- `tail -5000 ~/htdocs/var/log/system.log` - Allows you to quickly view system.log without waiting for the file to open. You can also swap system.log for any other log in the var/log folder
- `ls -lath` - This will tell the SSH to show you the files and their sizes within your current directory
- `bin/magento setup:upgrade --keep-generated` - Running this command will update all the modules on the instance, whilst keeping the static content, meaning you don't need to deploy static content
- `bin/magento config:set system/smtp/disable` - Setting the value to 0 disables the "Disable Email Communications" config in admin
- `bin/magento config:set twofactorauth/general/enable` - Setting the value to 0 disables TFA for that instance. **This MUST be re-enabled before committing config.php**
- `bin/magento config:set dev/debug/template_hints_storefront` - Setting this value to 1 will enable template path hints on the storefront. **You need to be in developer mode and flush cache for this to take effect**

More details about config:set references can be found here: https://devdocs.magento.com/guides/v2.4/config-guide/prod/config-reference-most.html
</details>

### Using the new IDE code editor
<details>
  <summary>For more information regarding using VS code on MDOQ...</summary>
  <br>
Sometimes, you may come across issues where it may require you to find files within the Magento application after using Template Path Hints to try and narrow down the source of an issue. Luckily, MDOQ now has an IDE code editor that can be used to find issues more clearly and in depth than Codiad can.

For example, you can use the code editor to find specific files and folders from using the terminal. This can be accessed from the burger menu lines at the top left of the IDE.

If you use this command: `grep -rli ""` , you can enter a keyword between the quotation marks, which will find any and all files associated with the keyword entered and is a great way to find files you need, quickly and efficiently
</details>

# Escalation Process

<p>
  Ensure your investigative findings have been noted in the comments before escalating to 2nd line
</p>
<p>These are the main steps depending on the cause:</p>
<ul>
  <li>
    Core Magento Bug -&nbsp; a Solution Specialist should review and advise
    of any potential workarounds.
  </li>
  <li>
    Theme Override -&nbsp; a Front-End Developer should review and fix
  </li>
  <li>
    3rd Party Extension - Initially, we need to check if the module is at its latest version. If not, contact the vendor regarding the issue and ask them to implement a fix as soon as possible.
  </li>
</ul>
Upon needing to escalate - Add "Escalated" tag to allocate a senior resource


___________

<!-- TITLE: 1st line Support -->
<!-- SUBTITLE: 1st line support process -->

<!-- > 	DISCUSSION POINT - we have to understand there are limitations to the number of intsances with MDOQ, therefore I would personally open up a debate on whether we reinstate this idea of having 1 TEST instance, which if always in-line with production (another process) then it should be available immediately as the primary instance to initiate the replication steps.

> Point of discussion - it is Arron's opinion that 1st line should always remain the communicators, frequently updating the client when certain time-frames have lasped Eg. No of days since last update or No of Hours billed since last update (probably both) along with a plan and message templates. Suzanne/Kel are tasked with gathering research on how other companies such a Amazon Seller Central respond to techinical tickets, they have generic canned responses. We could build templates and link them off this page. -->
