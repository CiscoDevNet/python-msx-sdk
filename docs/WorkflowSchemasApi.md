# python_msx_sdk.WorkflowSchemasApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_workflow_schema**](WorkflowSchemasApi.md#get_workflow_schema) | **GET** /workflow/api/v8/schemas/{id} | Returns a workflow schema.
[**get_workflow_schemas_list**](WorkflowSchemasApi.md#get_workflow_schemas_list) | **GET** /workflow/api/v8/schemas/list | Returns a list of workflow schemas.


# **get_workflow_schema**
> WorkflowSchemaByTypeResponse get_workflow_schema(id)

Returns a workflow schema.

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import workflow_schemas_api
from python_msx_sdk.model.workflow_schema_by_type_response import WorkflowSchemaByTypeResponse
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
    api_instance = workflow_schemas_api.WorkflowSchemasApi(api_client)
    id = "id_example" # str | 
    schema_type = "view" # str |  (optional) if omitted the server will use the default value of "view"

    # example passing only required values which don't have defaults set
    try:
        # Returns a workflow schema.
        api_response = api_instance.get_workflow_schema(id)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling WorkflowSchemasApi->get_workflow_schema: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a workflow schema.
        api_response = api_instance.get_workflow_schema(id, schema_type=schema_type)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling WorkflowSchemasApi->get_workflow_schema: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **schema_type** | **str**|  | [optional] if omitted the server will use the default value of "view"

### Return type

[**WorkflowSchemaByTypeResponse**](WorkflowSchemaByTypeResponse.md)

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

# **get_workflow_schemas_list**
> [WorkflowSchema] get_workflow_schemas_list()

Returns a list of workflow schemas.

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import workflow_schemas_api
from python_msx_sdk.model.workflow_schema import WorkflowSchema
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
    api_instance = workflow_schemas_api.WorkflowSchemasApi(api_client)
    schema_type = "view" # str |  (optional) if omitted the server will use the default value of "view"
    variable_type = False # bool |  (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Returns a list of workflow schemas.
        api_response = api_instance.get_workflow_schemas_list()
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling WorkflowSchemasApi->get_workflow_schemas_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of workflow schemas.
        api_response = api_instance.get_workflow_schemas_list(schema_type=schema_type, variable_type=variable_type)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling WorkflowSchemasApi->get_workflow_schemas_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_type** | **str**|  | defaults to "category"
 **schema_type** | **str**|  | [optional] if omitted the server will use the default value of "view"
 **variable_type** | **bool**|  | [optional] if omitted the server will use the default value of False

### Return type

[**[WorkflowSchema]**](WorkflowSchema.md)

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

