# python_msx_sdk.TemplateApplicationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apply_template**](TemplateApplicationsApi.md#apply_template) | **POST** /template/api/v8/templates/{id}/applications | Applies a template to a target.
[**delete_template_application**](TemplateApplicationsApi.md#delete_template_application) | **DELETE** /template/api/v8/templates/applications/{id} | Deletes a template application.
[**get_template_application**](TemplateApplicationsApi.md#get_template_application) | **GET** /template/api/v8/templates/applications/{id} | Gets a template application.
[**get_template_application_history**](TemplateApplicationsApi.md#get_template_application_history) | **GET** /template/api/v8/templates/applications/{id}/history | Gets a template application history.
[**get_template_applications_page**](TemplateApplicationsApi.md#get_template_applications_page) | **GET** /template/api/v8/templates/applications | Get a page of template applications.
[**update_application_status**](TemplateApplicationsApi.md#update_application_status) | **PATCH** /template/api/v8/templates/applications/{id} | Updates an application status.


# **apply_template**
> TemplateApplication apply_template(id, template_application_create)

Applies a template to a target.

### Example


```python
import time
import python_msx_sdk
from python_msx_sdk.api import template_applications_api
from python_msx_sdk.model.template_application_create import TemplateApplicationCreate
from python_msx_sdk.model.template_application import TemplateApplication
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
    api_instance = template_applications_api.TemplateApplicationsApi(api_client)
    id = "id_example" # str | 
    template_application_create = TemplateApplicationCreate(
        tenant_id="tenant_id_example",
        target_id="target_id_example",
        target_type="target_type_example",
        parameters={
            "key": "key_example",
        },
    ) # TemplateApplicationCreate | 

    # example passing only required values which don't have defaults set
    try:
        # Applies a template to a target.
        api_response = api_instance.apply_template(id, template_application_create)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling TemplateApplicationsApi->apply_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **template_application_create** | [**TemplateApplicationCreate**](TemplateApplicationCreate.md)|  |

### Return type

[**TemplateApplication**](TemplateApplication.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthenticated |  -  |
**403** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_template_application**
> delete_template_application(id)

Deletes a template application.

### Example


```python
import time
import python_msx_sdk
from python_msx_sdk.api import template_applications_api
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
    api_instance = template_applications_api.TemplateApplicationsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Deletes a template application.
        api_instance.delete_template_application(id)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling TemplateApplicationsApi->delete_template_application: %s\n" % e)
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

# **get_template_application**
> TemplateApplication get_template_application(id)

Gets a template application.

### Example


```python
import time
import python_msx_sdk
from python_msx_sdk.api import template_applications_api
from python_msx_sdk.model.template_application import TemplateApplication
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
    api_instance = template_applications_api.TemplateApplicationsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Gets a template application.
        api_response = api_instance.get_template_application(id)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling TemplateApplicationsApi->get_template_application: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**TemplateApplication**](TemplateApplication.md)

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

# **get_template_application_history**
> [TemplateApplication] get_template_application_history(id)

Gets a template application history.

### Example


```python
import time
import python_msx_sdk
from python_msx_sdk.api import template_applications_api
from python_msx_sdk.model.template_application import TemplateApplication
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
    api_instance = template_applications_api.TemplateApplicationsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Gets a template application history.
        api_response = api_instance.get_template_application_history(id)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling TemplateApplicationsApi->get_template_application_history: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**[TemplateApplication]**](TemplateApplication.md)

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

# **get_template_applications_page**
> TemplateApplicationsPage get_template_applications_page(tenant_id, page, page_size)

Get a page of template applications.

### Example


```python
import time
import python_msx_sdk
from python_msx_sdk.api import template_applications_api
from python_msx_sdk.model.template_applications_page import TemplateApplicationsPage
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
    api_instance = template_applications_api.TemplateApplicationsApi(api_client)
    tenant_id = "tenantId_example" # str | 
    page = 0 # int | 
    page_size = 10 # int | 
    template_id = "templateId_example" # str |  (optional)
    target_id = "targetId_example" # str |  (optional)
    target_type = "targetType_example" # str |  (optional)
    calculate_total_items = True # bool, none_type |  (optional)
    sort_by = "createdOn" # str |  (optional) if omitted the server will use the default value of "createdOn"
    sort_order = "asc" # str |  (optional) if omitted the server will use the default value of "asc"

    # example passing only required values which don't have defaults set
    try:
        # Get a page of template applications.
        api_response = api_instance.get_template_applications_page(tenant_id, page, page_size)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling TemplateApplicationsApi->get_template_applications_page: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a page of template applications.
        api_response = api_instance.get_template_applications_page(tenant_id, page, page_size, template_id=template_id, target_id=target_id, target_type=target_type, calculate_total_items=calculate_total_items, sort_by=sort_by, sort_order=sort_order)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling TemplateApplicationsApi->get_template_applications_page: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  |
 **page** | **int**|  |
 **page_size** | **int**|  |
 **template_id** | **str**|  | [optional]
 **target_id** | **str**|  | [optional]
 **target_type** | **str**|  | [optional]
 **calculate_total_items** | **bool, none_type**|  | [optional]
 **sort_by** | **str**|  | [optional] if omitted the server will use the default value of "createdOn"
 **sort_order** | **str**|  | [optional] if omitted the server will use the default value of "asc"

### Return type

[**TemplateApplicationsPage**](TemplateApplicationsPage.md)

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

# **update_application_status**
> TemplateApplication update_application_status(id, template_application_status_patch)

Updates an application status.

### Example


```python
import time
import python_msx_sdk
from python_msx_sdk.api import template_applications_api
from python_msx_sdk.model.template_application_status_patch import TemplateApplicationStatusPatch
from python_msx_sdk.model.template_application import TemplateApplication
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
    api_instance = template_applications_api.TemplateApplicationsApi(api_client)
    id = "id_example" # str | 
    template_application_status_patch = TemplateApplicationStatusPatch(
        status=TemplateStatus("NEW"),
        status_details="status_details_example",
    ) # TemplateApplicationStatusPatch | 

    # example passing only required values which don't have defaults set
    try:
        # Updates an application status.
        api_response = api_instance.update_application_status(id, template_application_status_patch)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling TemplateApplicationsApi->update_application_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **template_application_status_patch** | [**TemplateApplicationStatusPatch**](TemplateApplicationStatusPatch.md)|  |

### Return type

[**TemplateApplication**](TemplateApplication.md)

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

