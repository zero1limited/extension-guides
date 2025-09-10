# Tools Today

[TOC]



## Middleware
Toolstoday use a middleware created by Zero1 call Athena
Documentation on the functionality can be found [here](/clients/toolstoday/athena) << this is now OLD

Middleware integration is now done through a Magento module [Zero1_K8](/clients/toolstoday/zero1_k8)

## MDOQ
Instances use Elasticsearch `aaaa`



## QA

**Tools Today Sandbox Braintree Details**
Public key: 5rf9394gqsbxzk2w
Private key: ade4ace244eaf15135e6da2e950523fc
Merchant ID: 4j6xsm9fryj3q88m
Merchant Account ID: Tools_Today

**Login Details**
https://sandbox.braintreegateway.com/
ToolsToday / kQ%CB54Nhd

### Middleware
[Test case examples for Athena](https://docs.google.com/spreadsheets/d/1P_fOkAxpF-Q9Ndcq5qB9rNX97y6Y3OHR1FjrfPAXobU/edit#gid=0)

#### Escalation to 2nd line
Review production web logs Eg to investigate whether API calls are reaching the server for our test/example SKU
```
while [ True ]; do tail -n10000 /var/www/vhosts/toolstoday.co.uk/logs/nginx.443-access.log | grep 'Athena - production'; sleep 10; clear; done
```


```
94.46.150.31 - - [03/Feb/2021:21:54:20 +0000] "PUT /rest/V1/products/111262/stockItems/1 HTTP/1.1 "401 148 "-" "Magento 2 rest client (created by Zero1 https://www.zero1.co.uk)" "109.108.136.107, 94.46.153.227"[RT:0.037] [C:44791036]
```
#### 1st Line Process for Athena Stock Issues
1. Go to the web access section of the Athena wiki [here](https://wiki.zero1.co.uk/clients/toolstoday/athena#web-access) and use the credentials to login to the web interface.
2. Go to the update history section and search for a SKU of a product with stock issues.
3. Look at the filename column of the update table the search spits out and see what file you need to download (likely FULLSTOCK).
4. Go to the FTP client you use and use the details (use the k8ftpmaster account) from ftp access [here](https://wiki.zero1.co.uk/clients/toolstoday/athena#ftp-setup) to access the server.
5. Follow the file system Production>K8>Archive to find the file you require. Once you've found the correct file, download it.
6. Open the file and compare the data of the affected SKUs with the data in the update history section of Athena. If the csv is wrong Tom needs to fix it. If the web interface is wrong we need to fix it.
- **Extra:** To learn how Athena processes stock updates click [here](https://wiki.zero1.co.uk/en/clients/toolstoday/athena#how-product-updating-works)

## Application Stack
This client is hosted with UKFast



### Elasticsearch
```
{
  "name" : "HUkIDQF",
  "cluster_name" : "elasticsearch",
  "cluster_uuid" : "zLn6a4cwQTyEPmkkubM2hA",
  "version" : {
    "number" : "5.6.4",
    "build_hash" : "8bbedf5",
    "build_date" : "2017-10-31T18:55:38.105Z",
    "build_snapshot" : false,
    "lucene_version" : "6.6.1"
  },
  "tagline" : "You Know, for Search"
}
```

# Modules
## Zero1_SameDayDispatchText
This module allows an Admin configured html snippet to be shown for simple or grouped products on PDP and PLP pages when certain conditions are met.
![same_day_dispatch_module_plp_example.jpg](/clients/toolstoday/same_day_dispatch_module_plp_example.jpg)
![same_day_dispatch_module_simple_pdp_example.jpg](/clients/toolstoday/same_day_dispatch_module_simple_pdp_example.jpg)
![same_day_dispatch_module_grouped_pdp_example.jpg](/clients/toolstoday/same_day_dispatch_module_grouped_pdp_example.jpg)

### Settings
- **Custom Variable** "same_day_dispatch_days_of_week" - A comma seperated value listing the allowed days of the week the message can be displayed. The value must be stored under the variables "Plain Value" (Monday is 1)
- **Custom Variable** "same_day_dispatch_excluded_dates" - A comma seperated list of dates in the format `yyyy:mm:dd` that the message should not be shown on. The value must be stored under the variables "Plain Value"
- **Custom Variable** "same_day_dispatch_message" - The message/html to be displayed should the conditions be met. The message must be stored in the variables "HTML Value"

### Conditions
The message will be displayed if:
- The current day is in the list of allowed days
- The current date is not in the list of excluded data
- The product is in stock
- The product has a stock quantity > 0

### Extra
- **Original task** - https://zero1.teamwork.com/#/tasks/18683995


## Kerridge
All stuff about connecting to K8 backoffice system.

### Credentials
**K8**
Username: `zero1`
Password: `01Toolstoday**`

**K8 - Magento Access**
Username: `magento2`
Password: `xPpSBcEdiKfs5S5647qt05%MQ`

**VPN User (not working)**
Username: `User08`
Password: `CatHat22`

**Toms VPN User**
Username: `Tom`
Password: `network1`

#### Setting Up VPN Connection For K8

**Step 1 – Set Up VPN**
1. Go to https://www.draytek.com/products/smart-vpn-client/
2. Use the link to download latest version
3. When loaded up the app
4. Go to profiles
5. Connection type is PPTP
6. Add the IP address to connect is 92.207.210.229
7. Username is User08
8. Password is CatHat22

**Step 2 – Set Up Static Route to Connect to K8**
You need then to add a static route to the laptop or PC for K8 connection.
For that you have to run Command Prompt with admin privileges, then run the following command.
```
Route -p ADD 10.50.12.144 MASK 255.255.255.240 192.168.100.1
```

**Step 3 - Access K8**
download this file: [v21_prod.kcc](/clients/toolstoday/v21_prod.kcc)
then double click to open (which should launch the k8 client)

## Commercial Extensions
| Name | Version | Who purchased? | Login details for vendor |
|-|-|-|-|
Amasty_AdvancedReview |
Amasty_BannersLite |
Amasty_Base |
Amasty_Conditions |
Amasty_CommonTests |
Amasty_CommonRules |
Amasty_CronScheduleList |
Amasty_Customform |
Amasty_FreeGiftLite |
Amasty_LazyLoad |
Amasty_LazyLoadUi |
Amasty_Ogrid |
Amasty_PageSpeedOptimizer |
Amasty_PageSpeedTools |
Amasty_ProductAttachment |
Amasty_Preorder |
Amasty_PreorderMFTF2 |
Amasty_PreorderMFTF3 |
Amasty_Pgrid |
Amasty_ProductAttachmentLite |
Amasty_Promo |
Amasty_PromoMFTF2 |
Amasty_PromoMFTF3 |
Amasty_Rgrid |
Amasty_SalesRuleWizard |
Amasty_ShippingArea |
Amasty_ShippingTableRates |
Amasty_Shiprestriction |
Amasty_Sorting |
Amazon_Core |
Amazon_Login |
Amazon_Payment |
Ampersand_DisableStockReservation |
Bss_ProductQuestions |
Bss_ProductQuestionsFixBug |
Dan0sz_ResourceHints |
Dotdigitalgroup_Email |
Dotdigitalgroup_Chat |
Dotdigitalgroup_ChatGraphQl |
Dotdigitalgroup_EmailGraphQl |
Dotdigitalgroup_Sms |
Ebizmarts_MailChimp |
Experius_WysiwygDownloads |
Fooman_GoogleAnalyticsPlus |
Hackathon_EAVCleaner |
ImageKit_ImageKitMagento |
Klarna_Core |
Klarna_Ordermanagement |
Klarna_Kp |
Klarna_Onsitemessaging |
Klarna_KpGraphQl |
MageArray_StorePickup |
MageWorx_SeoAll |
MageWorx_Info |
MageWorx_HtmlSitemap |
MageWorx_SeoBase |
MageWorx_SeoBreadcrumbs |
MageWorx_SeoCategoryGrid |
MageWorx_SeoCrossLinks |
MageWorx_SeoExtended |
MageWorx_SeoMarkup |
MageWorx_SeoRedirects |
MageWorx_SeoReports |
MageWorx_SeoUrls |
MageWorx_SeoXTemplates |
MageWorx_XmlSitemap |
Mageplaza_Core |
Mageplaza_Smtp |
Mageplaza_Webhook |
Mdoq_Connector |
PayPal_Braintree |
PayPal_BraintreeGraphQl |
Smile_ElasticsuiteAdminNotification |
Smile_ElasticsuiteCore |
Smile_ElasticsuiteCatalog |
Smile_ElasticsuiteCatalogGraphQl |
Smile_ElasticsuiteCatalogRule |
Smile_ElasticsuiteCatalogOptimizer |
Smile_ElasticsuiteCms |
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
Zero1_AnnotateUpSells |
Zero1_Base |
Zero1_BulkImportWebhooks |
Zero1_CrosssellOnPdp |
Zero1_Csp |
Zero1_GDPR |
Zero1_K8 |
Zero1_MailLogFixer |
Zero1_Patches |
Zero1_ProductFeatureImages |
Zero1_Release |
Zero1_ReleaseLibrary |
Zero1_RunCronJob |
Zero1_SameDayDispatchText |
Zero1_ShippingFix |
