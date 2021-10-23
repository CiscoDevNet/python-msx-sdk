# python_msx_sdk.IncidentsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_incident**](IncidentsApi.md#cancel_incident) | **PATCH** /incident/api/v1/incidents/{id}/cancel | Cancels an incident.
[**create_incident**](IncidentsApi.md#create_incident) | **POST** /incident/api/v1/incidents | Create a new Incident.
[**delete_incident**](IncidentsApi.md#delete_incident) | **DELETE** /incident/api/v1/incidents/{id} | Deletes an incident.
[**get_incident**](IncidentsApi.md#get_incident) | **GET** /incident/api/v1/incidents/{id} | Get incident details.
[**get_incidents**](IncidentsApi.md#get_incidents) | **GET** /incident/api/v1/incidents | Get Incidents by filter.
[**update_incident**](IncidentsApi.md#update_incident) | **PUT** /incident/api/v1/incidents/{id} | Updates an incident.


# **cancel_incident**
> Incident cancel_incident(id, incident_cancel)

Cancels an incident.

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import incidents_api
from python_msx_sdk.model.incident_cancel import IncidentCancel
from python_msx_sdk.model.incident import Incident
from python_msx_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = python_msx_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with python_msx_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = incidents_api.IncidentsApi(api_client)
    id = "id_example" # str | 
    incident_cancel = IncidentCancel(
        notes="notes_example",
        tenant="tenant_example",
    ) # IncidentCancel | 

    # example passing only required values which don't have defaults set
    try:
        # Cancels an incident.
        api_response = api_instance.cancel_incident(id, incident_cancel)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling IncidentsApi->cancel_incident: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **incident_cancel** | [**IncidentCancel**](IncidentCancel.md)|  |

### Return type

[**Incident**](Incident.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthenticated |  -  |
**403** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_incident**
> Incident create_incident(incident_create)

Create a new Incident.

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import incidents_api
from python_msx_sdk.model.incident_create import IncidentCreate
from python_msx_sdk.model.incident import Incident
from python_msx_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = python_msx_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with python_msx_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = incidents_api.IncidentsApi(api_client)
    incident_create = IncidentCreate() # IncidentCreate | 

    # example passing only required values which don't have defaults set
    try:
        # Create a new Incident.
        api_response = api_instance.create_incident(incident_create)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling IncidentsApi->create_incident: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **incident_create** | [**IncidentCreate**](IncidentCreate.md)|  |

### Return type

[**Incident**](Incident.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthenticated |  -  |
**403** | Unauthorized |  -  |
**409** | Conflict |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_incident**
> delete_incident(id)

Deletes an incident.

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import incidents_api
from python_msx_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = python_msx_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with python_msx_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = incidents_api.IncidentsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Deletes an incident.
        api_instance.delete_incident(id)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling IncidentsApi->delete_incident: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**401** | Unauthenticated |  -  |
**403** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_incident**
> Incident get_incident(id)

Get incident details.

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import incidents_api
from python_msx_sdk.model.incident import Incident
from python_msx_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = python_msx_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with python_msx_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = incidents_api.IncidentsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get incident details.
        api_response = api_instance.get_incident(id)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling IncidentsApi->get_incident: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**Incident**](Incident.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthenticated |  -  |
**403** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_incidents**
> IncidentsPage get_incidents(page, page_size)

Get Incidents by filter.

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import incidents_api
from python_msx_sdk.model.incidents_page import IncidentsPage
from python_msx_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = python_msx_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with python_msx_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = incidents_api.IncidentsApi(api_client)
    page = 0 # int | 
    page_size = 10 # int | 
    id = "id_example" # str |  (optional)
    external_id = "externalId_example" # str |  (optional)
    tenant_id = "tenantId_example" # str |  (optional)
    category = "category_example" # str |  (optional)
    subcategory = "subcategory_example" # str |  (optional)
    state = "state_example" # str | New|InProgress|OnHold|Resolved|Canceled (optional)
    priority = "priority_example" # str | Critical|Low|High|Moderate|Planning (optional)
    severity = "severity_example" # str | High|Medium|Low (optional)
    sort_by = "sortBy_example" # str | category|subcategory|priority|severity|state (optional)
    sort_order = "sortOrder_example" # str | ASC/DESC (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Incidents by filter.
        api_response = api_instance.get_incidents(page, page_size)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling IncidentsApi->get_incidents: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Incidents by filter.
        api_response = api_instance.get_incidents(page, page_size, id=id, external_id=external_id, tenant_id=tenant_id, category=category, subcategory=subcategory, state=state, priority=priority, severity=severity, sort_by=sort_by, sort_order=sort_order)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling IncidentsApi->get_incidents: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  |
 **page_size** | **int**|  |
 **id** | **str**|  | [optional]
 **external_id** | **str**|  | [optional]
 **tenant_id** | **str**|  | [optional]
 **category** | **str**|  | [optional]
 **subcategory** | **str**|  | [optional]
 **state** | **str**| New|InProgress|OnHold|Resolved|Canceled | [optional]
 **priority** | **str**| Critical|Low|High|Moderate|Planning | [optional]
 **severity** | **str**| High|Medium|Low | [optional]
 **sort_by** | **str**| category|subcategory|priority|severity|state | [optional]
 **sort_order** | **str**| ASC/DESC | [optional]

### Return type

[**IncidentsPage**](IncidentsPage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthenticated |  -  |
**403** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_incident**
> Incident update_incident(id, incident_update)

Updates an incident.

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import incidents_api
from python_msx_sdk.model.incident_update import IncidentUpdate
from python_msx_sdk.model.incident import Incident
from python_msx_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = python_msx_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with python_msx_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = incidents_api.IncidentsApi(api_client)
    id = "id_example" # str | 
    incident_update = IncidentUpdate(
        attributes={
            "key": None,
        },
        category="inquiry",
        description="description_example",
        impact="Low",
        priority="Planning",
        severity="Low",
        state="New",
        subcategory="subcategory_example",
        tenant="tenant_example",
        urgency="Low",
    ) # IncidentUpdate | 

    # example passing only required values which don't have defaults set
    try:
        # Updates an incident.
        api_response = api_instance.update_incident(id, incident_update)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling IncidentsApi->update_incident: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **incident_update** | [**IncidentUpdate**](IncidentUpdate.md)|  |

### Return type

[**Incident**](Incident.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthenticated |  -  |
**403** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

