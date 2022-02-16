---
title: Capsule v2
sidebar: cyclr_sidebar
permalink: capsule-new
tags: [connector]
---

## Authentication

| Type      | OAUth2|
| OAuth2 type| AuthorisationCode |
| Authorize URL | {% raw %}https://api.capsulecrm.com/oauth/authorise?scope=read+write {% endraw %}|
| Access Token | https://api.capsulecrm.com/oauth/token |

## Partner Setup

Required:
* `Service Domain` : defined in your Cyclr console under **Settings** > **General Settings** > **Service Domain**.
* `Client ID` : see Application Setup.
* `Client Secret`: see Application Setup.
* `Authorise URL`: see Authentication.
* `Access Token`: see Authentication.

### Application Setup

1. Register a free Capsule account or log into your existing account.
2. Create a new application at [https://developer.capsulecrm.com/clients/new ](https://developer.capsulecrm.com/clients/new)
3. Enter the **NAME** - your application name.
4. Enter the **URL** - your Cyclr service domain.
5. Enter the **REDIRECT URL** - https://``Your Service Domain``/connector/callback.
6. Select the **APPLICATION TYPE** Web Application radio button.
7. Complete any other fields in the form and select **Save**.
8. The  `Client ID` and `Client Secret` are displayed. Note these for your Capsule v2 connector setup.

Visit the <a href="https://developer.capsulecrm.com/v2/overview/authentication#oauth-2">Capsule OAuth 2 documentation</a> for more information.

## Cyclr Setup
*   Go to your **Cyclr Console**.
*   Select the **Connectors** menu.
*   Select **Connector Library**.
*   Find the **Capsule v2** Connector.
*   Select the **Setup** button.

Enter the required values:

* `Client ID`
* `Client Secret`
* `Authorise URL`
* `Access Token`

### Test Connector

Install Capsule v2 in one of your Cyclr accounts and execute one or more methods to view the returned data.


## API Integration

Capsule v2 connector requires your end users to sign into Capsule and grant Cyclr access to their account.

To do this, call _/UpdateAccountConnectorOAuth_ with a one-time sign-in token.