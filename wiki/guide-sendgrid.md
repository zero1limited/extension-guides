# Sendgrid

## Pitch

Starting in April 2024, Gmail and Yahoo! will enforce new requirements for what mail they’ll accept and transmit to users’ inboxes.

What does this mean?
From April 2024 there will be stricter rules enforcing the use of DKIM for email authentication which requires work on your sending mail server and also domain name server. 

## Requirements

• Client must be on Magento 2.4.6 otherwise we need to use `mageplaza/module-smtp` - 2 hours more work
• Client must have a SendGrid Account
• Client ideally must be with Cloudflare

## Installation / Setup
Ask the client to setup an account via https://sendgrid.com/en-ukpricing

Visit the teammates https://app.sendgrid.com/settings/teammates page and 'Invite as Admin' whichever email address the ZERO-1 staff member has requested.






### Domain Auth
https://app.sendgrid.com/settings/sender_auth


### Setup sending key
https://app.sendgrid.com/guide/integrate/langs/smtp

Config for core Magento 2.4.6

> [!TIP]
> If we do this on a dev instance we can bake in with --lock-config

```
bin/magento config:set --lock-config system/smtp/host smtp.sendgrid.net
bin/magento config:set --lock-config system/smtp/port 587
bin/magento config:set --lock-config system/smtp/set_return_path 0
bin/magento config:set --lock-config system/smtp/transport smtp
bin/magento config:set --lock-config system/smtp/username apikey
bin/magento config:set --lock-config system/smtp/auth login
bin/magento config:set --lock-config system/smtp/ssl tls
```

Config for Mageplaza
- if we do this on a dev instance we can bake in with --lock-config
```
bin/magento config:set --lock-config smtp/general/enabled 1
bin/magento config:set --lock-config smtp/general/log_email 0
bin/magento config:set --lock-config smtp/configuration_option/host smtp.sendgrid.net
bin/magento config:set --lock-config smtp/configuration_option/port 587
bin/magento config:set --lock-config smtp/configuration_option/protocol tls
bin/magento config:set --lock-config smtp/configuration_option/authentication login
bin/magento config:set --lock-config smtp/configuration_option/username apikey
bin/magento config:set --lock-config smtp/configuration_option/test_email/from general
bin/magento config:set --lock-config smtp/developer/developer_mode 0
```
> [!IMPORTANT]
> Then save the API key in admin


### Testing
Create an account on the website front-end for EACH domain/website

[test-gwvmp966p@srv1.mail-tester.com](https://www.mail-tester.com/)https://www.mail-tester.com/
