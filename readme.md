![](readme/logo.jpg)

# CxAdmin

CxAdmin is a Python API client for the CxEngage API. It is a work in progress and is not yet complete.

All objects are designed to mirror their CxEngage counterparts. For example, a CxList object has the exact same properties as a list on the CxEngage platform.
Together with the way this program is designed, this means you can fetch items from CxEngage, manipulate them locally, and then upload them back to CxEngage, without having to worry about the API.

This API is designed to be easily expandable. If you would like to add functionality, please feel free to submit a pull request.

## Usage – Contents
* [Set up API client](#set-up-api-client)
* [Queues](#queues)
* [Lists](#lists)
* [Statistics](#statistics)
* [Environment](#environment)
* [Flows](#flows)

### Set up API client

```python
from CxAdmin import cx as cxadmin

cx = cxadmin.Cx(
    baseURL="your_base_url", # https://eu-west-1-prod-api.cxengage.net for EU, https://api.cxengage.net for US
    apiKey="your_api_key",
    apiSecret="your_api_secret",
    tenantID="your_tenant_id",
)
```

or

```python
from CxAdmin import cx as cxadmin

cx = cxadmin.Cx.fromConfigFile("config.json")
```

> Example config.json

```json
{
    "baseURL": "https://eu-west-1-prod-api.cxengage.net",
    "apiKey": "73668f12-4da1-9991-p182-83ufb38193pa",
    "apiSecret": "biglongjumblystringoflettersandnumbershere",
    "tenantID": "893jwa23-85k2-895k-1562-93pot7367185"
}
```

### Queues

#### Get list of queues
```python
cx.queues.getQueues()
```

### Lists

#### Get all lists
```python
cx.lists.getAllLists()
```

#### Get list by ID
```python
cx.lists.getListByID(listID)
```

#### Get list as CSV
```python
cx.lists.getListCSV(listID)
```

### Statistics

```python
cx.statistics.getInteractions(between: (datetime, datetime))
```

### Users

```python
cx.users.getAllUsers()
```

### Environment

*To be implemented*

### Flows

*To be implemented*
