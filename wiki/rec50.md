<!--
# Content Security Policy
Recent Reference sites - divinetrash.co.uk
https://github.com/zero1limited/ibottles/tree/master/app/code/Custom/Csp/etc

https://devdocs.magento.com/guides/v2.3/extension-dev-guide/security/content-security-policies.html

### Pitch Email
Content Security Policies (CSP) are a powerful tool to mitigate against Cross Site Scripting (XSS) and related attacks, including card skimmers, session hijacking, clickjacking, and more. Web servers send CSPs in response HTTP headers (namely Content-Security-Policy and Content-Security-Policy-Report-Only) to browsers that whitelist the origins of scripts, styles, and other resources. Together, CSPs and built-in browser features help prevent:

• Loading a malicious script from an attacker’s website
• A malicious inline script from sending credit card info to an attacker’s website
• Loading a malicious style that will make users click on an element that wasn’t supposed to be on a page

-->

# Phase 1 work
- Create your development instance
- Follow this guide https://github.com/zero1limited/magento2-module-csp/blob/master/README.md


> If you do not see the URL and see `<URL>` then this means your report is grouping the error, click the little arrow to the left if the report which should be inside a red oval containing also a number.
{.is-info}


![csp-debugging.png](/recommendations/csp-debugging.png)

> In the first report item above fonts.googleapi.com needs adding as an item into the style-src policy as per the example below.
{.is-info}

        <policy id="style-src">
            <values>
                <value id="googleapis" type="host">fonts.googleapis.com</value>
                ... other values here
            </values>
        </policy>

- Please repeat the process until you receive no further Content Security Policy violations - this is very important
- As an extra measure you may also wish to add your own domain as a wildcard option so that future domain charding work can take place. typically you could add `*.yourdomain.com` into `style-src` and `script-src`

- Test the site thoroughly - using MDOQ you can do this automatically with the aid of Ghost Inspector
- finish by setting the Magento configuration so that the website is strictly applying CSP as follows

Ensure the config.php puts the extension into Report Only Mode with these directives in the mode tag in app/code/Zero1/Csp/etc/config.php

            <mode>
                <storefront>
                    <report_uri>https://zero1.report-uri.com/r/d/csp/reportOnly</report_uri>
                    <report_only>1</report_only>
                </storefront>
                <admin>
                    <report_only>1</report_only>
                    <report_uri>https://zero1.report-uri.com/r/d/csp/reportOnly</report_uri>
                </admin>
            </mode>


- Commit your changes to source control
- Hand off to QA for final test and deploy - this is a downtime deployment which craig needs to do early morning ensuring a 3rd line dev is on hand.

# Phase 1 Review

Ensuring at least 1 week has passed since the depoyment of the phase 1 work, Review the live site again and also review the account report-url.com (user arron.moss@zero1.co.uk / `zZwI1t*B8o3%R9D$`) for any errors reported for this domain. To achieve this you should be able to review https://report-uri.com/account/reports/csp/ to look for reported URLs still containing policy violations.



# Phase 2 work


Amend any policies as necessary, and if you have to add new policies you need to deploy again and we need 1 week of no violations before making the below change to app/code/Zero1/Csp/etc/config.php


            <mode>
                <storefront>
                    <report_uri>https://zero1.report-uri.com/r/d/csp/reportOnly</report_uri>
                    <report_only>1</report_only>
                </storefront>
                <admin>
                    <report_only>1</report_only>
                </admin>
            </mode>

PLEASE NOTE: Changed 10 May 2022 - we will leave report_only mode set to 1 and as part of our security practices just keep reviewing report-url.com until we have more data (future task TBC).
All phase 2 deployments should be zero-downtime so can happen any time of day


## Related Material
[csp.zip](/modules/csp.zip)
