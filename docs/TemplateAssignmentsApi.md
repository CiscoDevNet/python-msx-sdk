# python_msx_sdk.TemplateAssignmentsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batch_assign_template**](TemplateAssignmentsApi.md#batch_assign_template) | **POST** /template/api/v8/templates/{id}/assignments/add | Assigns a template to one or more tenants.
[**batch_unassign_template**](TemplateAssignmentsApi.md#batch_unassign_template) | **POST** /template/api/v8/templates/{id}/assignments/remove | Unassigns a template from one or more tenants.
[**get_assignment**](TemplateAssignmentsApi.md#get_assignment) | **GET** /template/api/v8/templates/assignments/{id} | Gets a template assignment.
[**get_assignment_history**](TemplateAssignmentsApi.md#get_assignment_history) | **GET** /template/api/v8/templates/assignments/{id}/history | Gets a template assignment history.
[**get_template_assignments_page**](TemplateAssignmentsApi.md#get_template_assignments_page) | **GET** /template/api/v8/templates/assignments | Returns a page of template assignments.
[**update_assignment_status**](TemplateAssignmentsApi.md#update_assignment_status) | **PATCH** /template/api/v8/templates/assignments/{id} | Updates a template assignment status.


# **batch_assign_template**
> [TemplateAssignmentResponse] batch_assign_template(id, request_body)

Assigns a template to one or more tenants.

### Example


```python
import time
import python_msx_sdk
from python_msx_sdk.api import template_assignments_api
from python_msx_sdk.model.template_assignment_response import TemplateAssignmentResponse
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
    api_instance = template_assignments_api.TemplateAssignmentsApi(api_client)
    id = "id_example" # str | 
    request_body = [
        "request_body_example",
    ] # [str] | 
    inheritable = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Assigns a template to one or more tenants.
        api_response = api_instance.batch_assign_template(id, request_body)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling TemplateAssignmentsApi->batch_assign_template: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Assigns a template to one or more tenants.
        api_response = api_instance.batch_assign_template(id, request_body, inheritable=inheritable)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling TemplateAssignmentsApi->batch_assign_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **request_body** | **[str]**|  |
 **inheritable** | **bool**|  | [optional]

### Return type

[**[TemplateAssignmentResponse]**](TemplateAssignmentResponse.md)

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

# **batch_unassign_template**
> [TemplateAssignmentResponse] batch_unassign_template(id, request_body)

Unassigns a template from one or more tenants.

### Example


```python
import time
import python_msx_sdk
from python_msx_sdk.api import template_assignments_api
from python_msx_sdk.model.template_assignment_response import TemplateAssignmentResponse
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
    api_instance = template_assignments_api.TemplateAssignmentsApi(api_client)
    id = "id_example" # str | 
    request_body = [
        "request_body_example",
    ] # [str] | 

    # example passing only required values which don't have defaults set
    try:
        # Unassigns a template from one or more tenants.
        api_response = api_instance.batch_unassign_template(id, request_body)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling TemplateAssignmentsApi->batch_unassign_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **request_body** | **[str]**|  |

### Return type

[**[TemplateAssignmentResponse]**](TemplateAssignmentResponse.md)

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

# **get_assignment**
> TemplateAssignment get_assignment(id)

Gets a template assignment.

### Example


```python
import time
import python_msx_sdk
from python_msx_sdk.api import template_assignments_api
from python_msx_sdk.model.template_assignment import TemplateAssignment
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
    api_instance = template_assignments_api.TemplateAssignmentsApi(api_client)
    id = "id_example" # str | ID of template assignment record.

    # example passing only required values which don't have defaults set
    try:
        # Gets a template assignment.
        api_response = api_instance.get_assignment(id)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling TemplateAssignmentsApi->get_assignment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of template assignment record. |

### Return type

[**TemplateAssignment**](TemplateAssignment.md)

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

# **get_assignment_history**
> [TemplateAssignment] get_assignment_history(id)

Gets a template assignment history.

### Example


```python
import time
import python_msx_sdk
from python_msx_sdk.api import template_assignments_api
from python_msx_sdk.model.template_assignment import TemplateAssignment
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
    api_instance = template_assignments_api.TemplateAssignmentsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Gets a template assignment history.
        api_response = api_instance.get_assignment_history(id)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling TemplateAssignmentsApi->get_assignment_history: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**[TemplateAssignment]**](TemplateAssignment.md)

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

# **get_template_assignments_page**
> TemplateAssignmentsPage get_template_assignments_page(page, page_size)

Returns a page of template assignments.

### Example


```python
import time
import python_msx_sdk
from python_msx_sdk.api import template_assignments_api
from python_msx_sdk.model.template_assignments_page import TemplateAssignmentsPage
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
    api_instance = template_assignments_api.TemplateAssignmentsApi(api_client)
    page = 0 # int | 
    page_size = 10 # int | 
    template_id = "templateId_example" # str |  (optional)
    tenant_id = "tenantId_example" # str |  (optional)
    calculate_total_items = True # bool, none_type |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a page of template assignments.
        api_response = api_instance.get_template_assignments_page(page, page_size)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling TemplateAssignmentsApi->get_template_assignments_page: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a page of template assignments.
        api_response = api_instance.get_template_assignments_page(page, page_size, template_id=template_id, tenant_id=tenant_id, calculate_total_items=calculate_total_items)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling TemplateAssignmentsApi->get_template_assignments_page: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  |
 **page_size** | **int**|  |
 **template_id** | **str**|  | [optional]
 **tenant_id** | **str**|  | [optional]
 **calculate_total_items** | **bool, none_type**|  | [optional]

### Return type

[**TemplateAssignmentsPage**](TemplateAssignmentsPage.md)

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

# **update_assignment_status**
> TemplateAssignment update_assignment_status(id, template_assignment_status_patch)

Updates a template assignment status.

### Example


```python
import time
import python_msx_sdk
from python_msx_sdk.api import template_assignments_api
from python_msx_sdk.model.template_assignment import TemplateAssignment
from python_msx_sdk.model.template_assignment_status_patch import TemplateAssignmentStatusPatch
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
    api_instance = template_assignments_api.TemplateAssignmentsApi(api_client)
    id = "id_example" # str | ID of template assignment record.
    template_assignment_status_patch = TemplateAssignmentStatusPatch(
        status=TemplateStatus("NEW"),
        status_details="status_details_example",
    ) # TemplateAssignmentStatusPatch | 

    # example passing only required values which don't have defaults set
    try:
        # Updates a template assignment status.
        api_response = api_instance.update_assignment_status(id, template_assignment_status_patch)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling TemplateAssignmentsApi->update_assignment_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of template assignment record. |
 **template_assignment_status_patch** | [**TemplateAssignmentStatusPatch**](TemplateAssignmentStatusPatch.md)|  |

### Return type

[**TemplateAssignment**](TemplateAssignment.md)

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

