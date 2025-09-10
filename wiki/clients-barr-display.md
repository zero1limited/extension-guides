# Barr Display

[TOC]

## Overview

## Brightpearl

Investigating issues with orders being sent to Brightpearl.

 - Search the export logs here https://www.barrdisplay.com/admin_1tgnbo/hotlink_framework/log/ entering the order number into the reference. If the log detail loads nothing, get the ID, then you need to go to MDOQ and download a code backup from the morning AFTER the issue. Once downloaded, unpack and navigate into var/log/hotlink_framework/report/ and you should find report log files matching the ID, review these.
 - 



## Shipper HQ
Functionally, the app/code module would create a table to log errors in (`shipperhq_error`), which would log some core information, such as
the quote that it was associated with (`quote_id`), as well as some error message and the request (encoded json). This was turned off
[here by Arron on Dec 24, 2024](https://github.com/zero1limited/magento2-BarrDisplay/commit/87a92acedc111a881149384d8d61f69f3fd7ee77).
[Task](https://zero1.teamwork.com/tasks/38631411?c=14940316) . The reason it was turned off was because there are some instance where a bool
or Error value can be passed into the plugin that applies the db logging, and this was no accounted for in the original development.

It should be a simple case of adding the other types to the afterCollectRates plugin in `Plugin/ShipperHq/Shipper/Model/CarrierPlugin.php`,
and handle them accordingly. It would require a review of instances where Error or boolean being passed in occure, so as to not add false negatives
to the DB, as these are used to flag up any problematic orders.

There is an alternative module ([Zero1_ShippingErrorLogging](https://github.com/zero1limited/magento2-shipping-error-logging)) that is designed
to do a similar thing, but I (Brad) cannot figure out exactly how far into development this went and how functional it was. This was designed to
be a generic module that was agnostic to the actual shipping provider, and would just do it on all.

```sql
SELECT quote.*, shipperhq_error.*
FROM shipperhq_error, quote
WHERE quote.entity_id=shipperhq_error.quote_id AND TIMESTAMPDIFF(MINUTE, logged_date, CURRENT_TIMESTAMP) < 200;
```

## Commercial Extensions
| Name | Version | Who purchased? | Login details for vendor |
|-|-|-|-|
Amasty_Base |
Amasty_OAction |
Amasty_OrderAttributesSubscriptionPackage |
Amasty_Orderattr |
Amasty_OrderattrHyvaCompatibility |
Amazon_Core |
Amazon_Login |
Amazon_Payment |
Baldwin_UrlDataIntegrityChecker |
Bss_CustomProductAttributeExport |
ClassLlama_AvaTax |
Commerceshop_Shipping |
Commerceshop_Stampstore |
Dotdigitalgroup_Email |
Dotdigitalgroup_Chat |
Dotdigitalgroup_Sms |
Ebizmarts_MailChimp |
Fooman_PdfCore |
Fooman_PdfDesign |
Fooman_PdfOrderPdf |
Fooman_PdfCustomiser |
Hotlink_Framework |
Hotlink_Brightpearl |
Hyva_CompatModuleFallback |
Hyva_Email |
Hyva_GraphqlTokens |
Hyva_GraphqlViewModel |
Hyva_ThemeFallback |
Hyva_Theme |
Hyva_LumaCheckout |
Klarna_Core |
Klarna_Ordermanagement |
Klarna_Kp |
Klarna_Onsitemessaging |
Klarna_KpGraphQl |
MagePal_Core |
MagePal_CatalogLazyLoad |
Magefan_AdminUserGuide |
Magefan_Community |
Magefan_Blog |
Magefan_BlogGraphQl |
Magefan_LazyLoad |
Magefan_WysiwygAdvanced |
Mageplaza_Core |
Mageplaza_BannerSlider |
Mageplaza_AjaxLayer |
Mango_Loworderfee |
MarkShust_DisableTwoFactorAuth |
Mdoq_Connector |
PayPal_Braintree |
PayPal_BraintreeGraphQl |
Rootways_Authorizecim |
Scrumwheel_ImportExport |
ShipperHQ_Common |
ShipperHQ_Logger |
ShipperHQ_Shipper |
ShipperHQ_Option |
Smartwave_Core |
Smartwave_Dailydeals |
Smartwave_Filterproducts |
Smartwave_Megamenu |
Smartwave_Porto |
Smartwave_Socialfeeds |
Temando_ShippingRemover |
Vertex_Tax |
Vertex_AddressValidationApi |
Vertex_AddressValidation |
Wyomind_ElasticsearchCore |
Wyomind_QuickOrder |
Wyomind_SimpleGoogleShopping |
Yotpo_Yotpo |
Zero1_Accessorials |
Zero1_Base |
Zero1_CronDoctor |
Zero1_Csp |
Zero1_EnhancedConversionTracking |
Zero1_Ga4Gtm |
Zero1_Patches |
Zero1_Release |
Zero1_ReleaseLibrary |
Zero1_RunCronJob |
Zero1_ShippingTermsAndConditions |
Zero1_StreetValidator |
Zero1_SubCategoryListing |
