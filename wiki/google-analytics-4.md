# Our approach for GA4 / GTM / Google Ads

[TOC]

## Google Ads Conversion Tracking
 *** SDS blueprint - need to document based on that.
 
We are using Yireo to push the customer data into Ads

Once live someone in Operations needs to run this on production
```
bin/magento config:set googletagmanager2/settings/customer_eav_attributes firstname,lastname,email
```
Or bake it into configuration
```
bin/magento config:set --lock-config googletagmanager2/settings/customer_eav_attributes firstname,lastname,email
```


## Key GA4 Reports

 - [SDS transaction list](https://analytics.google.com/analytics/web/?authuser=0#/analysis/p257705830/edit/6rmGjbSJTBmhP8jUxm6RfA)


## Enhanced Ecommerce Events
Most of the standard events are handled with the Yireo extension
We have implemented Customer Group Reporting for SDS - needs detailing

If we are using the GA4 conversion tag / Yireo / 
Max feels he can set this up with the relevant access to GTM/GA4/Ads



## Checkout Journey
https://github.com/yireo/Yireo_GoogleTagManager2/issues/188
https://github.com/yireo/Yireo_GoogleTagManager2/compare/master...hans-vereyken:Yireo_GoogleTagManager2:master

## Search Redirects - Better Landing Pages
First thing we need to do is segment search customers.

Create a Custom Dimension for search_term - see Divine Trash
Freeform - Create a Segment based on the session

Find a way for this search term to direct and inject like this https://github.com/zero1limited/magento2-Divinetrash/blob/master/patches/zero1_blp.patch


## Search Suggest
https://www.youtube.com/watch?v=AaCnaI_tqes

Event Parameters are key, that stores the search term
In order to view Parameters in reports, it must be a Custom Dimension, Ive just created the SDS one search_term



## Getting GA4 Data into Big Query
https://www.youtube.com/watch?v=9p8ujplFicw&list=PLlUxtxNX9ZEwKGxI-AZBuy7evLcOFM8VM&index=6
https://support.google.com/analytics/answer/9823238?hl=en#zippy=%2Cin-this-article
https://console.cloud.google.com/bigquery?project=client-test-projects&ws=!1m0
https://console.cloud.google.com/bigquery?project=client-test-projects&ws=!1m14!1m4!4m3!1sclient-test-projects!2sanalytics_337100244!3sevents_intraday_20231025!1m4!1m3!1sclient-test-projects!2sbquxjob_fac7fea_18b676cb9da!3sUS!1m3!3m2!1sclient-test-projects!2sanalytics_337100244

## Notices
need to research where we have this



## Notes

