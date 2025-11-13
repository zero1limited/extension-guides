# Email
Everything related to email handling and transport for merchants 



[TOC]

* What to look out for:
  Ask client what mailbox is used for their mail
  If Office365 we cannot use usual SMTP module e.g. mageplaza or Magento core SMTP due to Oauth 2.0, ask client if they can use a different mailbox? - possible to use amasty SMTP module as this supports oauth however this is a paid module...

* What to avoid:
  Avoid proceeding with SMTP if Office365 is being used. Local relay / sendgrid can be used

* what service to recommend based on KEY information (like avoiding SMTP at ALL costs of they are using 365):
  If anything over than Microfsoft is being used then we can use core magento 2.4.6 SMTP for mail sending
  Avoid using SMTP if the mailbox is 365!

* How to estimate (MUST be based on domains/sites/method etc):
  Check with the client what mailbox is being used
  How many domains/sites are being used (are there different mailboxes for different sites)
  If 365 estimate differently to other methods as we can't use SMTP for this.

## TODO

Confirm primary recommendation(s)
Confirm discovery Q&A


## Local Mail delivery - 
DKIM issues will be faced so we don't have a solution with MDOQ currently

We are starting to roll out local relay due to increasingly flaky 3rd parties, we have this running on some sites inc zero1.co.uk in the php-fpm/configure 

```
cp /etc/resolv.conf /var/spool/postfix/etc/resolv.conf
service postfix stop && service postfix start
```

the above is working on zero1.co.uk but for other sites like pozzani we must use `supervisorctl restart postfix` why?


## SMTP Service Providers
Sendgrid - not responded to multiple reseller requests
Mailgun - no reseller options


## Extensions 
[Amasty](https://amasty.com/smtp-email-settings-for-magento-2.html)
List others we use


## Testing Email Delivery

* Go to https://www.mail-tester.com/ to get the test email needed to check the report
* Next, go to the live site you are testing and make an account with the above test email
* Go back to https://www.mail-tester.com/ and check the score
* The result will appear, with dropdowns of improvements/successes

Example of SPF record change:

>SPF record needs amending:
>What we retained as your current SPF record is:
>
>{current SPF record}<br/>
>
>It should be changed to:
>
>{new SPF record}<br/>
>
>There is no DMARC record either.

Link the report for any future use if needed

**Ensure that the email domain being used in Magento is correct**

This can be done by checking this line below the new/recommended SPF record: `The Name Server handling the domain name {domainName}`

