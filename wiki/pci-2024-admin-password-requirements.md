# PCI security requirements 2024 - Password policy
How to setup/install ZERO1s password requirements module, to comply with 2024 password policy requirements.

[TOC]

## Instructions
1. `composer require zero1/admin-user-password-requirements`
2. `php bin/magento module:enable Zero1_AdminUserPasswordRequirements`
3. `php bin/magento setup:upgrade && php bin/magento deploy:mode:set production && php bin/magento cache:flush`

## Testing
1. Log into the MAP
2. Try to change your password (`password1234`), validate you get some errors.
3. Change password to something that meets the requirements (`PAssword1234_!`)
4. Log out and back in with the new password.