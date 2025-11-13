# Server Utilization Report
This recommendation is applicable for all M2 sites, that are on MDOQ dedicated hosting (see [determining if someone is using dedicated hosting](#check-if-on-dedicated-hosting).

## Pitch
The utilization of the server behind your Magento site is often something that can be overlooked until it becomes an issue. (Usually an urgent one)
We recommend carrying out a server utilization report at least quarterly, this report will identify:
- Memory usage
- CPU usage
- Storage usage
Gathering these metrics will allow us to provide you with some insights into the heath of your server and spot potentially issues before they become a problem.

## Process
### Check if on dedicated hosting
1. log into MDOQ and navigate to the client you would like to check
2. get the ID of their production instance
3. Visit https://api.mdoq.io/v1/instance/id/INSTANCE_ID
4. check that "platform" is "Magento 2"
5. check that "type" is "production_large" or "production_xlarge"

Video: https://drive.google.com/file/d/1wmDtO33amNWNfBzqT5Glno9S6wDLsCzj/view

### Who
Anyone with access to Grafana
(If you don't have access to Grafana, please speak to Adam who can create you an account)

### Setup
This task requires no setup.

### Instructions
See [here](https://docs.google.com/document/d/1mKgubDyImKR7khEZPXCpLZx4FZHFRFnnORMOjwzp8zY/edit?usp=sharing) for an example report.

1. Make a copy of [this report](https://docs.google.com/document/d/1lTUgl_PAPpDHGHLoDfiOQ7TLgQ58YEacyTBBWg5jZeM/edit?usp=sharing) 

2. Gather the base MDOQ domain for the site.
  This can be found by getting the link from the SSH helper.
  For example, if the link to the ssh helper is: https://web-ssh-8zk9wenshm-9752.07.mdoq.io/
  The base MDOQ domain would be 07.mdoq.io

3. Log into [Grafana](http://grafana.mdoq.io:9089/) and nvaivate to the dashboard for the domain.
Access Credentials:
Username: `firstline@mdoq.io`
Password: `s&9pVmDDL1*Qeq4*nvL9`

4. collect images for:
  - CPU Basic
  - Memory Basic
  - Disk Space Used Basic
  - I/O Usage Read/Write
  - Load
  For 30 and 90 days

5. Carry out a review using the pointers below. If the statement is true, add it to the analysis section on the template.

#### CPU Basic
- Blue bit averaging 0->25%: "Your servers CPU is handling the current load very well. There is room for growth, without affecting the performance of your site. Your server should be able to deal with short traffic bursts very well."
- Blue bit averaging 25->50%: "Your servers CPU is handling the current load well. There is room for growth, without effecting the performance of your site. Your server should be able to deal with short traffic bursts."
- Blue bit averaging 50->75%: "Your servers CPU is handling the current load. There is room for some growth, however if growth continues we would recommend a server upgrade. You may experience some degration of performance during spikes of traffic."
- Blue bit averaging 75->100%: "Your servers CPU is struggling to cope with the demmand, there is no room for growth. You will experience performance degragation during traffic spikes. We recommend you upgrade your server."
- Blue bit climbing?: "Your servers CPU usage has experienced growth over the last 30-90 days."

#### Memory Basic
- Yellow bit averaging 0->33%: "Your server has plenty of memory available. There is plenty of room for growth."
- Yellow bit averaging 33->66%: "Your server is using an optimal amount of memory. There is some room for growth. If growth continues you may need to upgrade your server."
- Yellow bit averaging 66->100%: "Your server is using the majority of its memory. There is little room for growth. We recommend upgrading your server, and/or carrying out an investigation on memory usage. This would identify if there is a memory leak (in which case we me may be able to free some up) or if you truely need this amount of memory (which would solidify the argument to upgrade)"
- Yellow bit climbing?: "Your servers memory has increased over the last 30-90 days."

#### Disk Space Used
- Are all lines under 75%?: "Your storage usage is good and well within the limits your server is able to handle."
- Any line higher than 75%?: "Your servers storage space is almost full. We recommend carrying out an investigation on storage space, this will allow us to identify if there is an issue that can be resolved, or if you need to look at upgrading your server."
- Any line climbing to the point it will likely reach 70% in the next 90 days: "It looks like your storage space may hit critical usage in the near future. We recommend carrying out an investigation into storage space. This will allow us to identify if there is an issue that can be resolved, or if you need to look at upgrading your server."

#### I/O Usage Read/Write
Nothing for here yet


#### System Load
For these statements you will need to workout what 100% load would be. This is based on the number of  cores available. At the top of the Grafana dashboard you should be able to see "CPU Cores" whatever this number is, is 100%.
Example:
CPU Cores: 8
33% load: 2.64 = (8 / 100) * 33
66% load: 5.28 = (8 / 100) * 66
100% load: 8

You will need to calculate these values before continuing.

- Is the blue line under 33% on average?: "Your server is handling the demands on it well. There is room for growth without experiencing a drop in performance."
- Is the blue line under 66% on average?: "Your server is handling the demands on it. There is some room for growth, though during traffic spikes you may experience a drop in performance."
- Is the blue line over 66% on average?: "Your server is struggling with the demands on it. There is no room for growth. During traffic spikes you will likely experience a drop in performance. If traffic is high enough the server may become unresponsive as it is too busy to handle additional requests. We recommend upgrading your server."
