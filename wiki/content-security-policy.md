# Content Security Policy CSP implementation for Checkout

Moved to: https://zero1commerce.atlassian.net/wiki/spaces/IOW/pages/58556496/PCI+Compliance

## Pre Implementation
We will keep CSP at report only for admin, frontend and checkout. Install a module that allows the reports to be captured.
This can then be reviewed weekly, to see what needs to be added to CSPs whitelists.
As part of PCI DSS there should also be a reason why each script / resource is required, this method allows us to work through one at a time and generate the list.

1. Install plumbrocket csp. `plumrocket/module-csp-reports` free module, but needs to be purchased from their site.
2. Add MDOQ env updater to post roll up action (in `FINAL` step)
  ```bash
  # MDOQ CSP stuff
  curl -s https://raw.githubusercontent.com/MDOQ-UK/Templates/main/csp/env_updater.php | php -- '*.mysite1.com' '*.mysite2.co.uk'
  php bin/magento app:config:import
  ```
  **NB:** replace `mysite1.com mysite2.co.uk` with the root domains of the production site.
3. Configure the module
   ```bash
   php bin/magento config:set -c -- pr_csp/general/enabled 1 \
   && php bin/magento config:set -c -- pr_csp/main_settings/storefront_mode 1 \
   && php bin/magento config:set -c -- pr_csp/main_settings/admin_mode 1 \
   && php bin/magento config:set -c -- pr_csp/main_settings/erase_after 7
   ```
5. Test the MDOQ instance
6. From viewing the site I would expect to get a few reports, they can be viewed here: System > Tools | CSP Reports
7. Install DEG Report module `composer require degdigital/magento2-customreports`
8. Test everything and release
9. Go into MAP and confiure a report: Reports > Custom Reports | Custom Reports  
  Report Name: CSP Report  
  Report SQL: `select * from pr_csp_report`  
11. Then configure the report to be auto generated: Reports > Custom Reports | Automated Reports  
  Title: Export CSP Failures  
  Cron Expression: `0 3 * * *`  
  Reports To Export: CSP Report  
  Export Types: Email  
  Filename Pattern: `%reportname%-%Y%-%m%-%d%`  
  Export Location: `export/csp_reports`  
  Error Email Address: Your email address  
  Email Recipient(s): Your email addess and the clients if they want  
  
  
With this setup the client should have enough to pass a PCI audit, as we are being notified of failures.  
Stricter auditers may require enforced CSP for checkout, yet to be confirmed.
  


## Key Considerations when costing

* If we are on a simple setup (MDOQ/MIAMI) and know the payment provider is CSP-ready, we can implement with little effort
* If otherwise, we need to be careful managing expecations (Eg do the work & upgrade Hyva) then produce a manifest.


Key staff members - Callum

I think we should carry out the first couple BEFORE quoting to document and de-risk the work, keeping this document updated with risks etc.

Do we do any custom-CSP work for payment providers not yet CSP compatible? I say no.




### Finding "nonceless" scripts
Paste this in your browser console. Should give you the content of the scripts which you should able to find in the source
```js
document.querySelectorAll('script').forEach((e) => {
    if(!e.getAttribute('src') && !e.nonce && e.type != 'text/json' && e.type != 'application/json'){ 
        console.log('found script without nonce: '+e.type+' '+e.innerHTML)
    }
})
```

### Scripts in Ajax
It looks like any script load via ajax (including those via magewire), doesn't appear to work with the CSP helper method.
Didn't spend too long digging into why.

This is especially important for payment methods that use scripts once activate (ajax).

To find the scripts see 'Finding "nonceless" scripts', make sure you run this after the ajax as loaded.

I found the best way to handle this was to move the script to the bottom of the checkout page, then call it from the ajax content, this way the script can be "nonce'd".

Add to the checkout
`app/code/VENDOR/MODULE/view/frontend/layout/hyva_checkout_index_index.xml`
```xml
<?xml version="1.0"?>
<page xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="urn:magento:framework:View/Layout/etc/page_configuration.xsd">
    <body>
    <referenceContainer name="main">
        <referenceContainer name="hyva.checkout.api-v1.after">
            <block name="hyva.mollie.checkout-scripts" 
                template="Hyva_MolliePayment::page/scripts/applepay.phtml" 
                after="-" />
        </referenceContainer>
        </referenceContainer>
    </body>
</page>
```
**N.B** - the path the file is very important, hyva seem to have some logic that forces the template file to live under `page` when its in this container

Can then add your script in the template with the usual csp stuff `<?php $hyvaCsp->registerInlineScript() ?>`


### Migrating modules/templates
- use the csp helper
- manual
don't know of any other ways

#### Hyva CSP Helper
Hyva have made a helper util to help migrate stuff to CSP compliant.  
`composer exec hyva-csp-helper extensions/hyva/shipping-type-delivery`

```
## Running Hyva CSP helper on `hyva-themes/magento2-hyva-checkout-shipping-type-delivery`  
This will run several tools to optimize your code, find more about CSP  
Read our documentation for [theme](https://docs.hyva.io/hyva-themes/writing-code/csp/index.html) and [checkout](https://docs.hyva.io/checkout/hyva-checkout/devdocs/csp/index.html) changes

- @TODO! means **work todo**, please review
- @SKIPPED! means **work skipped**, please review
- @DONE! means **no work todo**, just informing about the change

### Updated requirements in composer.json
- requirement `hyva-themes/magento2-theme-module` (`^1.3.11`) @DONE!

### Register with $hyvaCsp

#### ./view/frontend/templates/checkout/section/watcher.phtml
- added `<?php $hyvaCsp->registerInlineScript() ?>` @DONE!
https://docs.hyva.io/hyva-themes/writing-code/csp/migration-tool.html#prerequisites
```
Gets you about 50-60% there and flags the bits you need to do

#### Making scripts/dom compatible

Two key bits with the CSP.

1. Scripts that stay the same.
```html
<script>
    var function() {
        products: [
            <?php foreach($products as $product): ?>
                '<?= $product->getName(); ?>'
            <?php endforeach; >
        ],
        hasProduct: function(name){
            return products.contains(name);
        }
    }
</script>
```
BAD - this means the script changes csp complains, hyva complains eveything complains. Need to make the dom the holder for changes

Better to do something like
```html
<?php foreach($products as $product): ?>
    <div data-role="product" data-product-name="<?= $product->getName(); ?>"></div>
<?php endforeach; >

<script>
    var function() {
        hasProduct(name){
            return null != document.querySelector('[data-role="product"][data-product-name="'+name+'"]')
        }
    }
</script>
<?php $hyvaCsp->registerInlineScript() ?>
```

This could be improved quite a bit, but the point that the script needs to stay static and load data either from the DOM or other resource remains.

2. Canny have functions in the dom
```html
<script>
    var myMethod = function(name){
        alert('you clicked: ' + name);
    }
</script>
<div onclick="myMethod('fooooo');">my div</div>
```
CSP won't allow this.
Data needs moving to dom attr then retrieved 

```html
<script>
    var myMethod = function(event){
        alert('you clicked: ' + event.target.dataset['name']);
    }
</script>
<div onclick="myMethod" data-name="fooooo">my div</div>
```
