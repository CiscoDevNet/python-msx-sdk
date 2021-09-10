# python_msx_sdk.WorkflowCategoriesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_workflow_category**](WorkflowCategoriesApi.md#create_workflow_category) | **POST** /workflow/api/v8/categories | Creates a new workflow category.
[**delete_workflow_category**](WorkflowCategoriesApi.md#delete_workflow_category) | **DELETE** /workflow/api/v8/categories/{id} | Deletes a workflow category.
[**get_workflow_categories_list**](WorkflowCategoriesApi.md#get_workflow_categories_list) | **GET** /workflow/api/v8/categories/list | Returns a list of workflow categories.
[**get_workflow_category**](WorkflowCategoriesApi.md#get_workflow_category) | **GET** /workflow/api/v8/categories/{id} | Returns a workflow category.
[**update_workflow_category**](WorkflowCategoriesApi.md#update_workflow_category) | **PUT** /workflow/api/v8/categories/{id} | Updates a workflow category.


# **create_workflow_category**
> WorkflowCategory create_workflow_category(tenant_id, workflow_category_create)

Creates a new workflow category.

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import workflow_categories_api
from python_msx_sdk.model.workflow_category import WorkflowCategory
from python_msx_sdk.model.workflow_category_create import WorkflowCategoryCreate
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
    api_instance = workflow_categories_api.WorkflowCategoriesApi(api_client)
    tenant_id = "tenantId_example" # str | 
    workflow_category_create = WorkflowCategoryCreate(
        name="name_example",
        title="title_example",
        description="description_example",
        schema_id="schema_id_example",
        unique_name="unique_name_example",
    ) # WorkflowCategoryCreate | 

    # example passing only required values which don't have defaults set
    try:
        # Creates a new workflow category.
        api_response = api_instance.create_workflow_category(tenant_id, workflow_category_create)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling WorkflowCategoriesApi->create_workflow_category: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  |
 **workflow_category_create** | [**WorkflowCategoryCreate**](WorkflowCategoryCreate.md)|  |

### Return type

[**WorkflowCategory**](WorkflowCategory.md)

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

# **delete_workflow_category**
> delete_workflow_category(id)

Deletes a workflow category.

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import workflow_categories_api
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
    api_instance = workflow_categories_api.WorkflowCategoriesApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Deletes a workflow category.
        api_instance.delete_workflow_category(id)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling WorkflowCategoriesApi->delete_workflow_category: %s\n" % e)
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

# **get_workflow_categories_list**
> [WorkflowCategory] get_workflow_categories_list()

Returns a list of workflow categories.

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import workflow_categories_api
from python_msx_sdk.model.workflow_category import WorkflowCategory
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
    api_instance = workflow_categories_api.WorkflowCategoriesApi(api_client)
    tenant_id = "tenantId_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of workflow categories.
        api_response = api_instance.get_workflow_categories_list(tenant_id=tenant_id)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling WorkflowCategoriesApi->get_workflow_categories_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | [optional]

### Return type

[**[WorkflowCategory]**](WorkflowCategory.md)

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

# **get_workflow_category**
> WorkflowCategory get_workflow_category(id)

Returns a workflow category.

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import workflow_categories_api
from python_msx_sdk.model.workflow_category import WorkflowCategory
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
    api_instance = workflow_categories_api.WorkflowCategoriesApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Returns a workflow category.
        api_response = api_instance.get_workflow_category(id)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling WorkflowCategoriesApi->get_workflow_category: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**WorkflowCategory**](WorkflowCategory.md)

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

# **update_workflow_category**
> WorkflowCategory update_workflow_category(id, workflow_category_update)

Updates a workflow category.

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import workflow_categories_api
from python_msx_sdk.model.workflow_category import WorkflowCategory
from python_msx_sdk.model.workflow_category_update import WorkflowCategoryUpdate
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
    api_instance = workflow_categories_api.WorkflowCategoriesApi(api_client)
    id = "id_example" # str | 
    workflow_category_update = WorkflowCategoryUpdate(
        name="name_example",
        title="title_example",
        description="description_example",
        schema_id="schema_id_example",
        unique_name="unique_name_example",
    ) # WorkflowCategoryUpdate | 

    # example passing only required values which don't have defaults set
    try:
        # Updates a workflow category.
        api_response = api_instance.update_workflow_category(id, workflow_category_update)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling WorkflowCategoriesApi->update_workflow_category: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **workflow_category_update** | [**WorkflowCategoryUpdate**](WorkflowCategoryUpdate.md)|  |

### Return type

[**WorkflowCategory**](WorkflowCategory.md)

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

