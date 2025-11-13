# Log Monitoring and Analytics

## General notes
App: https://app-uk.logz.io/#/dashboard/home

Have invited:
- Arron
- Callum
- Brad
- Craig
(doesn't appear to be a charge per user)


Best filter so far: `Client:SDS AND NOT level:(INFO OR DEBUG)`


## Setup / Installation

1. [zero1/enhanced-logging](https://github.com/zero1limited/magento2-enhanced-logging/tree/master?tab=readme-ov-file#installation) needs installing and deploying to live.
  **N.B* please reas the installation instructions and ensure the new `di.xml` is added to source control.
2. Verify file exist: `/home/magento/htdocs/var/log/logstash.log`
3. Log into the container via the MDOQ bastion (stay as root when you're in the container)
  ```
  cd /root
  apt update -qq && apt install -y screen

  # download and extract filebeat
  curl -L -O https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-8.17.1-linux-x86_64.tar.gz
  tar xzvf filebeat-8.17.1-linux-x86_64.tar.gz

  # install logz.io SSL certs
  curl https://raw.githubusercontent.com/logzio/public-certificates/master/AAACertificateServices.crt --create-dirs -o /etc/pki/tls/certs/COMODORSADomainValidationSecureServerCA.crt

  # configure file beat
  cd filebeat-8.17.1-linux-x86_64
  mv filebeat.yml filebeat.yml.orig
  nano filebeat.yml; #(see content below)

  # check config
  ./filebeat test config -c filebeat.yml

  # run it
  screen -R
  ./filebeat run -c filebeat.yml -v
  # dettach from screen
  Ctrl + A, Ctrl + D

  # should be good to exit
  ```
4. Wait for logs to appear took ~10mins last time for first logs to come through.


`filebeat.yml`
```yml
############################# Filebeat #####################################

filebeat.inputs:

- type: log
  paths:
    - /home/magento/htdocs/var/log/logstash.log
  fields:
    logzio_codec: json
    token: zvNgUvqnQiKWSmNUdCndZrTkqDeCfTcI
    type: magento
    Environment: Production
    Client: {CLIENT}
  fields_under_root: true
  encoding: utf-8
  ignore_older: 3h

#For version 6.x and lower
#filebeat.registry_file: /var/lib/filebeat/registry

#For version 7 and higher
filebeat.registry.path: /var/lib/filebeat

#The following processors are to ensure compatibility with version 7
processors:
- rename:
    fields:
     - from: "agent"
       to: "beat_agent"
    ignore_missing: true
- rename:
    fields:
     - from: "log.file.path"
       to: "source"
    ignore_missing: true

############################# Output ##########################################

output:
  logstash:
    hosts: ["listener-uk.logz.io:5015"]
    ssl:
      certificate_authorities: ['/etc/pki/tls/certs/COMODORSADomainValidationSecureServerCA.crt']
```
**N.B** replace `{CLIENT}` with the name of the client ie `SDS`