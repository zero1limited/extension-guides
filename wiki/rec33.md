# Enhanced GA4 Tracking for Messages, Notices & Alerts

[TOC]
<!--

PITCH


We have developed a set of code enhancements to Magento which provides some good behaviour insights into user activity. With this work we can additionally track the following in Google Analytics:

All Error, Warning & Success Notices on the front-end. This can provide valuable insight to issues with login, promo codes and checkout among other things. Many of these errors are shown to your users yet not fed back to the business owner, can provide actionable remedies to improve sales.

This work will take approximately 4 hours, please confirm if you are happy for us to proceed with this. 

Requirements
- you must have a fully functional Google Tag Manager account
- Universal Analytics
- Magento 2.3.5+

-->

## Pre-Requisites
Please carry out these steps either before you raise the recommendation or before work is started

**Check that the GTM account does not already contain any of the following**

Triggers
- Magento messages present
- Magento cart-empty message present

Tags
- GA Event - Magento messages
- GA Event - Magento cart-empty present

Once you are happy this has not already been installed, continue with the installation or raise the recommendation

## Instructions

Before you start and import the tags, you need to check you have a User Defined Variable called AnalyicsPropertyID


In Google Tag Manager account visit the Admin tab for your site, then select your container, then click Import Container
Download the attached NEEDTOCREATE-WHEN-CONFIRMED file then follow the instructions in the animation below

With the above 2 elements in place you should now be able to gain some great insights into;

Magento Core Messages - Visit Behaviour > Events in Google Analytics and gain valuable insight into events such as:

- Failed Logins
- Out of stock notices
- Invalid Coupon Codes
- Add to cart failures
- any other message which gets presented in the Magento core Warning/Alert/Success box

**Test your changes using the Preview option in GTM**
You can test this by visiting:
1. The website, attempting to login with an incorrect password
2. Review Google Analytics > Real-Time > Events

Once you are happy you can publish the changes (if you have permissions) and report back to the task owner.



## Initial working POC (Proof of concept)
divinetrash.co.uk https://tagmanager.google.com/#/container/accounts/168942493/containers/61496383/workspaces/36/tags?orgId=SNAsdj08SQCqBbb269rGTQ
This uses the custom event name 'message'

WORKING REPORT https://analytics.google.com/analytics/web/?authuser=0#/analysis/p312433204/edit/UrBpgp0XS3e9Es46FMtLfA

23 October 2024
https://www.youtube.com/watch?v=QmEOPuJr05w
Published a new variable for the Hyvä selector, appears to be working?

Principally this appears to be working for Divine Trash, need to wait 1 day for data, according to the video also I should not need to create dimensions and all that shit.
then I can incorporate into the Looker Studio Report.

