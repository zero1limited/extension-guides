# Encryption Key Rotation
This is a guide on how to rotate your sites encryption keys, based off the [Adobe documetation](https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/troubleshooting/known-issues-patches-attached/security-update-available-for-adobe-commerce-apsb24-40-revised-to-include-isolated-patch-for-cve-2024-34102)

## Steps
1. Enable maintenance mode. bin/magento maintenance:enable
2. Disable cron jobs. crontab -e
3. On the Admin sidebar, go to System > Other Settings > Manage Encryption Key.
4. Do one of the following:
- To generate a new key, set Auto-generate Key to Yes.
- To use a different key, set Auto-generate Key to No. Then in the New Key field, enter or paste the key that you want to use.
5. Click Change Encryption Key.
6. Flush the cache. bin/magento cache:flush
7. Enable cron jobs. crontab -e
8. Disable maintenance mode. bin/magento maintenance:disable


## Sits on the latest version of the patch (2.4.6-p7, 2.4.5-p9, 2.4.4-P10)

This new command should be executed on the environment that contains your app/etc/env.php file for the key that you want to update.

Confirm that the new command exists:
`bin/magento list | grep encryption:key:change`

You should see the following output:
`encryption:key:change Change the encryption key inside the env.php file.`

Change the encryption key:
`bin/magento encryption:key:change`


If you have executed this command on your production system, no further action should be required.
If you have run this on a development system, you must get this change into your production system as you would normally deploy sensitive configuration settings.

