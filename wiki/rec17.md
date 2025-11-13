# Guide
1. Create instance
2. Log into SSH an run the following
  ```
  cd ~/htdocs; \
  php bin/magento config:set --lock-config -- dev/js/merge_files 1; \
  php bin/magento config:set --lock-config -- dev/js/minify_files 1; \
  php bin/magento config:set --lock-config -- dev/js/enable_js_bundling 1; \
  php bin/magento config:set --lock-config -- dev/js/move_script_to_bottom 1; \
  php bin/magento config:set --lock-config -- dev/css/minify_files 1; \
  php bin/magento deploy:mode:set production && php bin/magento cache:flush
  ```
3. Add `app/etc/config.php` to Git
4. Full test of the site

If all good pass to Adam for sign off

Take live
