# python_msx_sdk.WorkflowInstancesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_workflow_instance**](WorkflowInstancesApi.md#cancel_workflow_instance) | **POST** /workflow/api/v8/workflows/instances/{id}/cancel | Cancels a workflow instance.
[**delete_workflow_instance**](WorkflowInstancesApi.md#delete_workflow_instance) | **DELETE** /workflow/api/v8/workflows/instances/{id} | Deletes a workflow instance.
[**get_workflow_instance**](WorkflowInstancesApi.md#get_workflow_instance) | **GET** /workflow/api/v8/workflows/instances/{id} | Returns a workflow instance.
[**get_workflow_instance_action**](WorkflowInstancesApi.md#get_workflow_instance_action) | **GET** /workflow/api/v8/workflows/instances/{id}/actions/{actionId} | Returns a workflow instance action.
[**get_workflow_instances_list**](WorkflowInstancesApi.md#get_workflow_instances_list) | **GET** /workflow/api/v8/workflows/{id}/instances/list | Returns a list of workflow instances.


# **cancel_workflow_instance**
> WorkflowInstance cancel_workflow_instance(id)

Cancels a workflow instance.

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import workflow_instances_api
from python_msx_sdk.model.workflow_instance import WorkflowInstance
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
    api_instance = workflow_instances_api.WorkflowInstancesApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Cancels a workflow instance.
        api_response = api_instance.cancel_workflow_instance(id)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling WorkflowInstancesApi->cancel_workflow_instance: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**WorkflowInstance**](WorkflowInstance.md)

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

# **delete_workflow_instance**
> WorkflowInstanceDeleteResponse delete_workflow_instance(id)

Deletes a workflow instance.

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import workflow_instances_api
from python_msx_sdk.model.workflow_instance_delete_response import WorkflowInstanceDeleteResponse
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
    api_instance = workflow_instances_api.WorkflowInstancesApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Deletes a workflow instance.
        api_response = api_instance.delete_workflow_instance(id)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling WorkflowInstancesApi->delete_workflow_instance: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**WorkflowInstanceDeleteResponse**](WorkflowInstanceDeleteResponse.md)

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

# **get_workflow_instance**
> WorkflowInstance get_workflow_instance(id)

Returns a workflow instance.

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import workflow_instances_api
from python_msx_sdk.model.workflow_instance import WorkflowInstance
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
    api_instance = workflow_instances_api.WorkflowInstancesApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Returns a workflow instance.
        api_response = api_instance.get_workflow_instance(id)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling WorkflowInstancesApi->get_workflow_instance: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**WorkflowInstance**](WorkflowInstance.md)

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

# **get_workflow_instance_action**
> WorkflowAction get_workflow_instance_action(id, action_id)

Returns a workflow instance action.

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import workflow_instances_api
from python_msx_sdk.model.workflow_action import WorkflowAction
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
    api_instance = workflow_instances_api.WorkflowInstancesApi(api_client)
    id = "id_example" # str | 
    action_id = "actionId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Returns a workflow instance action.
        api_response = api_instance.get_workflow_instance_action(id, action_id)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling WorkflowInstancesApi->get_workflow_instance_action: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **action_id** | **str**|  |

### Return type

[**WorkflowAction**](WorkflowAction.md)

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

# **get_workflow_instances_list**
> [WorkflowInstance] get_workflow_instances_list(id, page, page_size)

Returns a list of workflow instances.

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import workflow_instances_api
from python_msx_sdk.model.workflow_instance import WorkflowInstance
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
    api_instance = workflow_instances_api.WorkflowInstancesApi(api_client)
    id = "id_example" # str | 
    page = 0 # int | 
    page_size = 10 # int | 
    date_from = dateutil_parser('1970-01-01').date() # date |  (optional)
    date_to = dateutil_parser('1970-01-01').date() # date |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a list of workflow instances.
        api_response = api_instance.get_workflow_instances_list(id, page, page_size)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling WorkflowInstancesApi->get_workflow_instances_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of workflow instances.
        api_response = api_instance.get_workflow_instances_list(id, page, page_size, date_from=date_from, date_to=date_to)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling WorkflowInstancesApi->get_workflow_instances_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **page** | **int**|  |
 **page_size** | **int**|  |
 **date_from** | **date**|  | [optional]
 **date_to** | **date**|  | [optional]

### Return type

[**[WorkflowInstance]**](WorkflowInstance.md)

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

