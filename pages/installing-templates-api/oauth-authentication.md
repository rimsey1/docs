---
title: OAuth Authentication
sidebar: cyclr_sidebar
permalink: oauth-authentication
tags: [installing]
---

**_For connectors that require your user to be taken through an OAuth flow._**

Connectors using OAuth require that the user goes through a webflow where they are sent to the third party application to sign in and grant access to Cyclr.

You'll need to create an Account Sign-In Token for a User to access the account.  The `Token` is only valid for a **single use** and will be active for 5 minutes, as indicated by the `ExpiresAtUtc` value in the response.

Request:

````http
POST  /v1.0/accounts/{Account ID}/signintoken
Content-Type: application/json
Authorization: Bearer 0000000000000000000000000000000000000000000000000000000000000000

{
    "Username": "example_user"
}
````

Response:

````json
{
    "Token": "ABCD12340000000000000=",
    "ExpiresAtUtc": "2017-12-08T11:02:48.7436471Z"
}
````

The user should then be sent here in their browser:

`https://{Partner Service Domain}/connectorauth/updateaccountconnectoroauth?id={Account Connector ID}&token={Account Sign-In Token}&targetOrigin=...`

For example: 
```
https://app-h.cyclr.com/connectorauth/updateaccountconnectoroauth?id=1234&token=ABCD12340000000000000=&targetOrigin=https://yourapplication.com/complete-page
```

The following query string parameters can be included:

| Parameter | Description | Example |
| --- | --- | --- |
| **token** | The account sign-in token generated above | ABCD12340000000000000= |
| **targetOrigin** | Required.  Either the origin of another browser window for the JavaScript callback event to be dispatched to, or a URL to redirect the user to. Used after the OAuth authentication is complete. | <span>https://partner.cyclr.com/connectors</span> |
| **callbackMessage** | Callback message to be sent by JavaScript postMessage to the parent window. Don’t include if using a redirect for `targetOrigin`. | done |

*You should URL encode all parameter values.*

Cyclr redirects the user to the appropriate sign in page of the target application, captures the OAuth tokens generated by that app, and stores them internally. Token refresh is handled automatically when required later.

On completion, the user will either be redirected to the **targetOrigin** if **callbackMessage** was left blank, or the JavaScript message specified by the **callbackMessage** will be posted to the parent window to notify the host app that the authentication flow has completed.  You can then take appropriate action in your system.

To handle the **callbackMessage**, your system's webpage should use `window.addEventListener()` to listen for messages which Cyclr will send using `window.postMessage()`.  More information on using this methodology can be found on the [Mozilla Developer Network's Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/Window/postMessage).

### Providing Client ID and Client Secret Values

Typically, systems using OAuth allow you to create a single App which you can use with Cyclr to access all of your customer's accounts.  Some systems however, require the use of separate Apps for each customer.  The correct setup should be described in each Connector's Cyclr Connector Guide.

For systems that allow a single App for all customers, you should set the Client ID and Client Secret values of that App in your Cyclr Console's Application Connector Library entry.

For Connectors that require the Client ID and Client Secret values to be provided separately for each Account Connector, or if you have chosen to provide them for each, add the following (using these exact names) as [Account Connector Properties](./authenticate-account-connector#account-connector-properties):

* `ClientId`
* `ClientSecret`


### Providing Complete Authentication for the Connector

If your own Cyclr Partner Connector (a Connector that works against your own system's API) uses OAuth, you'll perhaps wish to provide all the authentication details yourself, rather than involve the user.  This can be done through a LAUNCH or Marketplace call using the `PartnerConnector` property, or by a separate Cyclr API call.

To do this you must provide all the values the Connector requires to work with the API.

That may simply be by providing `ClientId` and `ClientSecret` as [mentioned above](./oauth-authentication#providing-client-id-and-client-secret-values).  It may also require [Account Connector Properties](./authenticate-account-connector#account-connector-properties) and perhaps an **AuthValue** containing Access and Refresh Tokens and details.  See below for more details on the AuthValue.

### AuthValue Property

Depending on how an API authenticates, you can provide a JSON object containing the Access and Refresh Token details as follows:

````json
{
	"AccessToken": "XXXXXXXXXX",
	"RefreshToken": "XXXXXXXXXX",
	"Expires": "2021-10-01T00:00:00Z",
	"RefreshExpires": "2022-10-01T00:00:00Z"
}
````

That JSON object should then be serialized - e.g. by using the standard Javascript ```JSON.stringify()``` function - then used as the **AuthValue** property of an Account Connector.

That would look like this in an API call:

````json
"AuthValue": "{\"AccessToken\":\"XXXXXXXXXX\",\"RefreshToken\":\"XXXXXXXXXX\",\"Expires\":\"2021-10-01T00:00:00Z\",\"RefreshExpires\":\"2022-10-01T00:00:00Z\"}"
````

Or, if other details have been provided that will enable Cyclr to obtain those details itself, you can simply set it as an empty JSON object and the next time Cyclr attempts to call a Method on the Connector, it will automatically attempt to authenticate and retrieve this information:

````json
"AuthValue": "{}"
````


[Step Setup](./step-set-up)  
[API Key Authentication](./api-key-authentication)  
[HTTP Basic Authentication](./basic-authentication)
