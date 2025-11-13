# Instructions

<!-- 
[Module on GitHub](https://github.com/zero1limited/magento2-sub-category-listing)

[Module on Packagist](https://packagist.org/packages/zero1/module-sub-category-listing)

## Pitch Email

Almost all merchants have multiple category layers on their website, and most often it is more appropriate at higher levels to show visual subcategories as opposed to a singular product list. Presenting a sub category listing will help improve navigation and help your users find what they're looking for faster and more efficiently, while still keeping control in the user's hands (which is a key part of UX).

This task includes implementation of our custom code to achieve this since it is not a core Magento feature 
-->

Create an MDOQ dev instance for the relevant client
ssh onto the new instance

```
cd htdocs
```
```
composer config repositories.zero1-magento2 git "https://github.com/zero1limited/magento2-sub-category-listing"
```
```
composer require zero1/module-sub-category-listing
```
```
php bin/magento module:enable Zero1_SubCategoryListing
```
```
php bin/magento setup:upgrade
```
```
php bin/magento cache:flush
```

Go to your MDOQ instance and open the Github GUI
Git push, then select the following files...

```
composer.json
composer.lock
app/etc/config.php
```

After this is done, leave the instance where it is and please pass the task back to QA

# Q/A

- Go to MAP > Catalog > Categories
- Every category should now have the "Show Sub Category Listing" attribute set to Yes
- Find a category that has a few sub categories. Make sure the sub categories are enabled before continuing with testing
- Go to the frontend of the site and navigate to that category
- Make sure the sub category listing is displaying as expected
- Go back into the category in MAP and disable the "Show Sub Category Listing" attribute
- Go back to the frontend and check the sub category listing is no longer present (bare in mind caching when testing this step)

On completion, please pass the task back to the Zero1 owner
