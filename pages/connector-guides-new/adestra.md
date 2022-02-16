---
title: Upland Adestra
sidebar: cyclr_sidebar
permalink: adestra-new
tags: [connector]

---
## Authentication

| Type      | Basic |
| Authentication Description | Prefix username with lower-case account name and a dot (e.g. my_account.username). |

## Partner Setup
Required:
* `Account` : see Application Setup.
* `Username` : see Application Setup.
* `Password`: see Application Setup. 



### Application Setup

1. Set up a user: see the Adestra [documentation](https://app.adestra.com/doc/page/current/index/admin/users/users).
2.
3.
4.
5.

## Cyclr Setup

*   Go to your **Cyclr Console**.
*   Select the **Connectors** menu.
*   Select **Connector Library**.
*   Find the **Upland Adestra** Connector.
*   Select the **Setup** button.

Enter the required values:
* **Client ID**
* **Client Secret**


## User Guide

### Tables
The Adestra system has the concept of tables. Download table definitions from the Adestra portal or via the connector table methods.

Some method calls require a `table ID`. Call the **List Core Tables**, and **List Data Tables** methods to find the `table ID`.

The **Contacts** category methods include the default ID and Email.

Add custom fields as specified on the method for the required table. 

