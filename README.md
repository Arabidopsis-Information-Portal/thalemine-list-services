# ThaleMine Webservices

These are [Araport](http://www.araport.org) API wrappers around various [Thalemine Endpoints](https://www.araport.org/api-explorer/thalemine).

# create_thalemine_list: Create a list of specified type in ThaleMine for the current user
```
$ http POST "https://api.araport.org/community/v0.3/aip/create_thalemine_list_v1.0/access" Authorization:"Bearer: $TOKEN" "AT1G01040 AT1G01050 AT1G01060"
{
  "listName": "eriksf-test-list",
  "listSize": 3,
  "type": "Gene",
  "unmatchedIdentifiers": [
    "AT1G01040",
    "AT1G01050",
    "AT1G01060"
  ],
  "executionTime": "2015.09.29 16:27::13",
  "wasSuccessful": true,
  "error": null,
  "statusCode": 200
}
```

# add_to_thalemine_list: Add identifiers to a ThaleMine list for the current user
```
$ http POST "https://api.araport.org/community/v0.3/aip/add_to_thalemine_list_v1.0/access" Authorization:"Bearer: $TOKEN" "FT"
{
  "listName": "eriksf-test-list",
  "listSize": 4,
  "type": null,
  "unmatchedIdentifiers": [
    "FT"
  ],
  "executionTime": "2015.09.29 16:30::42",
  "wasSuccessful": true,
  "error": null,
  "statusCode": 200
}
```

# find_in_thalemine_list: Find object of specified type in the available lists of the current user
```
$ http "https://api.araport.org/community/v0.3/aip/find_in_thalemine_v1.0/access?publicId=AT1G01060&type=Gene" Authorization:"Bearer: $TOKEN"
{
  "lists": [
    {
      "timestamp": 1443126537363,
      "tags": [],
      "authorized": true,
      "title": "erik_test",
      "status": "CURRENT",
      "description": null,
      "name": "erik_test",
      "dateCreated": "2015-09-24T16:28:57-0400",
      "type": "Gene",
      "size": 4
    },
    {
      "timestamp": 1442944261017,
      "tags": [],
      "authorized": true,
      "title": "Genes_on_Chr1_between_29733_and_37349-2015-09-22T17_51_00.188Z",
      "status": "CURRENT",
      "description": null,
      "name": "Genes_on_Chr1_between_29733_and_37349-2015-09-22T17_51_00.188Z",
      "dateCreated": "2015-09-22T13:51:01-0400",
      "type": "Gene",
      "size": 3
    }
  ],
  "executionTime": "2015.09.29 16:11::16",
  "wasSuccessful": true,
  "error": null,
  "statusCode": 200
}
```

# get_thalemine_lists: Show all ThaleMine lists the current user can access
```
$ http "https://api.araport.org/community/v0.3/aip/get_thalemine_lists_v1.0/access" Authorization:"Bearer: $TOKEN"
{
  "lists": [
    {
      "timestamp": 1435677674323,
      "tags": [],
      "authorized": false,
      "title": "Demo - Cytokinin responsive genes",
      "status": "CURRENT",
      "description": "Cytokinin responsive genes reported by Bhargava et al. (2013).",
      "name": "Demo - Cytokinin responsive genes",
      "dateCreated": "2015-06-30T11:21:14-0400",
      "type": "Gene",
      "size": 226
    },
    {
      "timestamp": 1435672876925,
      "tags": [],
      "authorized": false,
      "title": "Demo - Genes with receiver domain",
      "status": "CURRENT",
      "description": "",
      "name": "Demo - Genes with receiver domain",
      "dateCreated": "2015-06-30T10:01:16-0400",
      "type": "Gene",
      "size": 41
    },
    {
      "timestamp": 1435673157785,
      "tags": [],
      "authorized": false,
      "title": "Demo - Photosynthesis",
      "status": "CURRENT",
      "description": "",
      "name": "Demo - Photosynthesis",
      "dateCreated": "2015-06-30T10:05:57-0400",
      "type": "Gene",
      "size": 154
    },
    {
      "timestamp": 1409084442353,
      "tags": [],
      "authorized": false,
      "title": "Demo - Sucrose Transporters List",
      "status": "CURRENT",
      "description": "",
      "name": "Demo - Sucrose Transporters List",
      "dateCreated": "2014-08-26T16:20:42-0400",
      "type": "Gene",
      "size": 9
    },
    {
      "timestamp": 1424368813554,
      "tags": [],
      "authorized": true,
      "title": "Gene list for Arabidopsis thaliana - Thu Feb 19 2015",
      "status": "CURRENT",
      "description": null,
      "name": "Gene list for Arabidopsis thaliana - Thu Feb 19 2015",
      "dateCreated": "2015-02-19T13:00:13-0500",
      "type": "Gene",
      "size": 6
    },
    {
      "timestamp": 1405619064668,
      "tags": [],
      "authorized": true,
      "title": "Gene list for all organisms 17 Jul 2014 13.44",
      "status": "CURRENT",
      "description": "",
      "name": "Gene list for all organisms 17 Jul 2014 13.44",
      "dateCreated": "2014-07-17T13:44:24-0400",
      "type": "Gene",
      "size": 1
    },
    {
      "timestamp": 1442944261017,
      "tags": [],
      "authorized": true,
      "title": "Genes_on_Chr1_between_29733_and_37349-2015-09-22T17_51_00.188Z",
      "status": "CURRENT",
      "description": null,
      "name": "Genes_on_Chr1_between_29733_and_37349-2015-09-22T17_51_00.188Z",
      "dateCreated": "2015-09-22T13:51:01-0400",
      "type": "Gene",
      "size": 3
    },
    {
      "timestamp": 1442943297250,
      "tags": [],
      "authorized": true,
      "title": "Genes_on_Chr5_between_1_and_200000-2015-09-22T17_34_56.428Z",
      "status": "CURRENT",
      "description": null,
      "name": "Genes_on_Chr5_between_1_and_200000-2015-09-22T17_34_56.428Z",
      "dateCreated": "2015-09-22T13:34:57-0400",
      "type": "Gene",
      "size": 59
    },
    {
      "timestamp": 1425510259009,
      "tags": [],
      "authorized": true,
      "title": "STM coexpression - Wed Mar 04 2015",
      "status": "CURRENT",
      "description": null,
      "name": "STM coexpression - Wed Mar 04 2015",
      "dateCreated": "2015-03-04T18:04:19-0500",
      "type": "Gene",
      "size": 31
    },
    {
      "timestamp": 1424369188184,
      "tags": [],
      "authorized": true,
      "title": "Synonym gene list",
      "status": "CURRENT",
      "description": null,
      "name": "Synonym gene list",
      "dateCreated": "2015-02-19T13:06:28-0500",
      "type": "Gene",
      "size": 22
    },
    {
      "timestamp": 1443126537363,
      "tags": [],
      "authorized": true,
      "title": "erik_test",
      "status": "CURRENT",
      "description": null,
      "name": "erik_test",
      "dateCreated": "2015-09-24T16:28:57-0400",
      "type": "Gene",
      "size": 4
    },
    {
      "timestamp": 1425505458407,
      "tags": [],
      "authorized": true,
      "title": "interacting_gene_list_1",
      "status": "CURRENT",
      "description": "",
      "name": "interacting_gene_list_1",
      "dateCreated": "2015-03-04T16:44:18-0500",
      "type": "Gene",
      "size": 16
    },
    {
      "timestamp": 1435788427891,
      "tags": [],
      "authorized": true,
      "title": "my_test_list_3",
      "status": "CURRENT",
      "description": null,
      "name": "my_test_list_3",
      "dateCreated": "2015-07-01T18:07:07-0400",
      "type": "Gene",
      "size": 3
    },
    {
      "timestamp": 1409157524131,
      "tags": [],
      "authorized": true,
      "title": "new_Gene_list_1",
      "status": "CURRENT",
      "description": "",
      "name": "new_Gene_list_1",
      "dateCreated": "2014-08-27T12:38:44-0400",
      "type": "Gene",
      "size": 5
    },
    {
      "timestamp": 1424368781769,
      "tags": [],
      "authorized": true,
      "title": "new_Gene_list_1_1",
      "status": "CURRENT",
      "description": "",
      "name": "new_Gene_list_1_1",
      "dateCreated": "2015-02-19T12:59:41-0500",
      "type": "Gene",
      "size": 6
    }
  ],
  "executionTime": "2015.09.29 16:19::09",
  "wasSuccessful": true,
  "error": null,
  "statusCode": 200
}
```

# get_thalemine_user: Get information about the current ThaleMine user
```
$ http "https://api.araport.org/community/v0.3/aip/get_thalemine_user_v1.0/access" Authorization:"Bearer: $TOKEN"
{
  "user": {
    "username": "ARAPORT:eriksf",
    "preferences": {
      "aka": "Erik Ferlanti",
      "alias": "Erik Ferlanti",
      "email": "erik@jcvi.org"
    }
  },
  "executionTime": "2015.09.29 16:22::44",
  "wasSuccessful": true,
  "error": null,
  "statusCode": 200
}
```
