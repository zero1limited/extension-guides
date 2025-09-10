# Systems Network 

[TOC]

Concentrating on the detailed network setup and infrastructure for the WRH (West Road House) network and access via VPN 

## VPN Access

VPN access is typically needed for
 - Secure access to WIKI.zero1.co.uk
 - Access to client Magento Admin Panels which are IP restricted

Our new VPN system is called Outine, application workstation instructions are below.

```
Use this server to safely access the Open Internet:

1) Download and install the Outline app for your device:

– iOS: https://itunes.apple.com/app/outline-app/id1356177741
– MacOS: https://itunes.apple.com/app/outline-app/id1356178125
– Windows: https://s3.amazonaws.com/outline-releases/client/windows/stable/Outline-Client.exe
– Linux: https://s3.amazonaws.com/outline-releases/client/linux/stable/Outline-Client.AppImage
– Android: https://play.google.com/store/apps/details?id=org.outline.android.client
- Android alternative link: https://s3.amazonaws.com/outline-releases/client/android/stable/Outline-Client.apk

2) You will receive an access key that starts with ss://. Once you receive the key, copy it.

3) Open the Outline client app. If your access key is auto-detected, tap 'Connect' and proceed. If your access key is not auto-detected, paste it in the field, then tap 'Connect' and proceed.

You're ready to use the Open Internet! To make sure that you've successfully connected to the server, try searching for 'what is my IP' on Google Search. The IP address shown in Google should match the IP address in the Outline client.

Learn more about Outline here: https://getoutline.org/
```

Access Key is 
```
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo3b05ZdDFFTk4xc2E2ZHBHUGUxQ1dx@213.171.203.23:54372/?outline=1
```

## WAN Network IPs

Currently we have a range of IP addresses but the primary IP used for outbound traffic is `213.105.127.200`




## Key Network Devices

- Firewall
- Router/WAN/Modem


### PBX



#### Setup


##### IVR / Receptionist
Use https://elevenlabs.io/app/speech-synthesis or https://cloud.google.com/text-to-speech
Convert mp3 to WAV - Arron has a tool but any will do
