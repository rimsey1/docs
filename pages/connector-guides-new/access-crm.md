---
title: Access CRM
sidebar: cyclr_sidebar
permalink: access-crm-new
tags: [connector]
---

## Authentication

| Type      | API Key |
| API Key Header | apiKey |

## Partner Setup

Required:
* `Service Domain` : defined in your Cyclr console under **Settings** > **General Settings** > **Service Domain**.
* `API Key` : see Application Setup.
* `Integrator Key`: see Application Setup. 

### Application Setup

Access supplies the `API Key` and `Integrator Key`. Contact your Access account manager to request your credentials.

## Cyclr Setup

*   Go to your **Cyclr Console**.
*   Select the **Connectors** menu.
*   Select **Connector Library**.
*   Find the Access CRM Connector.
*   Select the **Setup** button.
*   Enter your  `Integrator Key` and select **Next**.
*   Enter your  `API Key` and select **Next**.

## User Guide

### Calculated Fields
To add calculated fields to the response mappings of any methods,  add the suffix "\_calc" (underscore calc) to the Field Location's name. 

If the calculated field name does not include "\_calc" the API will throw an error, as your calculated field does not exist on the object definition.

#### Examples

A field location of **myCalculatedField** will result in a failed request.

A field location of **myCalculatedField_calc** will result in a successful request.