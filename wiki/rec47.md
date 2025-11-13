<!--

# Pitch Email

Keeping your user experience looking fresh and current is key to retain interest and grow customer lifetime value. We have developed an extension which incorporates the ability to have self-managed New-In categories using ElasticSuite. This task requires Elasticsuite and Elasticsearch 7+ to be installed and functional, which we can implement as part of this task but may incur additional time.

What's required
> Elasticsearch 7.6
> Elasticsuite
> Magento 2.4.x

-->

# Instructions

```
cd ~/htdocs

composer config repositories.zero1-magento2-newin git "https://github.com/zero1limited/magento2-newin"

composer require zero1/magento2-newin
bin/magento module:enable Zero1_NewIn
bin/magento setup:upgrade
bin/magento cache:flush

```

# QA
Run the standard regression tests and check that the following manually

- FE - Categories look and work the same
- MAP - Manage Catalog - Categories appear functional

# Handover
At the point of 'Client Acceptance' move the task to 'Ready for Release' and pass to the task Manager
