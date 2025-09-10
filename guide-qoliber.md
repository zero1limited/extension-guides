# Qoliber - Partnership

Hi Arron,

Thank you for being patient with us, here are composer keys and list of extensions ready to install:

Private Packagist Access:
```
composer config repositories.qoliber composer https://qoliber.repo.packagist.com/zero1/
composer config --global --auth http-basic.qoliber.repo.packagist.com token 313f922e0141047f07a8d7689051ff1e90d12472f4a84247f51badecc02c
```
Token for auth.json:
```
composer config --auth http-basic.qoliber.repo.packagist.com token 313f922e0141047f07a8d7689051ff1e90d12472f4a84247f51badecc02c
```
Packages List:
```
qoliber/faq
-
qoliber/faq
qoliber/fastsearch-magento2
qoliber/gpsr
qoliber/product-attachments
qoliber/product-labels
qoliber/product-labels-hyva

qoliber/attribute-seo-path (installed with other modules)
qoliber/seo-advanced-sitemaps
qoliber/seo-advisor-ai
qoliber/seo-dynamic-tags
qoliber/seo-dynamic-descriptions
qoliber/seo-friendly-product-urls
qoliber/seo-href-lang
qoliber/seo-images-friendly-url
qoliber/seo-opengraph-tags
qoliber/seo-pretty-filters-elasticsuite (special package for ElasticSuite compatibility for pretty filters)
qoliber/seo-pretty-filters
qoliber/seo-rich-snippets

```

## Fast Search

```
composer require qoliber/fastsearch-magento2:2.0.0-rc5


```





Docs (still under development):
https://docs.qoliber.com/

Staging docs:
https://stage-docs.qoliber.com/
user: stage-docs	
password: qoliber

All new extensions, updated and future versions will be uploaded to stage-docs.qoliber.com before the main launch in July. 
If you have ANY questions don't hesitate to contact me and plan a meeting where the can show you how each extension work.
We are focused on delivering as much extensions as possible till end of July, so the documentation might be updated a little bit later - as we want to shock the market with the quality and the number of plugins in the qoliber stratos pack (name was never discussed but has a nice feeling to it). 

Kind Regards,
Jakub Winkler




### Debugging Fast Search

Attempting fully clean install https://miami-dev-22131.04.mdoq.io/

```
rm -rf generated; php bin/magento setup:install --base-url='https://miami-dev-22131.04.mdoq.io/' --db-host='22131-mysql' --db-name='magento' --db-user='magento' --db-password='zero1zero1' --admin-firstname='Arron' --admin-lastname='Moss' --admin-email='arron.moss@zero1.co.uk' --admin-user='arron' --admin-password='24bAsiL54' --language='en_GB' --currency='GBP' --timezone='Europe/London' --es-hosts='22131-elastic-search:9200' --use-rewrites=1 --cleanup-database
```

##  Jakub SSH key for support
```
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDpO3eDaJXMnzGC4iafY7UwLYNjr7OpnQuhpVuVVT9BLaO+Dck5RUNN8/4YLlsGwS0+MEMT83w5lfVzrkF7NnH0/FVn5YrDy9lMzB/W3ImeEXsYKNxfk06UrkKJsccYrcuUq/TIpsK/OcAFuVSwLAf+QvNUtPQ7jlM+wZmrCzsX3whVRADeGIO+MleGk85+RwaISoP2v9550kmGYsYSqW7O93zGVqC4dAB9QhAKw6RR7U954XVyAho9nUQMhTdJXSdHyg0v/6TgwqkATJFUzbm7PL3PD/JXnOLVWzSHQG42mEztHnHDOPkMti2+q4p62vvGitazclXDREhdmxlcOJMyHPcNw7gL8c5r2lqb8XJCFERjpRNL9BsyIcHjipgTnDGkNlaQVUINjG0zt6JZwyI9ZWCqeea7VQcVYPi614o2V5RfIlWpKj0j7mQGwJapT+N7OUpJGPATVhzOVEVPDCm0sF3dGFScc3w98ljc1JS3iPFwC6bDA4wnFdFwEs9nrnoFG+Hh/51lazA4KfnAiWs1hWn0B9zDXJijrvkQJP9Iod9KfbhOkdn2Ww6zE71R2UskvfXCQz6eGMC2QgWbIYdqUi1W8nzCpo1xChZGqP9sUs+Exxp5BV1O2dEDqgwOvUIeXAA5gq/8EVD5+AX0992oeUbOFCywb4GxMkehpMsy8Q== jwinkler@qoliber.com

```






