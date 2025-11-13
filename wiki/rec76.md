## Aplicabality
This recommendation is applicable for all M2 sites.

## Pitch
Performing an audit to maintain a safe Magento admin, as well as provide some useful insight into other areas.

What are the benefits?
- improved security
- insights into inefficient configuration


Further Explanation:
Over time settings in Magento get changed and forgotten, categories get created and not filled products, users get created and not deleted etc...
This task will audit these a more and give you a report on any issues found and recommendations on how to proceed, this allows you to establish a baseline for you site making sure your production environment never falls below a certain standard.


## Process
### Who
Anyone with access to MDOQ

### Setup
This task requires a recent backup (within the last 24 hours). 
Ideally using test for the client, which may just involve recreating the DB.

### Instructions
Please work through all checks below, updating the report with any info detailed in each check.

#### SEO
##### URL Key Check
1. Go to helpers and open "mysql console"
2. In the bottom right of the page where the tab is called "SQL Editor" paste in the following:
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
- Update the report, mark this check as passed

If any results are rturned
- (within the mysql console) Navigate to "Data" > "Export Current Results..."
- Select "export as: csv"
- click export
- Name the file "unfriendly_seo_url_keys.csv"
- Upload csv to the ticket
- Within the report, mark this check as failed
- Within the report, add this to additional info
> We have found the attached list of products that contain whitespace in the `url_key`. This can lead to ugly and un-optimized url paths for products.
For each product in the list we would recommend, you delete the current `url_key` and click save. Magento will then generate a more SEO friendly url.
A list of the effected products is attached (unfriendly_seo_url_keys.csv)


## Handling Accepted Recommendations
**Please hand the task to the recommendation owner**
