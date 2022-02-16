---
title: 3DCart
sidebar: cyclr_sidebar
permalink: 3dcart-new
tags: [connector]
---

## Authentication

| Type      | OAUth2|
| OAuth2 type| AuthorisationCode |
| API Key Header | Authorization |
| Authorize URL | {%raw%} https://apirest.3dcart.com/oauth/authorize?store_url={{StoreURL}}&#124;exclude:scope,display,immediate {% endraw %}|
| Access Token | https://apirest.3dcart.com/oauth/token |

## Partner Setup

Required:
* `Service Domain` : defined in your Cyclr console under **Settings** > **General Settings** > **Service Domain**.
* `IP Address`: see Server Details.
* `Public Key` : see Application Setup.
* `Client ID` : see Application Setup.
* `Secret Key`: see Application Setup.

### Server Details

| Server | URL | IP Address |
| --- | --- | --- 
| US (North Virginia) | my.cyclr.com | 52.22.119.215 |
| UK (London) | my.cyclr.uk | 52.56.244.97 |
| EU (Frankfurt) | eu.cyclr.com | 18.185.231.228 |

### Application Setup

1. [Login ](https://devportal.3dcart.com/login.asp) to your 3DCart Developer Account.
2. Select **Add New**.
3. Enter a name and select **Next**.
4. On your **Portal Development Dashboard** enter the **callback URL** - https://``Your Service Domain``/connector/callback.
5. Enter the server `IP Address`.
6. Select the **Permissions**.
7. Set your Application scopes - **Contacts** and **Orders**.
8. Select **Save**.
9. Note the `Public Key` ,  `Client ID` and `Secret Key`.

Test the application at this stage to confirm that it works with your 3DCart Store.

## Cyclr Setup

*   Go to your **Cyclr Console**.
*   Select the **Connectors** menu.
*   Select **Connector Library**.
*   Find the **3DCart** Connector.
*   Select the **Setup** button.

Enter the required values:
* **Client ID**
* **Client Secret**

You are prompted to log in to your Secure Store.

### Test Connector

Install 3DCart in one of your Cyclr accounts and execute one or more methods to view the returned data.