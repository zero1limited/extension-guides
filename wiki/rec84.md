# Pitch
Your We have a new emerging technology setup which is showing great results for web performance around media assets. 

Currently this work package appears to remove/resolve all advisories around image optimisation for Web Vitals provided you are using best practice and storing all media images on the same server.
 
Using ImageKit.io CDN service we can get your Magento 2 store to deliver image to customers using the latest compression technologies including webP format, all handled at the edge and working as part of the CDN service.

This task includes the following only for 1 website/domain:

- imagekit.io account setup, storage & origin
- Magento 2 extension install & config
- QA on non-production site
- Live DNS amendments

Additional stores/domains can be incorporated within this task for an estimated 4 hours per store.

# Instructions
```
composer require imagekit/imagekit-magento
php bin/magento maintenance:enable
php bin/magento setup:upgrade
php bin/magento setup:di:compile
php bin/magento setup:static-content:deploy
php bin/magento maintenance:disable
php bin/magento cache:flush
```
