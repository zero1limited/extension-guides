# Abakhan





[TOC]

## Introduction

# Overview
Abakhan are now on M2 with a Hyva theme

## Emails

Emails are transported out via Mageplaza SMTP then onto https://mandrillapp.com/.

## Downloadable Products

We implemented some changes on Abakhan for their downloadable products. This should help understand how this works and hopefully help debug any issues that might crop up...

### Product List Pages


Any downloadable products that are enabled in admin will show like any other product on the frontend, but with the added feature of the "Download" tag as you'll see here...
https://www.abakhan.co.uk/catalogsearch/result/?q=Sirdar+Haworth+Tweed+Womens+Mock+Cable

The download tag is shown if the product is in the "Downloadable" attribute set

### Product Detail Pages

**Downloadable Products:**

When you click into a downloadable product page, you'll see a "View Physical Product" link below the add to basket button.
The "View Physical Product" link is determined by the product's "Associated Physical / Downloadable Product" attribute.
This attribute will have another product's SKU in there which triggers the relationship between the two. For example...

Abakhan Jumper Pattern (SKU = abajump01)
This product's "Associated Physical / Downloadable Product" has a value of "abajump01-download"
On the frontend of abajump01, the link will link to abajump01-download

**Physical Products:**

This works in exactly the same way as above; the only difference is the wording on the button:
"View downloadable PDF"
https://www.abakhan.co.uk/sirdar-haworth-tweed-womens-mock-cable-v-neck-cardigan-10147-81-137cm-32-54.html

### Troubleshooting

> "View Physical Product" or "View Downloadable PDF" links not working
{.is-danger}

Check whether the "Associated Physical / Downloadable Product" set on a product is enabled. If it's disabled, that's why it's throwing a 404. If it's enabled, speak to a FED

### Commercial Extensions
| Name | Version | Who purchased? | Login details for vendor |
|-|-|-|-|
| Adroll_Pixel
| Aheadworks_AddFreeProductToCart | 1.5.7 | CLIENT | `IT@abakhan.co.uk / AHead#2011` |
| Aheadworks_Blog | 2.12.0 | CLIENT | `IT@abakhan.co.uk / AHead#2011` |
| Aheadworks_GiftCard | 1.4.6 | CLIENT | `IT@abakhan.co.uk / AHead#2011` |
| Amasty_Base | 1.12.18 | CLIENT | `N/A` |
| Amasty_ShippingTableRates | 1.10.2 | CLIENT | `N/A` |
| Amazon_Core | 4.2.0 | CLIENT | `sales@allcrafts.co.uk / Amaz#2019z` |
| Amazon_Login | 4.2.0 | CLIENT | `sales@allcrafts.co.uk / Amaz#2019z` |
| Amazon_Payment | 4.2.0 | CLIENT | `sales@allcrafts.co.uk / Amaz#2019z` |
| Auctane_Api | 2.3.1 | CLIENT | `IT@abakhan.co.uk / fyp8OT12GRhK` |
| Awin_AdvertiserTracking
| Bss_AdminPaymentMethod | 1.0.1 | CLIENT | `N/A` |
| Bss_ProductStockAlert
| Bss_ProductStockAlertApi
| Bss_ProductStockAlertGraphQl
| Ebizmarts_MailChimp | 3.0.34 | CLIENT | `IT@abakhan.co.uk / Abakhan01` |
| Ebizmarts_SagePaySuite | 1.4.40 | CLIENT | `IT@abakhan.co.uk / Abakhan01` |
| Ess_M2ePro | 1.20.0 | CLIENT | `N/A` |
| Fooman_EmailAttachments | 107.2.0 | CLIENT | `N/A` |
| Fooman_GoogleAnalyticsPlus | 105.1.0 | CLIENT | `N/A` |
| Fooman_PdfCore | 19.15.1 | CLIENT | `N/A` |
| Fooman_PdfDesign | 1.4.1 | CLIENT | `N/A` |
| Fooman_PrintOrderPdf | 105.0.2 | CLIENT | `N/A` |
| Fooman_PdfCustomiser | 116.8.0 | CLIENT | `N/A` |
| Hackathon_EAVCleaner
| Hyva_BssProductStockAlert
| Klaviyo_Reclaim
| Magefan_AdminUserGuide | 2.0.1 | CLIENT | `N/A` |
| Magefan_Community| 2.1.8 | CLIENT | `N/A` |
| Magefan_LazyLoad | 2.0.16 | CLIENT | `N/A` |
| Mageplaza_Core | 1.4.11 | CLIENT | `N/A` |
| Mageplaza_Smtp | 4.7.1 | CLIENT | `N/A` |
| Mageside_SubscribeAtCheckout | 1.1.16 | CLIENT | `N/A` |
| MarkShust_DisableTwoFactorAuth | 1.1.4 | CLIENT | `N/A` |
| Mdoq_Connector
| Mollie_Payment
| PayPal_Braintree | 4.2.2 | CLIENT | `wabakhan@woolbox.co.uk / H3g#VoN2` |
| PayPal_BraintreeGraphQl | 4.1.2 | CLIENT | `wabakhan@woolbox.co.uk / H3g#VoN2` |
| Smile_ElasticsuiteAdminNotification
| Smile_ElasticsuiteCore
| Smile_ElasticsuiteCatalog
| Smile_ElasticsuiteCatalogGraphQl
| Smile_ElasticsuiteCatalogRule
| Smile_ElasticsuiteCatalogOptimizer
| Smile_ElasticsuiteTracker
| Smile_ElasticsuiteThesaurus
| Smile_ElasticsuiteSwatches
| Smile_ElasticsuiteIndices
| Smile_ElasticsuiteAnalytics
| Smile_ElasticsuiteVirtualCategory
| Stamped_Core
| Temando_ShippingRemover
| Temando_ShippingRemover | 1.0.0 | CLIENT | `N/A` |
| Wyomind_Framework | 7.0.9 | CLIENT | `N/A` |
| Wyomind_DataFeedManager
| Wyomind_SimpleGoogleShopping | 14.6.4 | CLIENT | `N/A` |
| Xtento_XtCore | 2.12.0 | CLIENT | `N/A` |
| Xtento_ProductExport | 2.14.6 | CLIENT | `N/A` |
| Yotpo_Yotpo| 3.1.3 | CLIENT | `N/A` |
| Zendesk_Zendesk
| Zero1_AddressFinder
| Zero1_Base
| Zero1_BssOosQty
| Zero1_BuyXForY
| Zero1_ClientSetup
| Zero1_Csp
| Zero1_GDPR
| Zero1_NewIn
| Zero1_PaypalQuoteCurrency
| Zero1_PrintedOrderStatus
| Zero1_ReleaseLibrary
| Zero1_RunCronJob
| Zero1_SampleProducts
| Zero1_SubCategoryList
| Zero1_SwatchesByStock







