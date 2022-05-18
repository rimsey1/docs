---
title: Logic Tools
sidebar: cyclr_sidebar
permalink: logic-tools
tags: [templates]
menus:
  templates:
    title: Logic Tools
    url: /logic-tools
    weight: 7
---

## Introduction

Cyclr provides 4 logic tools that can be used in Integration Cycles.  These are:

| Tool | Purpose |
| --- | --- |
| Decisions | Allows data to be split to follow different paths through the integration. |
| Delays | Allows a pause to be added to the flow. |
| Wait Until | Allows you to hold processing until a specific data/time has been reached. |
| Wait All | Allows you to add closing steps to a process when the integraton has been processing an array of transations in parallel. |

## Decisions

Decision steps can split the data in your cycle down a true or false branch.

![](./images/decision-example.png)

### Setting up a Decision step

Your cycle must contain at least one Get (green) or Webhook (grey) step so you have some data to work with.

Click and drag a Decision Step into your cycle and connect it where you wish to split the data, then click its cog Step Setup button.

![](./images/decision.png)

Decisions work by comparing a "Left Operand" to a "Right Operand"; in other words, it looks for a value in your data and compares it - using a condition you specify - to another value.

From within the Decision Step's Step Setup:

*   Choose a previous step and one of its fields; this is your Left Operand.
*   Choose a Condition, e.g. _Exists, Not Exists, Equals, Not Equals_.
*   Choose your Right Operand. This can the value of a previous step's field or you can type in a value.

The result of the screenshot example is that contacts with the last name of “Smith” are routed down the true branch; all other contacts will go down the false branch.

To create more advanced logic, you can chain multiple Decision steps together.

### IMPORTANT NOTE

**Decision steps only filter records from the steps to which they refer.  Take the example illustrated below:**

![](./images/example-decision.png)

* Step 3 has fields mapped from Step 1 and Step 2.
* Only Step 2's results are being filtered by a decision step.
* Any data from Step 1 will always be mapped, regardless of the results of Step 2.

## Delays

Delay steps added to a cycle, will execute without any scheduled delays. Connecting a Delay between two steps will allow you to set a fixed time that Cyclr should wait before it executes the next step.

![](./images/delay.png)

Click-drag a Delay from the logic section of the builder’s right sidebar.

Once the Delay s on the build canvas, connect it between two steps and click the setup cog in order to set the length of the delay.

You can also pause for a period based on a date field in your data. For example, when a contact’s subscription is due for renewal. To do this, you should use a Wait Until step.

## Wait Until

You can use a Wait Until step in two ways.

### Wait for a specific date

For example, the date of an event or webinar you are running.

![](./images/wait-until-fixed-date.png)

Select the Type a Value option and choose a date/time using the calendar and dropdown combos.

### Wait until dynamic date in your data

For example, a contact’s subscription renewal date.

![](./images/wait-until-dynamic-date.png)

Select a step from the first dropdown, then a field from the second. The field should be a date.

## Wait All

Wait All steps wait for all of the other steps in the cycle to complete execution. This is particularly useful when the Collection Splitting setting is turned on in your cycle. Wait All will continue to run its next step after all of the individual transactions have finished.

![](./images/wait-all-example.png)

In the example above, contacts from Salesforce will be split into individual transactions. Each transaction contains one contact and will be created in either List A or B in MailChimp depending on the decision step result.

After all contacts have been processed, the step following Wait All will be triggered. This will post a message on Slack to notify users that the data import has finished.

### Notes on use

* Try to avoid setting your cycle to run too frequently as the Wait All step only continues once there are no in progress transactions running on the cycle, regardless of when they were started.
* Wait All steps consider the first step in a cycle to be important as they typically retrieve the data that will be processed.  If the first step encounters an error, then execution won't continue after the Wait All step.
