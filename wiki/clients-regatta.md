# Regatta

[TOC]
## Contents
- [Mdoq Instances](#mdoq-instances)


## Magento Upgrade 2.4.6-p3
Bits about the upgrade

Magento Instance:           https://my.mdoq.io/#/filter/client-70/instance/20388
VSFB Instance (ch_uk):      https://my.mdoq.io/#/filter/client-70/instance/20798
VSFF Instance (ch_uk):      https://my.mdoq.io/#/filter/client-70/instance/20799


### Mdoq Instances
Regatta have their own Mdoq server, because of certain issues you need a hosts file ammend.

You can identify an instance their server because the url contains `.regatta-basecamp.mdoq.io`

If you instance has the following url:
`www-dare2b-fr-8985.regatta-basecamp.mdoq.io`
You will need to add:
```
167.98.165.89 www-dare2b-fr-8985.regatta-basecamp.mdoq.io
```
To your hosts file.
If you are on Mac or Linux you can run:
```
sudo echo "167.98.165.89 www-dare2b-fr-8985.regatta-basecamp.mdoq.io" >> /etc/hosts
```
If you are on windows you will need to edit
```
C:\Windows\System32\drivers\etc\hosts
```

Repeat this as many times as needed. (The IP will always be the same but the url will change)