<img src="https://www.zero1.co.uk/media/wysiwyg/openpos_1.jpg" width="100%" height="auto" />

# What is OpenPOS?

Everything you need to know about OpenPOS [is here](https://www.zero1.co.uk/blog/post/stories/openpos) 😁

Your Help is GREATLY appreciated.

If you are a merchant or agency wanting to implement OpenPOS please [join the OpenPOS Slack Channel Here](https://join.slack.com/t/openpos-workspace/shared_invite/zt-32ozggysy-s1XeL_IcChy6PLLNmtUMeg)

# Info

[Installation](#installation)

[Configuration](#configuration)

[Changelog](CHANGELOG.md)


# Installation

```
composer require zero1/open-pos
```

```
php bin/magento setup:upgrade
```

```
php bin/magento deploy:mode:set production
```

# Configuration

We appreciate feedback (including bugs or installation issues) via our new [community Slack Channel](https://join.slack.com/t/openpos-workspace/shared_invite/zt-32ozggysy-s1XeL_IcChy6PLLNmtUMeg). 

Configuration can be found in:
[Stores] -> [Configuration] -> [OpenPOS] -> [Configuration]

Once the module is installed, you can run `bin/magento openpos:setup-wizard` for guided setup of the POS store.


> [!TIP]
> Incase you didn't already know, OpenPOS is built to run as a standard Magento website, therefore you need to perform all relevant domain and webserver configuration to ensure the site resolves and is externally accessible.


# Theme Association
As part of any traditional Hyvä Theme setup you might want to copy our base POS theme into app/design and inherit `openpos/default`
If you are using our default template simply set your POS website theme to 'OpenPOS Default'