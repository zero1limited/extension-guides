<!--

This recommendation is a set of activities aimed at spring-cleaning your product data and ensuring optimal performance for database, media and indexes. The acvitities include a set of tools to report and remedy the following:

• Report product data in default and store scope(s)
• Report store configuration in default and store scope(s)
• Report the use of attribute values and whether there are any which are not used
• Report on unused product images
• Implement cleanup of all the above based on the reports

Typically we have seen this save anything from 10-50% of the disk space used by your Magento application, but also provide marginal performance improvements particularly for larger inventories. Also depending on your backup agreement, this could mean greater retention of backups if you have limited backup storage.


-->

# Instructions
Install `hackathon/magento2-eavcleaner` and ensure activated by running the following via CLI

```
cd ~/htdocs
bin/magento eav:config:restore-use-default-value --dry-run
```
Once you have confirmed the above runs, please run the following commands and report ALL the outputs back as individual comments per command
```
bin/magento eav:config:restore-use-default-value --dry-run
```
```
bin/magento eav:attributes:restore-use-default-value --dry-run
```
```
bin/magento eav:attributes:remove-unused --dry-run
```


# QA
Run the standard regression tests





# Handover
Arron would run the report on the live site, report this to the customer. The confirm an appropriate time to run live.

https://github.com/magento-hackathon/EAVCleaner/tree/magento2
