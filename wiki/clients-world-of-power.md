# World of Power

[TOC]


## Discontinued Products
These are set with the discontinued attribute ID 1068 which is a Boolean attribute, a true value will cause the [PDP to hide Add-To-Cart via this code](https://github.com/zero1limited/magento2-WorldOfPower/blob/69d39298345ef4221179bfb92f5dbb6effed510f/app/design/frontend/z1/wp/Magento_Catalog/templates/product/view/type/default.phtml#L12)



## Back Office Integration

At present, WOP upload a file (`WOP_UPDATE_DATA.csv` / `WOP_DISPATCH_DATA.csv`) to a location on their network.
Something then pushes this file via SFTP to the middleware.
The person responsible for managing the upload to SFTP is Darren Astles, he can be contacted at: Darren.Astles@amita.co.uk

## Stock and Prices
When investigating issues regarding stock and price updates, you need to setup your FTP client using the SFTP credentials in this WIKI so that you can download/review the logs and import files.

Stock and prices are imported every 10 mins from `lumenstorage/csv_data/WOP_UPDATE_DATA.csv`

If the file has been accessed in the last 5 mins it will not be processed (this is to stop it being processed whilst it's being uploaded)
If the file file has not been accessed in the last 5 mins it will be moved to `storage/csv_data/WOP_UPDATE_DATA.in-progress.csv`
If the import fails the file will be moved to `storage/csv_data_backup/WOP_UPDATE_DATA_TIMESTAMP_error.csv`
If the import suceeds the file will be moved to `storage/csv_data_backup/WOP_UPDATE_DATA_TIMESTAMP.csv`


## Back Ordering 
More info in https://github.com/zero1limited/magento2-WorldOfPower/blob/master/knowledgehub/documents/linnworks.md

## Lead Times
There is a document here which explains this functionality https://github.com/zero1limited/magento2-WorldOfPower/blob/master/knowledgehub/documents/linnworks.md



## Magento Export Orders
This process runs at 59 minutes past every hour.

Outputs to two log locations:
- `export_orders`
- `scheduler`
  Example log output
```
[2021-03-29 10:50:14] export_orders.INFO: START EXPORT: 2000095737  
[2021-03-29 10:50:14] export_orders.INFO: HEADER WRITTEN: 2000095737  
[2021-03-29 10:50:14] export_orders.INFO: ORDER WRITTEN: 2000095737  
[2021-03-29 10:50:14] export_orders.INFO: FINISHED EXPORTING (will now set status): 2000095737  
...  
[2021-03-29 10:50:20] export_orders.INFO: START EXPORT: 2000095740  
[2021-03-29 10:50:20] export_orders.INFO: HEADER WRITTEN: 2000095740  
[2021-03-29 10:50:20] export_orders.INFO: ORDER WRITTEN: 2000095740  
[2021-03-29 10:50:20] export_orders.INFO: FINISHED EXPORTING (will now set status): 2000095740  
[2021-03-29 10:50:21] export_orders.INFO: STATUS SET: 2000095740  
[2021-03-29 10:50:21] export_orders.INFO: Copied: /var/www/html/storage/order_exports/order_export_20210329_105013.csv to: /var/www/html/storage/order_exports_archive/order_export_20210329_105013.csv result was: 1  
[2021-03-29 10:59:02] export_orders.INFO: Copied: /var/www/html/storage/order_exports/order_export_20210329_105901.csv to: /var/www/html/storage/order_exports_archive/order_export_20210329_105901.csv result was: 1  

```

Orders are deemed "ready for export" when:
- created in last 24 hours
- status is 'processing'

When an order has been succesfully exported:
- it's status is set to 'exported'
- the file will be exported to: `/var/www/html/storage/order_exports`
- the file will also be backed up to: `/var/www/html/storage/order_exports_archive`

If oders stop being exported, this is **unlikely** to be an issue with cron, because the scheduling responsibility is with the host server, not lumen. It's more likely:
- error in the code  (1st line can check the logs)
- container fallen over (needs 3rd line to confirm)

The newly created order export file that lives in `/var/www/html/storage/order_exports` will be picked up via SFTP and entered into WOPs back office, again this process is managed by Amita. The file will be deleted when processed.

If you go to this directory and there are still files in here (more than 1), this means they haven't been picked up via systems at Amita / WOP.
You chould check the SFTP connection works before contacting Amita, just to ensure it isn't a problem at our end.

The order exports happen at 59 mins past the hour, hourly. Then this file is picked up at 00 minutes (if I recall it actually gets picked up at something like 15 mins past, but I can't find this info anywhere).


#### TODO
- ~~Callum please spend 10 minutes writing a bit of info here on how orders get to WOP Back Office~~
- ~~Orders are exported to CSV when at Processing?~~
- ~~When orders are exported they are set to status 'exported'?~~
- ~~Magento cron manages the export process, this runs under job code xxxx and is scheduled every xx minutes.~~
- ~~If orders stop exporting this suggests cron is not running?~~

Orders stopped exporting for 2 hours [according to this ticket](https://zero1.teamwork.com/#/tasks/23526562) but I do not know where 1st line should start looking

#### SFTP
**Credentials**
- Host: `54.36.166.28`
- Port: `2222`
- Username: `sftpuser`
- Password: `Afzhn7np40X8Xz7782Zd`
  Old Passwords:
    - `823hg83n4g03wjnroirew` (< 2022-09-26)
    - `Spn82szZfdjxrpLE` (< 2022-08-11)

**Logs**
Logs appear to be located at: `/lumenstorage/logs/*`

#### Jobs
| Cron | Name | Description | More Info |
|:-:|:-:|:-:|:-:|
| `59 * * * *` | magento:export-orders | Pull orders from magento and puts them in a csv format | [more info](#magento-export-orders)|
| `5 8-20 * * *` | system:backup-csv-data | | This is now disabled and no longer runs |
| `*/10 * * * *` | csv:import-dispatches  |  | [more info](#import-dispatches) |
| `*/10 * * * *` | csv:update-stock-and-prices | | [more info](#stock-and-prices)|




## Updating SFTP password
Part of the PCI requirements is to change the SFTP password regularly.

The SFTP endpoint is for uploading/downloading order dispatches, price, stock import.

**Prerquisites**
- Before doing this we need to tell Daren (From Wops IT company) `Darren.Astles@amita.co.uk` and organise when he is happy for this to be done.
- MAP passwords have to have been reset


**How to update SFTP password**
- generate a new Magento password
- generate a new SFTP password
- SSH into Magento site and run
  `php bin/magento admin:user:create --admin-user=wopmiddleware --admin-password=[NEW MAGENTO PASSWORD] --admin-email=wopmiddleware@zero1.co.uk --admin-firstname=wop --admin-lastname=middleware`
  (replacing [NEW MAGENTO PASSWORD] with a newly generated password)
- SSH into bastion and then into `zero1_middleware`
- `sudo su`, `su wop`, `cd ~/worldofpower-middleware/`
- edit `.env` updating, `MAGENTO_PASSWORD` and `SFTP_PASSWORD`
- then run `docker-compose up --force-recreate --build --detach sftp`
  (ignore any error messages)
- test the sftp credentials
  Host: `sftp://54.36.166.28`
  Port: `2222`
  Username: `sftpuser`
- test the magento credentials.
  Find an order in the MAP
- then email big daz to let him know the new password


The logs for this process are at: `storage/logs/update-stock-and-prices-DATESTAMP.log`

## Import Despatches
Orders/shipments are imported every 10 mins `storage/csv_data/WOP_DISPATCH_DATA.csv`
(when using SFTP this is: `/home/sftpuser/lumenstorage/csv_data/WOP_DISPATCH_DATA.csv`).

The middleware looks for the file `storage/csv_data/WOP_DISPATCH_DATA.csv`
If the file has been accessed in the last 5 mins it will not be processed (this is to stop it being processed whilst it's being uploaded)
If the file file has not been accessed in the last 5 mins it will be moved to `storage/csv_data/WOP_DISPATCH_DATA.in-progress.csv`
If the import fails the file will be moved to `storage/csv_data/WOP_DISPATCH_DATA_TIMESTAMP_error.csv`
If the import suceeds the file will be moved to `storage/csv_data/WOP_DISPATCH_DATA_TIMESTAMP.csv`

The logs for this process are at: `storage/logs/import_dispatches-DATESTAMP.log`

## Stop copy-and-paste functionality

To stop the copy and paste ability on any CMS page on WOP, just add this line of code to the bottom of the page's HTML...

```
{{block class="Magento\Framework\View\Element\Template" template="Magento_Theme::copyandpastecontent.phtml"}}

```

> Please be sure to do this on a test instance before doing it in live. Thanks!
{.is-warning}
---

## Commercial Extensions
| Name | Version | Who purchased? | Login details for vendor |
|-|-|-|-|
Aheadworks_Ajaxcartpro |
Amasty_BannersLite |
Amasty_Base |
Amasty_Conditions |
Amasty_CommonTests |
Amasty_CommonRules |
Amasty_CronScheduleList |
Amasty_Customform |
Amasty_Faq |
Amasty_InvisibleCaptcha |
Amasty_Orderattr |
Amasty_Promo |
Amasty_Rgrid |
Amasty_SalesRuleWizard |
Amasty_ShippingArea |
Amasty_ShippingTableRates |
Amasty_Shiprestriction |
Amasty_Xnotif |
Amazon_Core |
Amazon_Login |
Amazon_Payment |
Ampersand_DisableStockReservation |
Bss_PreOrder |
Dotdigitalgroup_Email |
Dotdigitalgroup_Chat |
Dotdigitalgroup_ChatGraphQl |
Dotdigitalgroup_EmailGraphQl |
Dotdigitalgroup_Sms |
Ebizmarts_SagePaySuite |
FishPig_WordPress |
FishPig_WordPress_Multisite |
Klarna_Core |
Klarna_Ordermanagement |
Klarna_Kp |
Klarna_Onsitemessaging |
Klarna_KpGraphQl |
Klaviyo_Reclaim |
MageWorx_Downloads |
MageWorx_DownloadsImportExport |
MageWorx_Info |
MageWorx_SeoAll |
MageWorx_SeoMarkup |
Mageplaza_Core |
Mageplaza_Smtp |
MarkShust_DisableTwoFactorAuth |
Mdoq_Connector |
PCAPredict_Tag |
PayPal_Braintree |
PayPal_BraintreeGraphQl |
Smile_ElasticsuiteAdminNotification |
Smile_ElasticsuiteCore |
Smile_ElasticsuiteCatalog |
Smile_ElasticsuiteCatalogGraphQl |
Smile_ElasticsuiteCatalogRule |
Smile_ElasticsuiteCatalogOptimizer |
Smile_ElasticsuiteTracker |
Smile_ElasticsuiteThesaurus |
Smile_ElasticsuiteSwatches |
Smile_ElasticsuiteIndices |
Smile_ElasticsuiteAnalytics |
Smile_ElasticsuiteVirtualCategory |
Temando_ShippingRemover |
Trustpilot_Reviews |
Vertex_Tax |
Vertex_AddressValidationApi |
Vertex_RequestLoggingApi |
Vertex_RequestLogging |
Vertex_AddressValidation |
Wyomind_Framework |
Wyomind_SimpleGoogleShopping |
Yotpo_Yotpo |
Zero1_Base |
Zero1_ClientSetup |
Zero1_CountdownTimer |
Zero1_Csp |
Zero1_GDPR |
Zero1_GreatSuccess |
Zero1_Patches |
Zero1_ReleaseLibrary |
Zero1_ShortCategoryPaths |
Zero1_SubCategoryListing |
