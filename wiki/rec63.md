# Coding Standards Review

## Pitch
https://devdocs.magento.com/guides/v2.4/coding-standards/code-standard-php.html

## Process
### Who


### Setup
`composer.json`
```
"scripts": {
        "post-install-cmd": [
          "([ $COMPOSER_DEV_MODE -eq 0 ] || vendor/bin/phpcs --config-set installed_paths ../../magento/magento-coding-standard/)"
        ],
        "post-update-cmd": [
          "([ $COMPOSER_DEV_MODE -eq 0 ] || vendor/bin/phpcs --config-set installed_paths ../../magento/magento-coding-standard/)"
        ],
        "phpcs-report": [
            "Composer\\Config::disableProcessTimeout",
            "if [ ! -d zero1/phpcs ]; then mkdir -p zero1/phpcs; fi; ./vendor/bin/phpcs --standard=Magento2 -p --report-full=zero1/phpcs/$(date +%F)_app_report --report-summary=zero1/phpcs/$(date +%F)_app_summary app; ./vendor/bin/phpcs --standard=Magento2 -p --report-summary=zero1/phpcs/$(date +%F)_vendor_summary --ignore=/vendor/magento vendor"
        ],
        "phpcs-fix": [
            "Composer\\Config::disableProcessTimeout",
            "./vendor/bin/phpcfb --standard=Magento2 -p app"
        ]
    }
```
```
composer require --dev phpstan/phpstan
composer require --dev squizlabs/php_codesniffer
composer require --dev magento/magento-coding-standard
./vendor/bin/phpcs --config-set installed_paths ../../magento/magento-coding-standard/
```

https://pear.php.net/manual/en/package.php.php-codesniffer.reporting.php
https://github.com/magento/magento-coding-standard
https://github.com/squizlabs/PHP_CodeSniffer/wiki




### Instructions

```
composer run-script phpcs-report
```

reports in zero1/*

commit report

maybe aggregate so we can give a tend (maybe as %warn %error)

explain diff between app and vendor reports

also need to look at: https://github.com/wapmorgan/PhpDeprecationDetector
https://github.com/exakat/php-static-analysis-tools
https://phpstan.org/
