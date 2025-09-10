# Google reCAPTCHA

This is our WIKI home for everything related to Google reCAPTCHA

## Can not resolve reCAPTCHA parameter

think we have a better process for this somewhere - https://github.com/zero1limited/ghost-inspector-mdoq-pras/blob/master/post-rollup-actions
need to work through projects and implement the above so we can make easy amends for rolling out across all clients.


Add this to /mdoq/post_roll_up_actions

```
curl -s https://raw.githubusercontent.com/zero1limited/ghost-inspector-mdoq-pras/master/post-rollup-actions | bash

```

[Clients currently using this method](https://github.com/search?q=org%3Azero1limited%20ghost-inspector-mdoq-pras&type=code)





## Debugging Hack

We have frequent Exception logs indicating "Can not resolve reCAPTCHA" which is a worry sometimes. We have a pikey patch to gather more information on this

Edit `vendor/magento/module-re-captcha-ui/Model/CaptchaResponseResolver.php`

Change line 25 to 
```
throw new InputException(__('Can not resolve reCAPTCHA parameter.'.$_SERVER['HTTP_HOST'].$_SERVER['REQUEST_URI']));

```
