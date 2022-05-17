# python_msx_sdk.TemplatesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_template**](TemplatesApi.md#delete_template) | **DELETE** /template/api/v8/templates/{id} | Deletes a template.
[**get_template**](TemplatesApi.md#get_template) | **GET** /template/api/v8/templates/{id} | Returns a template by id.
[**get_template_history**](TemplatesApi.md#get_template_history) | **GET** /template/api/v8/templates/{id}/history | Returns a template history by id.
[**get_templates_page**](TemplatesApi.md#get_templates_page) | **GET** /template/api/v8/templates | Returns a page of templates.
[**import_template**](TemplatesApi.md#import_template) | **POST** /template/api/v8/templates | Imports a template.
[**update_template_status**](TemplatesApi.md#update_template_status) | **PATCH** /template/api/v8/templates/{id} | Updates a template status.


# **delete_template**
> delete_template(id)

Deletes a template.

### Example


```python
import time
import python_msx_sdk
from python_msx_sdk.api import templates_api
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
    api_instance = templates_api.TemplatesApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Deletes a template.
        api_instance.delete_template(id)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling TemplatesApi->delete_template: %s\n" % e)
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

# **get_template**
> Template get_template(id)

Returns a template by id.

### Example


```python
import time
import python_msx_sdk
from python_msx_sdk.api import templates_api
from python_msx_sdk.model.template import Template
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
    api_instance = templates_api.TemplatesApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Returns a template by id.
        api_response = api_instance.get_template(id)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling TemplatesApi->get_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**Template**](Template.md)

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

# **get_template_history**
> [Template] get_template_history(id)

Returns a template history by id.

### Example


```python
import time
import python_msx_sdk
from python_msx_sdk.api import templates_api
from python_msx_sdk.model.template import Template
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
    api_instance = templates_api.TemplatesApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Returns a template history by id.
        api_response = api_instance.get_template_history(id)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling TemplatesApi->get_template_history: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**[Template]**](Template.md)

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

# **get_templates_page**
> TemplatesPage get_templates_page(page, page_size)

Returns a page of templates.

### Example


```python
import time
import python_msx_sdk
from python_msx_sdk.api import templates_api
from python_msx_sdk.model.templates_page import TemplatesPage
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
    api_instance = templates_api.TemplatesApi(api_client)
    page = 0 # int | 
    page_size = 10 # int | 
    calculate_total_items = True # bool, none_type |  (optional)
    external_id = "externalId_example" # str | External ID to filter templates by. (optional)
    service = "service_example" # str | Name of service to filter templates by. (optional)
    tags = [
        "tags_example",
    ] # [str] |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a page of templates.
        api_response = api_instance.get_templates_page(page, page_size)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling TemplatesApi->get_templates_page: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a page of templates.
        api_response = api_instance.get_templates_page(page, page_size, calculate_total_items=calculate_total_items, external_id=external_id, service=service, tags=tags)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling TemplatesApi->get_templates_page: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  |
 **page_size** | **int**|  |
 **calculate_total_items** | **bool, none_type**|  | [optional]
 **external_id** | **str**| External ID to filter templates by. | [optional]
 **service** | **str**| Name of service to filter templates by. | [optional]
 **tags** | **[str]**|  | [optional]

### Return type

[**TemplatesPage**](TemplatesPage.md)

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

# **import_template**
> Template import_template(template_create)

Imports a template.

### Example


```python
import time
import python_msx_sdk
from python_msx_sdk.api import templates_api
from python_msx_sdk.model.template import Template
from python_msx_sdk.model.template_create import TemplateCreate
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
    api_instance = templates_api.TemplatesApi(api_client)
    template_create = TemplateCreate(
        external_id="external_id_example",
        name="name_example",
        description="description_example",
        service_type="service_type_example",
        type="type_example",
        subtype="subtype_example",
        configuration="configuration_example",
        attributes={
            "key": "key_example",
        },
        tags=[
            "tags_example",
        ],
        notes="notes_example",
    ) # TemplateCreate | 

    # example passing only required values which don't have defaults set
    try:
        # Imports a template.
        api_response = api_instance.import_template(template_create)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling TemplatesApi->import_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_create** | [**TemplateCreate**](TemplateCreate.md)|  |

### Return type

[**Template**](Template.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_template_status**
> Template update_template_status(id, template_patch)

Updates a template status.

### Example


```python
import time
import python_msx_sdk
from python_msx_sdk.api import templates_api
from python_msx_sdk.model.template import Template
from python_msx_sdk.model.template_patch import TemplatePatch
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
    api_instance = templates_api.TemplatesApi(api_client)
    id = "id_example" # str | 
    template_patch = TemplatePatch(
        name="name_example",
        description="description_example",
        service_type="service_type_example",
        type="type_example",
        subtype="subtype_example",
        configuration="configuration_example",
        attributes={
            "key": "key_example",
        },
        tags=[
            "tags_example",
        ],
        notes="notes_example",
        status=TemplateStatus("NEW"),
        status_details="status_details_example",
    ) # TemplatePatch | 

    # example passing only required values which don't have defaults set
    try:
        # Updates a template status.
        api_response = api_instance.update_template_status(id, template_patch)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling TemplatesApi->update_template_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **template_patch** | [**TemplatePatch**](TemplatePatch.md)|  |

### Return type

[**Template**](Template.md)

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

