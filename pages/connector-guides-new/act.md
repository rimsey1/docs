---
title: Act!
sidebar: cyclr_sidebar
permalink: act-new
tags: [connector]
---

## Authentication

| Type      | Basic |

## Partner Setup
Required:
* `Username` : your Act! username.
* `Password`: your Act! password.
* `Database Name` : see Application Setup.
* `Act Domain` : see Application Setup.
* `Secret Key`: see Application Setup. 

### Application Setup

* Get your `Database Name`: in your Act! console, select your **username** and then **User Management**.
* Get your `Act Domain` :
  * **Cloud** : Enter your Act address, substitute api for app to api. 
  ```
  Act url: appeu.act.com
  Act url with api substition: apieu.act.com
  ```
  
  * **Self-Hosted** : Enter your instance domain,  `Database Name` with the suffix “-api”.
  ```
  url pattern:  {Act Domain Name}.com/{Act Database Name}-api
  enter: appeu.act.com/actdb-api
  ```
 