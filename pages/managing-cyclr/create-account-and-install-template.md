---
title: Create an Account and Install a Template
sidebar: cyclr_sidebar
permalink: create-account-and-install-template
tags: [Create an Account and Install a Template]
---


This document describes how to Create an Account and Install a Template into it, using API calls.

Note: Throughout this document, the domain used in the example requests is ```api.cyclr.com```.

If you are on the UK instance, this should be replaced with ```api.cyclr.uk```, and for the EU, ```api.eu.cyclr.com```.

## 1. Create Account

```curl
curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' -d  '{ \ 
 "Id": "(Optional) The External Account ID you would like for this account", \  "Name": "Account Name", \ 
 "Description": "(Optional) Account Description", \ 
 "Timezone": "(Optional) Timezone for the account, IANA time zone database format.", \  }' 'https://api.cyclr.com/v1.0/accounts'
 ```

## 2. Install template into new account

```curl
curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' -- header 'X-Cyclr-Account: ACCOUNT ID FROM PREVIOUS STEP' -d '{ \  }' 'https://api.cyclr.com/v1.0/templates/TEMPLATE-ID/install'
```

Depending on the template being installed, there may be more to specify in this call, but this  is the minimum.

### 3. Authenticate connector (OAuth)

#### 3a. Get Sign-in Token

```curl
curl -X POST --header 'Content-Type: application/json' --header 'Accept:  application/json' -d '{ \
"Username": "string" \ 
 }' 'https://api.cyclr.com/v1.0/accounts/ACCOUNT ID FROM STEP 1/signintoken'
```

#### 3b. List Account Connectors

```curl
curl -X GET --header 'Accept: application/json' --header 'X-Cyclr-Account: ACCOUNT ID FROM PREVIOUS STEP'  
'https://api.cyclr.com/v1.0/account/connectors'
```

#### 3c. Update Connector Auth

```curl
curl --request POST \
  --url 'https://YOUR-SERVICE-DOMAIN/connectorauth/updateaccountconnectoroauth?id=1234&token=TOKEN-FROM-STEP-3a&targetOrigin=https://www.cyclr.com'
```

Your service domain can be found by visiting General Settings in your Cyclr console.  It generally has a format matching one of the following:

* mycompany-h.cyclr.com
* mycompany-h.eu.cyclr.com
* mycompany-h.cyclr.uk

``targetOrigin`` should be either the origin of another browser window for the  JavaScript callback event to be dispatched to, or a URL to redirect the user to.

### 4. Make call to a Connector Method 

#### 4a. List Connector Methods 

```curl
curl -X GET --header 'Accept: application/json' --header 'X-Cyclr-Account: Account  ID from Previous Step' 'https://api.cyclr.com/v1.0/connectors/NAME OF  CONNECTOR/methods'
```

#### 4b. Call Method

```curl
 curl -X POST --header 'Content-Type: application/json' --header 'Accept:  application/json' --header 'X-Cyclr-Account: Account ID from Previous Step' -d '{ \  "Parameters": {}, \ 
 "Fields": {}, \ 
 "Mergefields": {} \ 
 }' 'https://api.cyclr.com/v1.0/account/connectors/Account Connector ID from Step  3B/methods/Method ID'
```

### 5. Start Cycle

```curl
curl -X PUT --header 'Content-Type: application/json' --header 'Accept: application/json' -- header 'X-Cyclr-Account: Account ID' -d '{ \ 
 "StartTime": "2021-12-07T09:17:50.888Z", \ 
 "Interval": 0, \ 
 "RunOnce": true \ 
 }' 'https://api.cyclr.com/v1.0/cycles/Cycle ID/activate'
```
