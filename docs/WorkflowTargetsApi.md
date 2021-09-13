# python_msx_sdk.WorkflowTargetsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_workflow_target**](WorkflowTargetsApi.md#create_workflow_target) | **POST** /workflow/api/v8/targets | Creates a new workflow target.
[**delete_workflow_target**](WorkflowTargetsApi.md#delete_workflow_target) | **DELETE** /workflow/api/v8/targets/{id} | Deletes a workflow target.
[**get_workflow_target**](WorkflowTargetsApi.md#get_workflow_target) | **GET** /workflow/api/v8/targets/{id} | Returns a workflow target.
[**get_workflow_targets_list**](WorkflowTargetsApi.md#get_workflow_targets_list) | **GET** /workflow/api/v8/targets/list | Returns a list of workflow targets.
[**update_workflow_target**](WorkflowTargetsApi.md#update_workflow_target) | **PUT** /workflow/api/v8/targets/{id} | Updates a workflow target.


# **create_workflow_target**
> WorkflowTarget create_workflow_target(workflow_target_create)

Creates a new workflow target.

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import workflow_targets_api
from python_msx_sdk.model.workflow_target import WorkflowTarget
from python_msx_sdk.model.workflow_target_create import WorkflowTargetCreate
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
    api_instance = workflow_targets_api.WorkflowTargetsApi(api_client)
    workflow_target_create = WorkflowTargetCreate() # WorkflowTargetCreate | 

    # example passing only required values which don't have defaults set
    try:
        # Creates a new workflow target.
        api_response = api_instance.create_workflow_target(workflow_target_create)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling WorkflowTargetsApi->create_workflow_target: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_target_create** | [**WorkflowTargetCreate**](WorkflowTargetCreate.md)|  |

### Return type

[**WorkflowTarget**](WorkflowTarget.md)

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

# **delete_workflow_target**
> delete_workflow_target(id)

Deletes a workflow target.

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import workflow_targets_api
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
    api_instance = workflow_targets_api.WorkflowTargetsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Deletes a workflow target.
        api_instance.delete_workflow_target(id)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling WorkflowTargetsApi->delete_workflow_target: %s\n" % e)
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

# **get_workflow_target**
> WorkflowTarget get_workflow_target(id)

Returns a workflow target.

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import workflow_targets_api
from python_msx_sdk.model.workflow_target import WorkflowTarget
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
    api_instance = workflow_targets_api.WorkflowTargetsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Returns a workflow target.
        api_response = api_instance.get_workflow_target(id)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling WorkflowTargetsApi->get_workflow_target: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**WorkflowTarget**](WorkflowTarget.md)

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

# **get_workflow_targets_list**
> [WorkflowTarget] get_workflow_targets_list()

Returns a list of workflow targets.

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import workflow_targets_api
from python_msx_sdk.model.workflow_target import WorkflowTarget
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
    api_instance = workflow_targets_api.WorkflowTargetsApi(api_client)
    internal = True # bool |  (optional)
    type = "type_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of workflow targets.
        api_response = api_instance.get_workflow_targets_list(internal=internal, type=type)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling WorkflowTargetsApi->get_workflow_targets_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **internal** | **bool**|  | [optional]
 **type** | **str**|  | [optional]

### Return type

[**[WorkflowTarget]**](WorkflowTarget.md)

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

# **update_workflow_target**
> WorkflowTarget update_workflow_target(id, workflow_target_update)

Updates a workflow target.

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import workflow_targets_api
from python_msx_sdk.model.workflow_target import WorkflowTarget
from python_msx_sdk.model.workflow_target_update import WorkflowTargetUpdate
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
    api_instance = workflow_targets_api.WorkflowTargetsApi(api_client)
    id = "id_example" # str | 
    workflow_target_update = WorkflowTargetUpdate(
        name="l",
        description="l",
        title="title_example",
        schema_id="schema_id_example",
        type="type_example",
        properties={
            "key": None,
        },
        unique_name="unique_name_example",
    ) # WorkflowTargetUpdate | 

    # example passing only required values which don't have defaults set
    try:
        # Updates a workflow target.
        api_response = api_instance.update_workflow_target(id, workflow_target_update)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling WorkflowTargetsApi->update_workflow_target: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **workflow_target_update** | [**WorkflowTargetUpdate**](WorkflowTargetUpdate.md)|  |

### Return type

[**WorkflowTarget**](WorkflowTarget.md)

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

