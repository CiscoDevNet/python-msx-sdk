# python_msx_sdk.WorkflowEventsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_workflow_event**](WorkflowEventsApi.md#create_workflow_event) | **POST** /workflow/api/v8/events | Creates a new workflow event.
[**delete_workflow_event**](WorkflowEventsApi.md#delete_workflow_event) | **DELETE** /workflow/api/v8/events/{id} | Deletes a workflow event.
[**get_workflow_event**](WorkflowEventsApi.md#get_workflow_event) | **GET** /workflow/api/v8/events/{id} | Returns a workflow event.
[**get_workflow_events_list**](WorkflowEventsApi.md#get_workflow_events_list) | **GET** /workflow/api/v8/events/list | Returns a list of workflow events.
[**update_workflow_event**](WorkflowEventsApi.md#update_workflow_event) | **PUT** /workflow/api/v8/events/{id} | Updates a workflow event.


# **create_workflow_event**
> WorkflowEvent create_workflow_event(workflow_event_create)

Creates a new workflow event.

### Example


```python
import time
import python_msx_sdk
from python_msx_sdk.api import workflow_events_api
from python_msx_sdk.model.workflow_event_create import WorkflowEventCreate
from python_msx_sdk.model.workflow_event import WorkflowEvent
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
    api_instance = workflow_events_api.WorkflowEventsApi(api_client)
    workflow_event_create = WorkflowEventCreate(None) # WorkflowEventCreate | 

    # example passing only required values which don't have defaults set
    try:
        # Creates a new workflow event.
        api_response = api_instance.create_workflow_event(workflow_event_create)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling WorkflowEventsApi->create_workflow_event: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_event_create** | [**WorkflowEventCreate**](WorkflowEventCreate.md)|  |

### Return type

[**WorkflowEvent**](WorkflowEvent.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_workflow_event**
> delete_workflow_event(id)

Deletes a workflow event.

### Example


```python
import time
import python_msx_sdk
from python_msx_sdk.api import workflow_events_api
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
    api_instance = workflow_events_api.WorkflowEventsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Deletes a workflow event.
        api_instance.delete_workflow_event(id)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling WorkflowEventsApi->delete_workflow_event: %s\n" % e)
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

# **get_workflow_event**
> WorkflowEvent get_workflow_event(id)

Returns a workflow event.

### Example


```python
import time
import python_msx_sdk
from python_msx_sdk.api import workflow_events_api
from python_msx_sdk.model.workflow_event import WorkflowEvent
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
    api_instance = workflow_events_api.WorkflowEventsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Returns a workflow event.
        api_response = api_instance.get_workflow_event(id)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling WorkflowEventsApi->get_workflow_event: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**WorkflowEvent**](WorkflowEvent.md)

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

# **get_workflow_events_list**
> [WorkflowEvent] get_workflow_events_list()

Returns a list of workflow events.

### Example


```python
import time
import python_msx_sdk
from python_msx_sdk.api import workflow_events_api
from python_msx_sdk.model.workflow_event import WorkflowEvent
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
    api_instance = workflow_events_api.WorkflowEventsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Returns a list of workflow events.
        api_response = api_instance.get_workflow_events_list()
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling WorkflowEventsApi->get_workflow_events_list: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[WorkflowEvent]**](WorkflowEvent.md)

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

# **update_workflow_event**
> WorkflowEvent update_workflow_event(id, workflow_event_update)

Updates a workflow event.

### Example


```python
import time
import python_msx_sdk
from python_msx_sdk.api import workflow_events_api
from python_msx_sdk.model.workflow_event_update import WorkflowEventUpdate
from python_msx_sdk.model.workflow_event import WorkflowEvent
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
    api_instance = workflow_events_api.WorkflowEventsApi(api_client)
    id = "id_example" # str | 
    workflow_event_update = WorkflowEventUpdate(
        title="title_example",
        description="description_example",
        target_id="target_id_example",
        schema_id="schema_id_example",
        properties={
            "key": None,
        },
    ) # WorkflowEventUpdate | 

    # example passing only required values which don't have defaults set
    try:
        # Updates a workflow event.
        api_response = api_instance.update_workflow_event(id, workflow_event_update)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling WorkflowEventsApi->update_workflow_event: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **workflow_event_update** | [**WorkflowEventUpdate**](WorkflowEventUpdate.md)|  |

### Return type

[**WorkflowEvent**](WorkflowEvent.md)

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

