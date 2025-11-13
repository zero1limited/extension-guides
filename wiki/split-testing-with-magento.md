# Split Testing

[TOC]


AB TESTING, Body Classes

so could we just have generic TEST containers

Test 1  / Default:Hide / Variant1:show

The JS always throws customers into a silo (Default/Variant1)
If you are a customer in Variant1, then the variant1 class will be added to the page body class.



<details>
  <summary>JSON for GTM</summary>
  
  ### Heading
  1. Foo
  2. Bar
     * Baz
     * Qux

  ### Some Javascript
  ```js
  function logSomething(something) {
    console.log('Something', something);
  }
  ```
</details>



Insert this into GTM [abtest.json](/operations/abtest.json)
```json
{
    "exportFormatVersion": 2,
    "exportTime": "2023-05-11 19:23:01",
    "containerVersion": {
        "path": "accounts/309752/containers/47150949/versions/0",
        "accountId": "309752",
        "containerId": "47150949",
        "containerVersionId": "0",
        "container": {
            "path": "accounts/309752/containers/47150949",
            "accountId": "309752",
            "containerId": "47150949",
            "name": "mdoq.acme-stuff.co.uk",
            "publicId": "GTM-WD64XT2",
            "usageContext": [
                "WEB"
            ],
            "fingerprint": "1624011440085",
            "tagManagerUrl": "https://tagmanager.google.com/#/container/accounts/309752/containers/47150949/workspaces?apiLink=container",
            "features": {
                "supportUserPermissions": true,
                "supportEnvironments": true,
                "supportWorkspaces": true,
                "supportGtagConfigs": false,
                "supportBuiltInVariables": true,
                "supportClients": false,
                "supportFolders": true,
                "supportTags": true,
                "supportTemplates": true,
                "supportTriggers": true,
                "supportVariables": true,
                "supportVersions": true,
                "supportZones": true
            },
            "tagIds": [
                "GTM-WD64XT2"
            ]
        },
        "tag": [
            {
                "accountId": "309752",
                "containerId": "47150949",
                "tagId": "23",
                "name": "AB Split Test",
                "type": "html",
                "parameter": [
                    {
                        "type": "TEMPLATE",
                        "key": "html",
                        "value": "<script> \n  console.log('{{ABCookie}}');\n  var defaultVariant = \"default\", variantOne = \"variantOne\", \n  variant = defaultVariant, \n  randomNumSample = 1073741823; \n\n  if(!{{ABCookie}}) { // If cookie isn't set run code\n    console.log('Cookie Not set, customer first visit');\n    if({{ABRandom}} < randomNumSample) {\n      console.log('ABRandom (GTM Var is LESS than randomNumSample');\n      variant = testVariant(); implementVariant();\n    }\n    var d = new Date();\n    d.setTime(d.getTime()+1000*60*60*24*730);\n    var expires = \"expires=\"+d.toGMTString();\n    document.cookie = \"ABCookie=\"+variant+\"; \"+expires+\"; path=/\";\n  } else if({{ABCookie}} == variantOne) { // If user has only seen Variation 1\n      console.log('cookie {{ABCookie}} is variant ' +variant);\n      variant = testVariant(); implementVariant();\n  } else {\n      console.log('cookie {{ABCookie}} is NOT matching ');\n  }\n  \nfunction testVariant() {\n    return variantOne;\n}\n  \nfunction implementVariant() {\n  \tdocument.body.className += ' variant1';\n}\n</script>"
                    },
                    {
                        "type": "BOOLEAN",
                        "key": "supportDocumentWrite",
                        "value": "false"
                    }
                ],
                "fingerprint": "1683815915640",
                "firingTriggerId": [
                    "2147479553"
                ],
                "parentFolderId": "21",
                "tagFiringOption": "ONCE_PER_EVENT",
                "monitoringMetadata": {
                    "type": "MAP"
                },
                "consentSettings": {
                    "consentStatus": "NOT_SET"
                }
            }
        ],
        "variable": [
            {
                "accountId": "309752",
                "containerId": "47150949",
                "variableId": "22",
                "name": "ABCookie",
                "type": "k",
                "parameter": [
                    {
                        "type": "BOOLEAN",
                        "key": "decodeCookie",
                        "value": "false"
                    },
                    {
                        "type": "TEMPLATE",
                        "key": "name",
                        "value": "ABCookie"
                    }
                ],
                "fingerprint": "1683812794878",
                "parentFolderId": "21",
                "formatValue": {}
            },
            {
                "accountId": "309752",
                "containerId": "47150949",
                "variableId": "24",
                "name": "ABRandom",
                "type": "r",
                "fingerprint": "1683810248234",
                "parentFolderId": "21"
            }
        ],
        "folder": [
            {
                "accountId": "309752",
                "containerId": "47150949",
                "folderId": "21",
                "name": "ZERO1 AB Testing",
                "fingerprint": "1683809111159"
            }
        ],
        "fingerprint": "1683832981597",
        "tagManagerUrl": "https://tagmanager.google.com/#/versions/accounts/309752/containers/47150949/versions/0?apiLink=version"
    }
}

```


GA4 Admin : Custom Definitions: Custom Dimensions : Dimension Name: 'AB Test' with scope User
Set the User Property value to 'abcookie'

Then edit your main GA4 tag, add a configuration parameter called abcookie, then the values as {{ABCookie}}

Viewing this data in GA4 - https://www.analyticsmania.com/post/view-custom-dimensions-in-google-analytics/
We simply look at Report Comparisons - waiting for this to show 

waiting as of setup 21 May 2025

```
<style>
body.variant1 .variant1 {display:block;}
body.variant0 .variant0 {display:block;}

body.variant0 .variant1 {display:none;}
body.variant1 .variant0 {display:none;}

</style>
```

Custom Dimensions in GA4
When you send the user properties to Google Analytics 4, you must register them as user-scoped custom dimensions in the GA4 interface. To do that, you must go to Admin > Custom Definitions > Custom Dimensions and click Create Custom Dimensions. Then enter the following settings: Make sure the scope is User.8 Apr 2023

### PILOT - extensions.zero1.co.uk
https://analytics.google.com/analytics/web/?authuser=0#/p470469160/reports/intelligenthome
https://analytics.google.com/analytics/web/?authuser=0#/analysis/p470469160/edit/vOtyG-8ZRnCt4S15Ay7Hog

https://www.youtube.com/watch?v=T12YSrswMQ0
need to check data again 
https://analytics.google.com/analytics/web/?authuser=0#/p470469160/reports/explorer?params=_u..nav%3Dmaui%26_u.dateOption%3Dtoday%26_u.comparisonOption%3Ddisabled%26_u..comparisons%3D%5B%7B%22savedComparisonId%22:%2210058395091%22,%22name%22:%22All%20Users%22,%22isEnabled%22:true,%22filters%22:%5B%5D,%22systemDefinedSavedComparisonType%22:8,%22isSystemDefined%22:true%7D,%7B%22name%22:%22AB%20Test%20Group%20does%20not%20contain%200%22,%22isEnabled%22:true,%22filters%22:%5B%7B%22fieldName%22:%22customDimensionsGroup1Slot01%22,%22evaluationType%22:3,%22expressionList%22:%5B%220%22%5D,%22complement%22:true,%22isCaseSensitive%22:true%7D%5D%7D%5D%26_r.explorerCard..seldim%3D%5B%22sessionPrimaryChannelGroup%22,%22customDimensionsGroup1Slot01%22%5D&ruid=lifecycle-traffic-acquisition-v2,business-objectives,generate-leads&collectionId=business-objectives&r=lifecycle-traffic-acquisition-v2

## Adopting the same process for behavioural

So you can use the above, but set cookie values so an array for....
cares['shipping','applepay','reviews']
so if you wish, you can implement a block but use css styles such as cares-shipping and these blocks will only show for those customers expressing interest.

interest can be set on any other website interaction.
We set interactions using click interactions which have a class of 'track-care-shipping', this will add shipping to the 'cares' cookie array.



![cares-about.png](/media/cares-about.png)




