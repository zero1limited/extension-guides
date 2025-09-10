# Spillwarehouse / Newpig

[TOC]


# Magento Cloud

Arron has authorisation to access the Cloud Project via https://account.magento.com/cloud/project/subscriptions/

Then https://cloud.magento.com/project/3684/dashboard/gettingstarted


Dev Site on Master https://master-7rqtwti-5l4ppgunholbi.eu-3.magentosite.cloud/

Project Access Web GUI (Platform.sh) https://eu-3.magento.cloud/projects/5l4ppgunholbi/environments/master


```
git clone --branch master 5l4ppgunholbi@git.eu-3.magento.cloud:5l4ppgunholbi.git new-pig-bv
```

## Preproduction site
This is the main production instance with 16vCPU which will eventually become live
- [Frontend](https://master-7rqtwti-5l4ppgunholbi.eu-3.magentosite.cloud/)
- [Magento Admin Panel](https://master-7rqtwti-5l4ppgunholbi.eu-3.magentosite.cloud/admin/)


## Deployment pipeline
In order to initiate a production deployment you simply need to manually merge your work into the 'master' branch, this will trigger the deployment on production.


ZERO-1 user accounts
- arronm-zero1
- paulf-zero1





# Current M1 Site

Anything relating to the current M1 site goes here...

### PDFs
New Pig should now be uploading their PDFs via SFTP access.
(THESE CREDS ARE PROBABLY OLD, CHECK BELOW FOR UPDATED CREDS)
- *Host*: `37.220.90.121`
- *Port*: `2020`
- *Username*: `spill-sftp`
- *Password*: `ye2qH7aT5pvK6rG#3E2B`

The directory `magebox` should be in that users home directory.


### PDFs - Legacy

New Pig upload their PDFs to Magento via Dropbox which is linked to a Magebox module.

Instructions for uploading a PDF...

1 - Go to https://www.dropbox.com/

2 - Login with <a href="https://zero1.teamwork.com/#tasks/22540822?c=9440077">these login details</a>

3 - Navigate in Dropbox to Apps/Magebox/spillwarehouse

4 - Upload the PDF here (or in one of the sub folders or create a new sub folder). Just take note of the folder(s) it's in

5 - Go to Magento Admin > Catalog > Magebox > Update Files

6 - Once the files have been updated, go back to Dropbox and get the folder names and filename of the PDF.
E.g. /Trademarks/New Pig Trademark.pdf

7 - Replace any spaces in the filename with %20
This example is /Trademarks/New%20Pig%20Trademark%20List.pdf

8- Copy the folder and file name as above and add it to the end of this URL...
https://www.newpig.de/media/wysiwyg/magebox/spillwarehouse/
Then you've got the final link on Magento...
https://www.newpig.de/media/wysiwyg/magebox/spillwarehouse/Trademarks/New%20Pig%20Trademark%20List.pdf


## Password Reset
### SSH

**updating password**
1. login via ssh 
2. as root run `passwd`
3. open a new terminal and try and log in with new creds. (If you can't don't close anything and seek assistance)
4. If all good update creds in wiki (see below)

**Creds**
**Host**: `37.220.90.121`  
**Port**: `2020`  
**Username**: `root`  
**Password**: `43+g*l"z723w\um&_l@`
(`ssh root@37.220.90.121 -p2020`)

**N.B** because this server is now very old the SSH key types it forces aren't "safe" you may get the error: `Unable to negotiate with 37.220.90.121 port 2020: no matching host key type found. Their offer: ssh-rsa,ssh-dss`
If you do you need to add 
```
HostKeyAlgorithms ssh-rsa
PubkeyAcceptedKeyTypes ssh-rsa
```
To your `~/.ssh/config` file whilst accessing the server, then remove after as it will break newer connections.

Old Passwords
- `w21T3Nb@3%%x^neh4SEG`
- `1ez3aJhxR#L*JMYyg8jQD!pNha`
- `UdC9QHSAKf)fczSGS`
- `z=;c?s(1}!80>xu,}`
- `&Xg6r#3U7HyN4G7eqHNS8JsFCHhat5`
- `JzENUEQfg!*6lkdjSHbfDYl0x0XwnNU8kc$mR2ceaa&V2$KyEg`
- `0LC1Ofg)uypfSPhB#)z4lTNc(8KMgxez`


### SFTP

**updating password**
1. login via ssh
2. as root run `passwd spill-sftp`
3. attempt new sftp connection
4. if all good send the new password (via the ticket) to:
  - Simone Sengers-Veldhuizen 
  - Ashley Ventilla-Logan
5. updated password in this wiki

**Creds**
**Host**: `37.220.90.121`
**Port**: `2020`
**Username**: `spill-sftp`
**Password**: `=p@#[h4s'o!y&(t7\2"`

Old Passwords
- `a4E8qjPnU4AT4C#Txrw3`
- `7$&4sag$vQ8yvNr8XXEhErNQj!`
- ```Rf|\UY`GlDiE5mQxw```
- `ld8mxthb9007cswkesuo12uj63no`
- `Mb38jV@4kShP*WsfhS$rk2cygt7wkv`
- `UhMvdrt7FcA4sI4T!7!f6Yc*0`
- ```m&sw_?J=[@/~`'*k'KZ0uY0cp3~(Qk;F```

---

## Commercial Extensions
| Name | Version | Who purchased? | Login details for vendor |
|-|-|-|-|
