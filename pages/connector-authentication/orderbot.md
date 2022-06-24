---
title: Orderbot Authentication
sidebar: cyclr_sidebar
permalink: orderbot-connector
tags: [connector]
---

<a name="orderbot-setup"></a>

# Orderbot setup

You need your Orderbot `username` and `password` to setup the Orderbot connector in Cyclr.

<a name="cyclr-setup"></a>

# Cyclr setup

### Account setup

You will be asked for the following values when installing the Orderbot connector within an account:

-   **Username**: The Orderbot account username.
-   **Password**: The Orderbot account password.

Your Orderbot connector is now set up! You can test it by executing one of the methods to confirm it can return some data.

<a name="additional-information"></a>

# Additional information

### Mapping custom fields

Methods in the `Products > Custom Fields` category dynamically return custom field data dependant on how custom fields are set up in the Orderbot UI. To map these fields within Cyclr:

1. Go to the **Settings** page of the Orderbot connector:
    - For template connectors: **Cyclr Console** > **Templates** > **Template Connectors** > **Orderbot** > **Edit Connector**.
    - For connectors within a cycle: **Cycle Builder** > **Application Connectors** > **Orderbot** > **Settings**.
2. Under the **Methods and Fields** heading, expand the **Products** and then **Custom Fields** categories.
3. Expand the method you want to map custom fields for - either **Get Product (Custom Fields)** or **List Products (Custom Fields)**.
4. Select the pink **+** icon.
5. Enter the following:
    - **Field Location**: The custom field name set within Orderbot. For get methods, this should just be entered as the field name. For list methods, this should be entered as the field name prepended with `[].`. For example: If the custom field in Orderbot is named `expLicCode`, then the field location for get methods should be set to `expLicCode` and for list methods should be set to `[].expLicCode`.
    - **Display Name**: The display name to use within Cyclr.
    - **Description**: The description to use within Cyclr.
    - **Data Type**: The data type of the custom field set within Orderbot.
6. Select **Create**.
7. Steps in a cycle can now have the custom field mapped.
