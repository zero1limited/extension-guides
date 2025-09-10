# iBottles.co.uk

[TOC]



## Payment
Stripe https://stripe.com/docs/testing

4000056655665556
123
Any Future Date

## Adding a category when testing an upgrade
When creating a new category on iBottles, it won't appear on the Mega Menu, due to their theme and overrides etc. Below, is what needs to be added/changed so it will show up for testing purposes:

1. Create a new category in admin (**Note down the ID of the category you've just made, as you'll need it shortly**)
2. Go to VS Code and go to this file: `app/design/frontend/Actuate/ibottles/Magento_Theme/templates/html/topmenu.phtml`
3. In this file, you will see a variable called `$topMenuArr=array` at the top of the file. Click just before the end bracket, add a comma and add your Category ID from earlier (Example: It should now look like this: `$topmenuarr=array(47,5,41,46,49,40,60,67)`
4. Once you've done that, scroll down a bit and you should see about 7 `$class[]` variables. After the 7th one, add this below it: `$class[]='level0 nav-7 level-top'`
5. Next, run these commands: `rm -rf generated && bin/magento c:f`. Your category should now appear on the Mega Menu
   (**N.B: Make sure the topmenu.phtml file does not get pushed**)

## Troubleshooting
Existing code stripped from store scope 1 `design_config/edit/scope/stores/scope_id/1/`
Footer Misc HTML
This was stripped back of the valcomp toggle and lpTag shit on Friday 14th May 20.00
```
<script>
    require([
        'jquery'
    ], function (
        jQuery
    ) {
        'use strict';
        jQuery.noConflict();
        jQuery(document).ready(function() {

            function toggleNav() {
                jQuery('#toggle').click(function() {
			        jQuery(this).toggleClass('active');
			        jQuery('#overlay').toggleClass('open');
                    jQuery('.nav-sections').toggleClass('mobile-menu-open');
		        });
            }

            toggleNav();

        })
    });
</script>

<style>
#toggle.active {top: -140px;}
</style>



<script type="text/javascript"> window.lpTag=window.lpTag||{};if(typeof window.lpTag._tagCount==='undefined'){window.lpTag={site:'31026783'||'',section:lpTag.section||'',autoStart:lpTag.autoStart===false?false:true,ovr:lpTag.ovr||{},_v:'1.5.1',_tagCount:1,protocol:location.protocol,events:{bind:function(app,ev,fn){lpTag.defer(function(){lpTag.events.bind(app,ev,fn);},0);},trigger:function(app,ev,json){lpTag.defer(function(){lpTag.events.trigger(app,ev,json);},1);}},defer:function(fn,fnType){if(fnType==0){this._defB=this._defB||[];this._defB.push(fn);}else if(fnType==1){this._defT=this._defT||[];this._defT.push(fn);}else{this._defL=this._defL||[];this._defL.push(fn);}},load:function(src,chr,id){var t=this;setTimeout(function(){t._load(src,chr,id);},0);},_load:function(src,chr,id){var url=src;if(!src){url=this.protocol+'//'+((this.ovr&&this.ovr.domain)?this.ovr.domain:'lptag.liveperson.net')+'/tag/tag.js?site='+this.site;}var s=document.createElement('script');s.setAttribute('charset',chr?chr:'UTF-8');if(id){s.setAttribute('id',id);}s.setAttribute('src',url);document.getElementsByTagName('head').item(0).appendChild(s);},init:function(){this._timing=this._timing||{};this._timing.start=(new Date()).getTime();var that=this;if(window.attachEvent){window.attachEvent('onload',function(){that._domReady('domReady');});}else{window.addEventListener('DOMContentLoaded',function(){that._domReady('contReady');},false);window.addEventListener('load',function(){that._domReady('domReady');},false);}if(typeof(window._lptStop)=='undefined'){this.load();}},start:function(){this.autoStart=true;},_domReady:function(n){if(!this.isDom){this.isDom=true;this.events.trigger('LPT','DOM_READY',{t:n});}this._timing[n]=(new Date()).getTime();},vars:lpTag.vars||[],dbs:lpTag.dbs||[],ctn:lpTag.ctn||[],sdes:lpTag.sdes||[],ev:lpTag.ev||[]};lpTag.init();}else{window.lpTag._tagCount+=1;} </script>

<!-- ZERO-1 -->
<script type="text/javascript">  
var activationdate = new Date("Mon Feb 1 2021 09:00:00 GMT+0000");
var now = new Date();
//console.log(now);
  //console.log(activationdate);

if (now > activationdate) {
  console.log('time');
 document.getElementById("valcomp").style.display = "block";
}
  else {
  console.log('not time yet');
}
</script>

```








## Data Link
Back Office system talks via Rest, to Get Orders and Update Stock.

Hi,

DataLink updates only product qty and stock status, not the product status
and we are updating m2 api stockItems endpoint :)

Best regards,
Anton Pluzhnikov, General Manager of DataLink
Holbi Group Ltd

tel : 02071933329, call center : 08000112569

Paradise Farm, High street
Kempsford
Fairford
GL7 4EU
Company No. 05622862


## Orderwise
This middleware is hosted on Heart Internet - https://customer.heartinternet.uk/manage/package_view.cgi/9e0af9d6c666e873/superuser
FTP is allowed only from the ZERO-1 Office IP

> You need to be on the Zero1 VPN for all this shizzle
{.is-warning}

There are some scripts sat on a server that call away to magento to import orders.
(don't know if this is via a cron or a webhook or what) but it is effectively a wrapper for Orderwise
as they don't have an api.

The scripts seem to handle multiple things, have only looked at orders so far.

### Debugging
There are daily log files in the `logs` which are written to each time the stuff runs.

#### Orders
From an initial dig looks like you can trigger the orders script with: https://orderwise.ibottles.uk/orders.php?store=1
It even looks like you can force an order with something like: https://orderwise.ibottles.uk/orders.php?store=1&order=INCREMENT_ID
> I haven't determined if the response is used by Orderwise, or if the response is just a copy of what has been sent to orderwise.

Some other shiny urls:
https://orderwise.ibottles.uk/generate_access_token.php?store=1
https://orderwise.ibottles.uk/settings.php

## Testing Orders BEFORE releasing changes

If you have changes which are likely to affect orders (Ie new payments or elements changing order information) then you can tag your changes and recreate TEST which is connected to Orderwise Staging. The below URL (accessibly only via the VPN) when replacing INCREMENT_ID with a real order on TEST, should push the order to Orderwise Staging and your contact at iBottles should be able to see this in their Orderwise application.


### Orderwise Staging
1. Make changes here https://github.com/zero1limited/ibottles-orderwise/tree/staging
2. SSH into the Heart Hosting Server and run
```
cd ~/public_html/orderwise-staging/
git pull
```

3. Test using - https://orderwise-staging.ibottles.uk/orders.php?store=99&order=INCREMENT_ID

You can also point to a different Magento instance by editing https://github.com/zero1limited/ibottles-orderwise/blob/96fe80f4dfc7d321aa9b10fd3fe4d812c6d100c5/class.magento.php#L77



In the FTP directory (below) there is a magento.class.php which has the credentials to access Magento, Orderwise pulls the orders when using this as an example URL https://orderwise-staging.ibottles.uk/orders.php?store=99&order=INCREMENT_ID

> For some reason Orderwises code references store 99, they set this up and I have no idea why, so we will keep with this.

### Credentials
**FTP Access**
Username: ibottles.uk
Password: y!r/HEnYK
FTP Server IP: 79.170.44.16

**Production**
FTP Folder public_html/orderwise
URL to the above: https://orderwise.ibottles.uk/
MySQL:
User: cl16-orderwise
Database: cl16-orderwise
Password: s2J.2/FMs

**Staging**
FTP Folder public_html/orderwise-staging
URL to the above: https://orderwise-staging.ibottles.uk/
MySQL:
User: cl16-owstaging
Database: cl16-owstaging
Password: g-!4xCskN

### Commercial Extensions
| Name | Version | Who purchased? | Login details for vendor |
|-|-|-|-|
Amasty_Acart |
Amasty_BannersLite |
Amasty_Base |
Amasty_Cart |
Amasty_Geoip |
Amasty_Conditions |
Amasty_CronScheduleList |
Amasty_CrossLinks |
Amasty_ElasticSearch |
Amasty_Xsearch |
Amasty_ElasticSearchMFTF3 |
Amasty_Feed |
Amasty_Gdpr |
Amasty_GdprCookie |
PayPal_Braintree |
Amasty_GoogleAddressAutocomplete |
Amasty_Mage24Fix |
Amasty_MegaMenu |
Amasty_MegaMenuGraphQl |
Amasty_Meta |
Amasty_Oaction |
Amasty_Paction |
Amasty_PageSpeedOptimizer |
Amasty_Promo |
Amasty_PromoBanners |
Amasty_Rewards |
Amasty_Rgrid |
Amasty_Rules |
Amasty_RulesLoyalty |
Amasty_RulesPro |
Amasty_SalesRuleWizard |
Amasty_SeoHtmlSitemap |
Amasty_SeoToolKit |
Amasty_SeoSingleUrl |
Amasty_SeoRichData |
Amasty_ShopbyBase |
Amasty_Shopby |
Amasty_ShopbyBrand |
Amasty_ShopbyPage |
Amasty_ShopbySeo |
Amasty_Smtp |
Amasty_XmlSitemap |
Amasty_ElasticSearchGraphQl |
Amasty_XsearchMFTF3 |
Amazon_Core |
Amazon_Login |
Amazon_Payment |
Custom_Banner |
Custom_Notifyme |
Dan0sz_ResourceHints |
Dotdigitalgroup_Email |
Dotdigitalgroup_Chat |
Dotdigitalgroup_ChatGraphQl |
Dotdigitalgroup_EmailGraphQl |
Dotdigitalgroup_Sms |
Holbi_ExtendREST |
Holbi_GetStockItemByID |
Klarna_Core |
Klarna_Ordermanagement |
Klarna_Kp |
Klarna_Onsitemessaging |
Klarna_KpGraphQl |
Lillik_PriceDecimal |
Mageplaza_Core |
Mageplaza_Smtp |
MarkShust_DisableTwoFactorAuth |
Mdoq_Connector |
OlegKoval_RegenerateUrlRewrites |
Amasty_Checkout |
PayPal_BraintreeGraphQl |
Staempfli_ImageResizer |
StripeIntegration_Payments |
Swissup_AddressFieldManager |
Swissup_Core |
Swissup_FieldManager |
Taxamo_Tax |
Temando_ShippingRemover |
Trustpilot_Reviews |
Ubertheme_Ubdatamigration |
Vertex_Tax |
Vertex_AddressValidationApi |
Vertex_RequestLoggingApi |
Vertex_RequestLogging |
Vertex_AddressValidation |
WebShopApps_MatrixRate |
Wyomind_Framework |
Wyomind_SimpleGoogleShopping |
Yotpo_Yotpo |
Zero1_Base |
Zero1_Csp |
Zero1_GDPR |
Zero1_Patches |
Zero1_ReleaseLibrary |
