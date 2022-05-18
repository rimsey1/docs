---
title: Wait All Steps
sidebar: cyclr_sidebar
permalink: wait-all
tags: [builder-tools]
---

Wait All steps wait for all of the other steps in the cycle to complete execution. This is particularly useful when the Collection Splitting setting is turned on in your cycle. Wait All will continue to run its next step after all of the individual transactions have finished.

![](./images/wait-all-example.png)

In the example above, contacts from Salesforce will be split into individual transactions. Each transaction contains one contact and will be created in either List A or B in MailChimp depending on the decision step result.

After all contacts have been processed, the step following Wait All will be triggered. This will post a message on Slack to notify users that the data import has finished.

### Notes on use

* Try to avoid setting your cycle to run too frequently as the Wait All step only continues once there are no in progress transactions running on the cycle, regardless of when they were started.
* Wait All steps consider the first step in a cycle to be important as they typically retrieve the data that will be processed.  If the first step encounters an error, then execution won't continue after the Wait All step.
