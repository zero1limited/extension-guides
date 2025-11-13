# Instructions

<!--

## Pitch Email

Lazy Loading images is a technical concept to improve page load times. Images are loaded asynchronously meaning that images aren't loaded until they appear in the user's viewport.

This will reduce the 'Time to interactive' to the smallest time possible, particularly on mobile devices where the total page assets could be significantly larger than needed.

We have a trusted extension which can aid this and improve your overall performance metrics.

-->

Create an MDOQ dev instance for the relevant client
Until we have Composer 2 installed.... then

AT THE MOMENT, THESE EXTENSIONS WONT INSTALL

```
composer config repositories.module-webp2 git "https://github.com/landofcoder/module-magento-2-webp2"
composer config repositories.module-nextgen git "https://github.com/landofcoder/module-magento-2-next-gen-images"



composer require landofcoder/module-webp2:dev-master
```

Install the module via the MDOQ GUI by installing `landofcoder/module-webp2`




ssh onto the new instance then run the following commands...

```
cd htdocs
```


```
php bin/magento setup:upgrade
```
```
php bin/magento cache:flush
```
### Completion

Now the configuration and testing is finished, go to your MDOQ instance and open the Github GUI
Git push, then select the following files...

```
composer.json
composer.lock
app/etc/config.php
```

Once the push is successful, please leave the instance where it is and pass to QA

# QA
<!--
Follow the steps <a href="https://share.vidyard.com/watch/shYkZ6RGkHrRrayDJEUwmF?">in this video</a> to test the module.

> Note if the module isn't working as shown in the video, the client may already have image optimisation extensions installed which could conflict with this one. If that's the case, please pass to a FED to investigate further
{.is-warning}

Please also setup a standard automated regression test which will complete QA

# QA Screenshots

We now need some screenshots of the current site's performance before passing the task back. A really good screenshot tool is this Chrome Extension - [Go Full Page](https://chrome.google.com/webstore/detail/gofullpage-full-page-scre/fdpohaocaechififmbbbbbknoalclacl?hl=en) 

Please perform the following steps...

- Go the client's LIVE site (or sites if they're multi store like WOP) and grab the url(s)
- Go to [webpagetest.org](https://www.webpagetest.org/) and run a test for each site. **Make sure the test is running from London**
- Once the test(s) is/are complete, screenshot the page(s)
- Go to [tools.pingdom.com](https://tools.pingdom.com/) and run a test for each site. **Make sure the test is running from Europe**
- Once the test(s) is/are complete, screenshot the page(s)
- Go to [Page Speed Insights](https://developers.google.com/speed/pagespeed/insights/) and run a test for each site.
- Once the test(s) is/are complete, you'll see a `Mobile` tab and a `Desktop` tab near the top left of the page. Please screenshot both pages

Please attach all screenshots to the ticket in a private comment before passing the task back to the Zero1 owner
-->
# Zero1 Owner
<!--

- Demonstrate the features either as a live web conference or loom video.
  - Feature in action on PLP
  - Example of CMS Block implementation - adding MAGEFAN_LAZY_LOAD as per [guide](https://magefan.com/magento-2-image-lazy-load-extension/configuration)
-->
