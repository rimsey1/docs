---
title: Asana
sidebar: cyclr_sidebar
permalink: asana-new
tags: [connector]
---
{::options parse_block_html="true" /}

<section class="authentication">
## Authentication

| Type      | OAUth2|
| OAuth2 type| AuthorisationCode |
| Authorize URL | https://app.asana.com/-/oauth_authorize |
| Access Token | https://app.asana.com/-/oauth_token |
{: .table .vheader}
</section>

<section class="required">
## Partner Setup

<div class="section-content">
* `Service Domain` : defined in your Cyclr console under **Settings** > **General Settings** > **Service Domain**.
* `Client ID` : see Application Setup.
* `Client Secret`: see Application Setup.
</div>
</section>
### Application Setup

1. Navigate to your **Asana Account Settings** dialog.
2. Select the **Apps** tab, and **Add New Application**.
3. Enter the **App Name**  - a name for your new application.
4. Enter the **App URL** - the url of your company.
5. Enter the **Redirect URL** - https://``Your Service Domain``/connector/callback.
6. Complete the app creation.
7. The  `Client ID` and `Client Secret` are displayed in the **Details** view. Note these for your Asana connector setup.

## Cyclr Setup

*   Go to your **Cyclr Console**.
*   Select the **Connectors** menu.
*   Select **Connector Library**.
*   Find the **Asana** Connector.
*   Select the **Setup** button.

Enter the required values:

* **Client ID**
* **Client Secret**

### Test Connector

Install Asana in one of your Cyclr accounts and execute one or more methods to view the returned data.