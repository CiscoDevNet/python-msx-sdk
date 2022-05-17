# python_msx_sdk.WorkflowsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_workflow**](WorkflowsApi.md#delete_workflow) | **DELETE** /workflow/api/v8/workflows/{id} | Delete a workflow.
[**export_workflow**](WorkflowsApi.md#export_workflow) | **GET** /workflow/api/v8/workflows/{id}/export | Exports a workflow.
[**get_workflow**](WorkflowsApi.md#get_workflow) | **GET** /workflow/api/v8/workflows/{id} | Returns a workflow.
[**get_workflow_start_config**](WorkflowsApi.md#get_workflow_start_config) | **GET** /workflow/api/v8/workflows/{id}/startconfig | Returns a workflow start config.
[**get_workflows_list**](WorkflowsApi.md#get_workflows_list) | **GET** /workflow/api/v8/workflows/list | Returns a list of workflows.
[**import_workflow**](WorkflowsApi.md#import_workflow) | **POST** /workflow/api/v8/workflows | Imports a workflow.
[**start_workflow**](WorkflowsApi.md#start_workflow) | **POST** /workflow/api/v8/workflows/{id}/start | Starts a workflow.
[**update_workflow**](WorkflowsApi.md#update_workflow) | **PUT** /workflow/api/v8/workflows/{id} | Updates a workflow.
[**validate_workflow**](WorkflowsApi.md#validate_workflow) | **POST** /workflow/api/v8/workflows/{id}/validate | Validates a workflow.


# **delete_workflow**
> delete_workflow(id)

Delete a workflow.

### Example


```python
import time
import python_msx_sdk
from python_msx_sdk.api import workflows_api
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
    api_instance = workflows_api.WorkflowsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete a workflow.
        api_instance.delete_workflow(id)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling WorkflowsApi->delete_workflow: %s\n" % e)
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

# **export_workflow**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} export_workflow(id)

Exports a workflow.

### Example


```python
import time
import python_msx_sdk
from python_msx_sdk.api import workflows_api
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
    api_instance = workflows_api.WorkflowsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Exports a workflow.
        api_response = api_instance.export_workflow(id)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling WorkflowsApi->export_workflow: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

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

# **get_workflow**
> Workflow get_workflow(id)

Returns a workflow.

### Example


```python
import time
import python_msx_sdk
from python_msx_sdk.api import workflows_api
from python_msx_sdk.model.workflow import Workflow
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
    api_instance = workflows_api.WorkflowsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Returns a workflow.
        api_response = api_instance.get_workflow(id)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling WorkflowsApi->get_workflow: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**Workflow**](Workflow.md)

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

# **get_workflow_start_config**
> WorkflowStartConfig get_workflow_start_config(id)

Returns a workflow start config.

### Example


```python
import time
import python_msx_sdk
from python_msx_sdk.api import workflows_api
from python_msx_sdk.model.workflow_start_config import WorkflowStartConfig
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
    api_instance = workflows_api.WorkflowsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Returns a workflow start config.
        api_response = api_instance.get_workflow_start_config(id)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling WorkflowsApi->get_workflow_start_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**WorkflowStartConfig**](WorkflowStartConfig.md)

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

# **get_workflows_list**
> [Workflow] get_workflows_list()

Returns a list of workflows.

### Example


```python
import time
import python_msx_sdk
from python_msx_sdk.api import workflows_api
from python_msx_sdk.model.workflow import Workflow
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
    api_instance = workflows_api.WorkflowsApi(api_client)
    tenant_id = "tenantId_example" # str |  (optional)
    atomic = False # bool |  (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of workflows.
        api_response = api_instance.get_workflows_list(tenant_id=tenant_id, atomic=atomic)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling WorkflowsApi->get_workflows_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | [optional]
 **atomic** | **bool**|  | [optional] if omitted the server will use the default value of False

### Return type

[**[Workflow]**](Workflow.md)

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

# **import_workflow**
> WorkflowMapping import_workflow(request_body)

Imports a workflow.

### Example


```python
import time
import python_msx_sdk
from python_msx_sdk.api import workflows_api
from python_msx_sdk.model.workflow_mapping import WorkflowMapping
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
    api_instance = workflows_api.WorkflowsApi(api_client)
    request_body = {
        "key": None,
    } # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | 
    tenant_ids = [
        "tenantIds_example",
    ] # [str] |  (optional)
    _global = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Imports a workflow.
        api_response = api_instance.import_workflow(request_body)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling WorkflowsApi->import_workflow: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Imports a workflow.
        api_response = api_instance.import_workflow(request_body, tenant_ids=tenant_ids, _global=_global)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling WorkflowsApi->import_workflow: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  |
 **tenant_ids** | **[str]**|  | [optional]
 **_global** | **bool**|  | [optional]

### Return type

[**WorkflowMapping**](WorkflowMapping.md)

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

# **start_workflow**
> [StartWorkflowResponse] start_workflow(id, workflow_start_config)

Starts a workflow.

### Example


```python
import time
import python_msx_sdk
from python_msx_sdk.api import workflows_api
from python_msx_sdk.model.start_workflow_response import StartWorkflowResponse
from python_msx_sdk.model.workflow_start_config import WorkflowStartConfig
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
    api_instance = workflows_api.WorkflowsApi(api_client)
    id = "id_example" # str | 
    workflow_start_config = WorkflowStartConfig(
        input_variables=[
            WorkflowVariable(None),
        ],
        type_of_target_needed="type_of_target_needed_example",
        target_id="target_id_example",
    ) # WorkflowStartConfig | 
    sync = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Starts a workflow.
        api_response = api_instance.start_workflow(id, workflow_start_config)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling WorkflowsApi->start_workflow: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Starts a workflow.
        api_response = api_instance.start_workflow(id, workflow_start_config, sync=sync)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling WorkflowsApi->start_workflow: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **workflow_start_config** | [**WorkflowStartConfig**](WorkflowStartConfig.md)|  |
 **sync** | **bool**|  | [optional]

### Return type

[**[StartWorkflowResponse]**](StartWorkflowResponse.md)

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

# **update_workflow**
> WorkflowMapping update_workflow(id, request_body)

Updates a workflow.

### Example


```python
import time
import python_msx_sdk
from python_msx_sdk.api import workflows_api
from python_msx_sdk.model.workflow_mapping import WorkflowMapping
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
    api_instance = workflows_api.WorkflowsApi(api_client)
    id = "id_example" # str | 
    request_body = {
        "key": None,
    } # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | 
    tenant_ids = [
        "tenantIds_example",
    ] # [str] |  (optional)
    _global = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Updates a workflow.
        api_response = api_instance.update_workflow(id, request_body)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling WorkflowsApi->update_workflow: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Updates a workflow.
        api_response = api_instance.update_workflow(id, request_body, tenant_ids=tenant_ids, _global=_global)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling WorkflowsApi->update_workflow: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **request_body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  |
 **tenant_ids** | **[str]**|  | [optional]
 **_global** | **bool**|  | [optional]

### Return type

[**WorkflowMapping**](WorkflowMapping.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_workflow**
> ValidateWorkflowResponse validate_workflow(id)

Validates a workflow.

### Example


```python
import time
import python_msx_sdk
from python_msx_sdk.api import workflows_api
from python_msx_sdk.model.validate_workflow_response import ValidateWorkflowResponse
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
    api_instance = workflows_api.WorkflowsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Validates a workflow.
        api_response = api_instance.validate_workflow(id)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling WorkflowsApi->validate_workflow: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**ValidateWorkflowResponse**](ValidateWorkflowResponse.md)

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

