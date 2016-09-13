PPSA
---

Prezi's Presentation Search API

Description
---
An API which serves all presentation records in our Database.

Usage
---
Using PPA is very simple.

Endpoint for search:

     http://hasanagha.pythonanywhere.com/search/
     Methods allowed: [POST]
     Request Type: AJAX
     Mandatory Headers: ['X-Requested-With': 'XMLHttpRequest']


Admin URL to add/edit records:

    http://hasanagha.pythonanywhere.com/admin/
    username: hasan
    password: hasan


Technical Babble
---
Uses `Django 1.9.7` with `SQLite3` as a database.

