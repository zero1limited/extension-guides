# SDS London 

[TOC]

Everything relating to how SDS works is now detailed in a public wiki here - https://zero1.teamwork.com/#/notebooks/299559

Please could you make sure that any new features / changes / debugs etc are detailed in that wiki to make life easier for both us and SDS please? Thanks!

Sean.

**Trade Account**
Username: `sean.watson@zero1.co.uk`
Password: `Ch0plapaz@`


## Enhanced Product Ordering via ElasticSuite Optimizers
Optimisers are a part of the Elasticsuite extension and found in Magento Admin under the ElasticSuite menu item.






## Intec Middleware Integration

Public Notebook available here https://zero1.teamwork.com/#/projects/552862/notebooks/287150

Testing Inbound Stock updates

1. Check files are being pulled from the Middleware with `cd ~/htdocs && bin/magento crmsync:ftp` then check whether any files have been pulled using `ls -la var/import/intec/`. If recent files are listed here then FTP communication is working and you can now test stock updates using `cd ~/htdocs && bin/magento crmsync:stock`. When run manually via CLI this should output stock items for each update.

## Commercial Extensions
| Name | Version | Who purchased? | Login details for vendor |
|-|-|-|-|
Amasty_Base |
Amasty_CommonTests |
Amasty_Geoip |
Amasty_InvisibleCaptcha |
Amasty_Orderattr |
Amasty_Pgrid |
Amasty_ShippingTableRates |
Amazon_Core |
Amazon_Login |
Amazon_Payment |
Baldwin_UrlDataIntegrityChecker |
Bss_ForceLogin |
Dotdigitalgroup_Email |
Dotdigitalgroup_Chat |
Dotdigitalgroup_ChatGraphQl |
Dotdigitalgroup_EmailGraphQl |
Dotdigitalgroup_Sms |
Ebizmarts_SagePaySuite |
Hackathon_EAVCleaner |
Hyva_Checkout |
Hyva_Email |
Hyva_GraphqlTokens |
Hyva_GraphqlViewModel |
Hyva_ThemeFallback |
Hyva_ReactCheckout |
Smile_ElasticsuiteCore |
Hyva_Theme |
Hyva_LumaCheckout |
Idealpostcodes_Ukaddresssearch |
JBC_CRMSync |
Klarna_Core |
Klarna_Ordermanagement |
Klarna_Kp |
Klarna_Onsitemessaging |
Klarna_KpGraphQl |
MageArray_StorePickup |
Mageplaza_Core |
Mageplaza_BannerSlider |
Mageplaza_ShareCart |
Mageplaza_Smtp |
Mdoq_Connector |
Mollie_Payment |
PayPal_Braintree |
PayPal_BraintreeGraphQl |
RedChamps_Core |
RedChamps_CustomerGroupSpecificEmails |
Smile_ElasticsuiteAdminNotification |
Smile_ElasticsuiteCatalog |
Smile_ElasticsuiteSwatches |
Smile_ElasticsuiteCatalogGraphQl |
Smile_ElasticsuiteCatalogRule |
Smile_ElasticsuiteCatalogOptimizer |
Smile_ElasticsuiteTracker |
Smile_ElasticsuiteThesaurus |
Hyva_SmileElasticsuite |
Smile_ElasticsuiteIndices |
Smile_ElasticsuiteAnalytics |
Smile_ElasticsuiteVirtualCategory |
Temando_ShippingRemover |
Trustpilot_Reviews |
Vertex_Tax |
Vertex_AddressValidationApi |
Vertex_RequestLoggingApi |
Vertex_RequestLogging |
Vertex_AddressValidation |
Wyomind_Framework |
Wyomind_DataFeedManager |
Yotpo_Yotpo |
Zero1_AutomaticGroupedOrdering |
Zero1_BreadcrumbsPDP |
Zero1_DisablePaymentMethod |
Zero1_EnhancedConversionTracking |
Zero1_Ga4Gtm |
Zero1_ImprovedCheckoutSuccessPageHyva |
Zero1_OrderGroupedVariations |
Zero1_PageBuilderWebVitals |
Zero1_Patches |
Zero1_Release |
Zero1_SDSGroupedProducts |
Zero1_SDSModifications |
Zero1_ShortCategoryPaths |
Zero1_SortByPrice |
Zero1_Splats |
Zero1_SubCategoryListing |
Zero1_TradeAccountSignUp |
Zero1_TradeApplication |
Zero1_TradeRedirection |

