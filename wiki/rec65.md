# Baldwin_UrlDataIntegrityChecker baldwin/magento2-module-url-data-integrity-checker Url data integrity checker module for Magento 2
[TOC]

## Pitch
From time to time it's possible for a number of your URLs to become malformed. This issue can cause increasing issues if left unresolved. We have a number of tools and processes to check, mitigate and advise of any work required. We would intend to raise this recommendation periodically at a frequency dependant on your size/turnover or potentially other marketing/diagnostic triggers.

**Frequency:** quarterly 

## Installation



### Check for Spaces
1. We propose you use TEST for this item since the module does NOT need to go live
2. Go to helpers and open "mysql console"
3. In the bottom right of the page where the tab is called "SQL Editor" paste in the following:
  ```sql
  select cpev.entity_id as id, 
    cpe.sku as sku, 
    cpev.store_id as store_id,
    cpev.value as url_key 
  from catalog_product_entity_varchar as cpev 
  left join catalog_product_entity as cpe 
    on cpe.entity_id = cpev.entity_id
  where cpev.attribute_id = (select attribute_id from eav_attribute where attribute_code = 'url_key' and entity_type_id = 4) 
  and cpev.value like '% %';
  ```

If 0 results are returned.
- update the ticket to say all product url_keys no not have spaces.

If any results are returned, install the module

```
composer require baldwin/magento2-module-url-data-integrity-checker
```

then run:

```
bin/magento setup:upgrade
bin/magento catalog:category:integrity:urlkey
bin/magento catalog:category:integrity:urlpath
bin/magento catalog:product:integrity:urlkey
bin/magento catalog:product:integrity:urlpath
```



- Navigate to "Data" > "Export Current Results..."
- Select "export as: csv"
- click export
- Upload csv to the ticket with the following message
> We have found the attached list of products that contain whitespace in the `url_key`. This can lead to ugly and un-optimized url paths for products.
For each product in the list we would recommend, you delete the current `url_key` and click save. Magento will then generate a more SEO friendly url.


