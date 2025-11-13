# Zero 1 Hot Tags

 [TOC]

[Module on GitHub](https://github.com/zero1limited/magento2-hot-tags)

[Module on Packagist](https://packagist.org/packages/zero1/module-hot-tags)

## Pitch Email

Increasing visibility of popular and in-demand products on your site is a great way to help increase higher CTR and conversion rates. One way to do this is to add a message (Hot Tag) on the product details page which shows exactly how popular and in-demand your products are based on the actions of your users. 

Shoppers tend to have FOMO (Fear Of Missing Out) and they don't want to miss out on something that seems popular. If messages on a site suggest a product is in high demand — "Trending Now! Added to basket 100 times today" - customers can often make impulse buys and also justify their purchase based on the popularity of that product.

Including this messaging on your site will gain the benefits mentioned above along with the following features:

- Choose between 'Added to basket' or 'Viewed' as your trigger
- Choose your timescale; e.g. 'in the last hour', 'today'
- Fully customisable text
- Choose the minimum number of actions / triggers before showing the tag
- Customise the styling of the tag


## Instructions

Create an MDOQ dev instance for the relevant client
ssh onto the new instance then run the following commands...

```
cd htdocs
```
```
composer config repositories.zero1-magento2 git "https://github.com/zero1limited/magento2-hot-tags"
```
```
composer require zero1/module-hot-tags
```
```
php bin/magento module:enable Zero1_HotTags
```
```
php bin/magento setup:upgrade
```
```
php bin/magento cache:flush
```

### Completion

Go to your MDOQ instance and open the Github GUI
Git push, then select the following files...

```
composer.json
composer.lock
app/etc/config.php
```

Once the push is successful, please leave the instance where it is and pass to QA

# QA

This module shows a message on the frontend that displays how many times people have viewed products and how many times people have added products to their basket. This data comes from Magento's reporting system; therefore, Reports MUST be enabled in order for this feature to work. 

First thing we need to do is check whether reporting is enabled on your instance because this will determine whether the data shows on the frontend or not...

## Check Report status

- Go into MAP > Stores > Configuration > General > Reports | General Options
- Check if Enable Reports = Yes
- Check if "Enable Product View Report" and "Enable Product Added To Cart Report" are = Yes

If reports are **DISABLED**, please enable the reports mentioned above, then continue to the next step "Setup Regression Test"
If reports are **ENABLED** (product view and product added reports MUST be enabled too), skip past "Setup Regression Test" and continue to "Finding Products"

## Setup Regression Test

- Run the following commands on the instance to enable reporting before setting up the regression test

```
bin/magento config:set reports/options/enabled 1
bin/magento config:set reports/options/product_view_enabled 1
bin/magento config:set reports/options/product_to_cart_enabled 1
```

- Setup & Run a Regression Test
Now that reporting is enabled, we need to generate some data in the reports using regression tests. 

QA can create a regression test that will view / add specific products every 5 mins to then start putting data in Magento's reporting system.
Please contact Criag as he made a base template GI test here - https://app.ghostinspector.com/tests/60bf4b50c72ce60533765598

Let the regression test run for as long as needed to gather the relevant information

## Finding Products

Now that we have data in the reports, we need to get to that data to see which products we should be testing with. We need 1 product for "Most Viewed" and 1 product for "Most Added"...

### Finding suitable products

One easy way to do this is to go into MAP > Dashboard and in the summary, there'll be a "Best Sellers" and "Most Viewed" section. Grab a SKU from each of those; these are your "Most Viewed" and "Most Added"

### Get the product's IDs

Now we need to get the IDs of those products which you can do by...

- MAP > Catalog > Products
- Filter by the SKU you've just got
- The ID will show on the left

## Get the product data

Now we've got the relevant IDs of the products and we know they're the most viewed / most added, we need to query the data from the database

- Open your MDOQ instance and go to Support > MySQL Console
- When this loads you'll see the SQL Editor at the bottom. This is where we'll be getting the data

Before running any of the commands below, please just take a mental note of the object_id ```object_id=12345``` and also the interval ```INTERVAL 1 HOUR```

> Make sure you replace 12345 with the ID of the product you're testing. If your product ID is 10932, then...
> ```object_id=12345``` becomes ```object_id=10932```
{.is-danger}

When copying these commands, just whack em in the "SQL Editor" then click "Query" to run them.

Be sure to take notes of how many results you get on each of the commands being run

### Get the Most Viewed Data

Returns the amount of time the product has been viewed in the **last hour**
```
select * FROM report_event WHERE event_type_id = (select event_type_id from report_event_types WHERE event_name='catalog_product_view') AND object_id=12345 and store_id=1 AND logged_at > (CURDATE() - INTERVAL 1 HOUR);
```


Returns the amount of time the product has been viewed in the **last day**
```
select * FROM report_event WHERE event_type_id = (select event_type_id from report_event_types WHERE event_name='catalog_product_view') AND object_id=12345 and store_id=1 AND logged_at > (CURDATE() - INTERVAL 1 DAY);
```

Returns the amount of time the product has been viewed in the **last week**
```
select * FROM report_event WHERE event_type_id = (select event_type_id from report_event_types WHERE event_name='catalog_product_view') AND object_id=12345 and store_id=1 AND logged_at > (CURDATE() - INTERVAL 1 WEEK);
```

### Get the Most Added Data

Returns the amount of time the product has been viewed in the **last hour**
```
select * FROM report_event WHERE event_type_id = (select event_type_id from report_event_types WHERE event_name='checkout_cart_add_product') AND object_id=12345 and store_id=1 AND logged_at > (CURDATE() - INTERVAL 1 HOUR);
```


Returns the amount of time the product has been viewed in the **last day**
```
select * FROM report_event WHERE event_type_id = (select event_type_id from report_event_types WHERE event_name='checkout_cart_add_product') AND object_id=12345 and store_id=1 AND logged_at > (CURDATE() - INTERVAL 1 DAY);
```

Returns the amount of time the product has been viewed in the **last week**
```
select * FROM report_event WHERE event_type_id = (select event_type_id from report_event_types WHERE event_name='checkout_cart_add_product') AND object_id=12345 and store_id=1 AND logged_at > (CURDATE() - INTERVAL 1 WEEK);
```

## Test the Frontend

Now that we know how many times a certain product has been viewed / added, we can test the module.

### Most Added

- Go to MAP > Stores > Configuration > Zero1 > Hot Tags > Frontend Experience Settings
- Check that the trigger is set to Add To Basket. 
- Take note of what the Trigger Timescale is. This can be either last hour, day, or week. This is obviously relative to the number you've got from running thos SQL commands...
- Go to the frontend of your instance and find your "Most Added" product

**Check:** The number that you got from your SQL query should match the qty message on the frontend of the instance

- Change your Trigger Timescale to a different option
- Flush cache
- Revisit the product on the frontend in a new porn window and cross reference numbers shown to the ones from your SQL queries

Do this for ALL Trigger Timescale options

### Most Viewed

Do exactly as above, but just make sure the Trigger in MAP is set to "Viewed"

## Completion

Once QA is complete, please pass the ticket back to the Zero1 Owner and please also note down the number of SQL results you got for each of the queries and whether this matches up to the frontend. Thanks!

# Zero1 Owner

Check if reporting is on or off on live and explain this will cause the module to not have any data in it for a while until the reports start gathering data.

Demonstrate the module in action to the client on their site and ask if they require any styling which can be carried out in the module's configuration.

# Config As Code
```
bin/magento config:set hottags/general/active 1
bin/magento config:set hottags/frontend/trigger "viewed"
bin/magento config:set hottags/frontend/triggertext "Added to basket "
bin/magento config:set hottags/frontend/triggertimescale "today"
bin/magento config:set hottags/frontend/triggertimescaletext " today"
bin/magento config:set hottags/frontend/tag_text "%amount% people are viewing this right now"
bin/magento config:set hottags/frontend/show_tag_pre_text 1
bin/magento config:set hottags/frontend/tag_pre_text "Trending Now!"
bin/magento config:set hottags/frontend/minimum_triggers "10"
bin/magento config:set hottags/frontend/show_tag_after "2000"
bin/magento config:set hottags/design/background_colour "gold"
bin/magento config:set hottags/design/text_colour "#000"
bin/magento config:set hottags/design/border_colour "gold"
```
