# ThaleMine Webservices

These are [Araport](http://www.araport.org) API wrappers around various [Thalemine Endpoints](https://www.araport.org/api-explorer/thalemine).

# create_thalemine_list: Create a list of specified type in ThaleMine for the current user
```
>>> import services.create_thalemine_list.main as main
>>> main.search({'name':'esf-test-list', 'type':'Gene', 'data':'AT1G01040 AT1G01050 AT1G01060'})
{
  "listName": "esf-test-list",
  "error": null,
  "executionTime": "2015.09.14 17:48::08",
  "wasSuccessful": true,
  "listSize": 3,
  "unmatchedIdentifiers": [
    "AT1G01060",
    "AT1G01040",
    "AT1G01050"
  ],
  "type": "Gene",
  "statusCode": 200
}

```
The list function returns all of the lists for which the current user has access.
```
>>> import services.create_thalemine_list.main as main
>>> main.list({})
    {
      "status": "CURRENT",
      "description": "Cytokinin responsive genes reported by Bhargava et al. (2013).",
      "title": "Demo - Cytokinin responsive genes",
      "timestamp": 1435677674323,
      "tags": [],
      "dateCreated": "2015-06-30T11:21:14-0400",
      "authorized": false,
      "size": 226,
      "type": "Gene",
      "name": "Demo - Cytokinin responsive genes"
    }
    ---
    {
      "status": "CURRENT",
      "description": "",
      "title": "Demo - Genes with receiver domain",
      "timestamp": 1435672876925,
      "tags": [],
      "dateCreated": "2015-06-30T10:01:16-0400",
      "authorized": false,
      "size": 41,
      "type": "Gene",
      "name": "Demo - Genes with receiver domain"
    }
    ---
    {
      "status": "CURRENT",
      "description": "",
      "title": "Demo - Photosynthesis",
      "timestamp": 1435673157785,
      "tags": [],
      "dateCreated": "2015-06-30T10:05:57-0400",
      "authorized": false,
      "size": 154,
      "type": "Gene",
      "name": "Demo - Photosynthesis"
    }
    ---
    {
      "status": "CURRENT",
      "description": "",
      "title": "Demo - Sucrose Transporters List",
      "timestamp": 1409084442353,
      "tags": [],
      "dateCreated": "2014-08-26T16:20:42-0400",
      "authorized": false,
      "size": 9,
      "type": "Gene",
      "name": "Demo - Sucrose Transporters List"
    }
    ---
    {
      "status": "CURRENT",
      "description": null,
      "title": "Gene list for Arabidopsis thaliana - Thu Feb 19 2015",
      "timestamp": 1424368813554,
      "tags": [],
      "dateCreated": "2015-02-19T13:00:13-0500",
      "authorized": true,
      "size": 6,
      "type": "Gene",
      "name": "Gene list for Arabidopsis thaliana - Thu Feb 19 2015"
    }
    ---
    {
      "status": "CURRENT",
      "description": "",
      "title": "Gene list for all organisms 17 Jul 2014 13.44",
      "timestamp": 1405619064668,
      "tags": [],
      "dateCreated": "2014-07-17T13:44:24-0400",
      "authorized": true,
      "size": 1,
      "type": "Gene",
      "name": "Gene list for all organisms 17 Jul 2014 13.44"
    }
    ---
    {
      "status": "CURRENT",
      "description": null,
      "title": "STM coexpression - Wed Mar 04 2015",
      "timestamp": 1425510259009,
      "tags": [],
      "dateCreated": "2015-03-04T18:04:19-0500",
      "authorized": true,
      "size": 31,
      "type": "Gene",
      "name": "STM coexpression - Wed Mar 04 2015"
    }
    ---
    {
      "status": "CURRENT",
      "description": null,
      "title": "Synonym gene list",
      "timestamp": 1424369188184,
      "tags": [],
      "dateCreated": "2015-02-19T13:06:28-0500",
      "authorized": true,
      "size": 22,
      "type": "Gene",
      "name": "Synonym gene list"
    }
    ---
```

# get_thalemine_user: Get information about the current ThaleMine user
```
Both the list and search endpoints return the same data.

>>> import services.get_thalemine_user.main as main
>>> main.search({})
{
  "username": "ARAPORT:eriksf",
  "preferences": {
    "alias": "Erik Ferlanti",
    "aka": "Erik Ferlanti",
    "email": "erik@jcvi.org"
  }
}
```
