# DNS Prefetch & Preload Optimisation

## Pitch
For Performance optimisation of your site it is recommended that you use some more complex techniques to preload website assets in a more effective manner. This is referred to as Preloading or Prefetching and is referred to by Google in their Lighthouse documentation https://developers.google.com/web/updates/2018/05/lighthouse#preload_key_requests

This is known to improve the performance metrics score in Google Lighthouse

We will install, configure, test and deploy a custom Magento extension which adds these features to your production site and also provides the ability for the configuration to be changed in future if your website uses assets from other 3rd party domains. 




## Instructions
Once you have your MDOQ instance ready....

1. Using the Module Install feature via Toolbelt, install `dan0sz/resource-hints-magento2`
2. Go to Google Chrome, open your Developer Tools then the Lighthouse tab then with only the Performance category selected click 'Generate report'. This will provide you with some suggestions to preload or prefetch, possibly under Opportunities titled 'Preconnect to required origins'. Make a note of the URLs reported.
3. Login to Magento Admin and configure the module via 'Stores > Configuration > General > Web > Resource Hints'. There is an example below.

4. Once the module has finished installation, you can carry out regression testing on the site. The features cannot be tested until the extension is live. Please ensure this task is assigned to Arron once a deployment has taken place.


> Please note, your objective here is not to successfully configure the extension, but just to install it and ensure there are no regression issues. Due to the complex nature of the configuration this has to be configured in production by a qualified Magento Solution Specialist
{.is-warning}



<!--

## Arrons Notes
https://developers.google.com/web/updates/2018/05/lighthouse#preload_key_requests

bash
m2db_host=$(php -r '$env = include "./app/etc/env.php"; echo $env["db"]["connection"]["default"]["host"].PHP_EOL;');\
m2db_user=$(php -r '$env = include "./app/etc/env.php"; echo $env["db"]["connection"]["default"]["username"].PHP_EOL;');\
m2db_password=$(php -r '$env = include "./app/etc/env.php"; echo $env["db"]["connection"]["default"]["password"].PHP_EOL;');\
m2db_database=$(php -r '$env = include "./app/etc/env.php"; echo $env["db"]["connection"]["default"]["dbname"].PHP_EOL;');\
echo "USE ${m2db_database}; select CONCAT('bin/magento config:set --lock-config ',path,' ',value) as command FROM core_config_data WHERE value !='' AND path NOT LIKE '%system_value%' AND updated_at > DATE_SUB(NOW(),INTERVAL 1 HOUR);" | mysql -h ${m2db_host} -u ${m2db_user} -p${m2db_password};
```
