Improved Checkout with UK Address Lookup using Loqate

[Personal Intro]
[Sponsor note]
[What you need]


[Setting the scene - show a site and how it benefits]
Ecommerce checkout is for obvious reasons a key focus in turning visitors into customers. Improving the simplicity of checkout is going to improve sales, that is ever more important as we move to smaller devices and become more impatient. Data entry is the more time-consuming aspect of checkout and in particular, address entry. While there are browsers that can pre-fill address fields in certain cases, Ecommerce sites now have bot-prevention measures which means auto-completion of fields is less successful than one might hope. We have therefore developed a free module which improves this experience. 

[on-screen walkthrough]
First what we need to do is install our free module. 
Get access to your Command Line Interface and navigate to the Magento Root directory then type `

composer require zero1/module-address-finder

` hit return then when that has completed run `

bin/magento setup:upgrade

`
Once the module is installed you need to login to the Admin system and configure it, OR you can simply run these commands as a quicker way to get up and running.

bin/magento config:set --lock-config zero1_address_finder/general/enable 1
bin/magento config:set --lock-config zero1_address_finder/general/account_code ZERO111116
bin/magento config:set --lock-config zero1_address_finder/general/public_key GU96-KY82-AH28-PD11

Then once the module is installed and configured you are ready to go ahead and test it. You might have automated testing setup but for now we are going to manually test this so that we can confirm it has no adverse effects on your site.

https://mdoq-acme-stuff-co-uk-10574.02.mdoq.io/

And there we have it, a fully functional, production-ready enhancement to your Magento store.

[back to camera]
I hope you find this guide useful in working with the Magento platform, if you are interested in knowing more please subscribe via any of our social channels and we will be posting regular guides on all things Magento.


FILLER 1 - 

If you have never worked with composer before, we will be releasing lots more videos about managing your Magento application dependencies with composer which is the best way to keep your platform up-to-date. 

What this process does is check for the most suitable version compatible with your installation. If you have purchased extensions from Magento Marketplace or any other leading vendor, then you will probably have been supplied Composer credentials which can easily be configured so that you can communicate with all the repositories required to keep your packages updated. This is a major improvement over Magento 1 as it allows you to run composer update to update the whole application, leaving you to test and fix any local aspects such as theme or client specific customisations. 

FILLER 2

The —lock-config argument will store the value into the config.php file, which



SETUP - GENERAL
Switch to the acme workstation user
Open Teleprompter, copy the final script above plus the intro script
Setup the Laptop Desktop for screen-recording mode
Cable the iPhone in and load it to the screen with Quicktime
Load Camtasia
Login to MDOQ using - wile.e.coyote@acme-stuff.co.uk  Password123



WORKING NOTES
We have this working on…. beanbagbazaar.co.uk
￼

Competition - https://github.com/ctidigital/magento2-google-address-lookup - they dont have post-code

Start here - https://mdoq.io/#/filter/client-65
