---
title: Mailchimp
sidebar: cyclr_sidebar
permalink: mailchimp-new
tags: [connector]
---

## Authentication

| Type      | OAUth2|
| OAuth2 type| AuthorisationCode |
| Authorize URL | https://login.mailchimp.com/oauth2/authorize |
| Access Token | https://login.mailchimp.com/oauth2/token |

## Partner Setup

Required:
* `Service Domain` : defined in your Cyclr console under **Settings** > **General Settings** > **Service Domain**.
* `Client ID` : see Application Setup.
* `Client Secret`: see Application Setup.

### Application Setup

1. Navigate to the [Registered Apps](https://us1.admin.mailchimp.com/account/oauth2/) page in your Mailchimp account.
2. Select the [Register An App](https://us19.admin.mailchimp.com/account/oauth2/client/) link.
3. Fill out the **Register An App** form.
4. Provide the  **Redirect URI** : https://``Your Service Domain``/connector/callback.
5. Select **Create**.
6. The  `Client ID` and `Client Secret` are displayed. Note these for your Mailchimp connector setup.

Visit the <a href="https://mailchimp.com/developer/guides/access-user-data-with-oauth-2/#register-your-application">Mailchimp official documentation</a> for more information:

## Cyclr Setup

*   Go to your **Cyclr Console**.
*   Select the **Connectors** menu.
*   Select **Connector Library**.
*   Find the **Mailchimp** Connector.
*   Select the **Setup** button.

Enter the required values:

* **Client ID**
* **Client Secret**

### Test Connector

Install Mailchimp in one of your Cyclr accounts and execute one or more methods to view the returned data.