# Klaviyo

[TOC]

## Setup
Setup instructions were taken from [klaviyos blog](https://help.klaviyo.com/hc/en-us/articles/115000357752)

1. When setting up we need to select "dynamic" and to send emails from the send. domain
  ![setup Picture](/img/media/dept-marketing/klaviyo/setup.png)
2. The following DNS records then need adding
  
  | Host | Value | Record Type |
  | - | - | - |
  | send.helloworld.com | ns1.klaviyo.com | NS |
  | send.helloworld.com | ns2.klaviyo.com | NS |
  | send.helloworld.com | ns3.klaviyo.com | NS |
  | send.helloworld.com | ns4.klaviyo.com | NS |
  | helloworld.com | klaviyo-site-verification=public_API_key | TXT |


### Integration failure issue 
we see a common setup issue where Klayiyo insist on connecting to a URL with index.php 
Eg https://staging.5adaybox.co.uk/index.php/rest/V1/customerGroups/search?searchCriteria%5B[…]iteria%5BcurrentPage%5D=1&searchCriteria%5BpageSize%5D=50

The avove gives a 404
SOLUTION: Create a Rule : Redirect Rule in Cloudflare with example below

Request URL: https://staging.5adaybox.co.uk/index.php/rest/*
Target URL: https://staging.5adaybox.co.uk/rest/${1}
Check Preserve query string




## Custom Data / SFTP
This has a POC on SDS London
Estimation for the initial setup is 1 day
Then subsequent estimations required based on the data which needs mining

Setup required
 - SFTP setup https://developers.klaviyo.com/en/docs/use_klaviyos_sftp_import_tool
 - Custom Reporting - `composer require degdigital/magento2-customreports`
 - Setup FTP keys here https://www.klaviyo.com/sftp/set-up then add the private key to source control
 - Magento Cron Setup

### Example Cron Job
```
LOG=~/htdocs/var/log/klav.log && date >> $LOG && sftp -i ~/htdocs/klav-sdslondon VqWrjT_XYrSfu@sftp.klaviyo.com <<< $'put /home/magento/htdocs/var/export/custom_report_exports/YesterdaysTradeCustomers.csv /profiles'  >> $LOG
```


## Hyvä Compatibility

```
composer require hyva-themes/magento2-klaviyo-reclaim
```

To validate the above is working look for `initKlaviyoCustomerTracking` in the source code on a product detail page once the above is installed.


## Custom Data via Javascript API
This could be an easy way to push additional data to Klaviyo, example being it might only need us to load that data onto the page for the client so this could be a front-end template override?
https://developers.klaviyo.com/en/docs/javascript_api
