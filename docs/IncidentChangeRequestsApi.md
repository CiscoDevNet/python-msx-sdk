# python_msx_sdk.IncidentChangeRequestsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_change_request**](IncidentChangeRequestsApi.md#create_change_request) | **POST** /incident/api/v8/changerequests | Create a change request.
[**delete_change_request**](IncidentChangeRequestsApi.md#delete_change_request) | **DELETE** /incident/api/v8/changerequests/{id} | Deletes a change request.
[**get_change_request**](IncidentChangeRequestsApi.md#get_change_request) | **GET** /incident/api/v8/changerequests/{id} | Returns a change request.
[**get_change_requests_page**](IncidentChangeRequestsApi.md#get_change_requests_page) | **GET** /incident/api/v8/changerequests | Returns a filtered list of change requests.
[**update_change_request**](IncidentChangeRequestsApi.md#update_change_request) | **PUT** /incident/api/v8/changerequests/{id} | Updates a change request.


# **create_change_request**
> ChangeRequest create_change_request(change_request_create)

Create a change request.

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import incident_change_requests_api
from python_msx_sdk.model.change_request_create import ChangeRequestCreate
from python_msx_sdk.model.change_request import ChangeRequest
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
    api_instance = incident_change_requests_api.IncidentChangeRequestsApi(api_client)
    change_request_create = ChangeRequestCreate() # ChangeRequestCreate | 

    # example passing only required values which don't have defaults set
    try:
        # Create a change request.
        api_response = api_instance.create_change_request(change_request_create)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling IncidentChangeRequestsApi->create_change_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **change_request_create** | [**ChangeRequestCreate**](ChangeRequestCreate.md)|  |

### Return type

[**ChangeRequest**](ChangeRequest.md)

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

# **delete_change_request**
> delete_change_request(id)

Deletes a change request.

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import incident_change_requests_api
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
    api_instance = incident_change_requests_api.IncidentChangeRequestsApi(api_client)
    id = "id_example" # str | 
    tenant_id = "tenantId_example" # str | Required for bi-directional scenario (optional)

    # example passing only required values which don't have defaults set
    try:
        # Deletes a change request.
        api_instance.delete_change_request(id)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling IncidentChangeRequestsApi->delete_change_request: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Deletes a change request.
        api_instance.delete_change_request(id, tenant_id=tenant_id)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling IncidentChangeRequestsApi->delete_change_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **tenant_id** | **str**| Required for bi-directional scenario | [optional]

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

# **get_change_request**
> ChangeRequest get_change_request(id)

Returns a change request.

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import incident_change_requests_api
from python_msx_sdk.model.change_request import ChangeRequest
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
    api_instance = incident_change_requests_api.IncidentChangeRequestsApi(api_client)
    id = "id_example" # str | Change Request Number  CHG0030022
    tenant_id = "tenantId_example" # str | Required for bi-directional scenario (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a change request.
        api_response = api_instance.get_change_request(id)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling IncidentChangeRequestsApi->get_change_request: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a change request.
        api_response = api_instance.get_change_request(id, tenant_id=tenant_id)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling IncidentChangeRequestsApi->get_change_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Change Request Number  CHG0030022 |
 **tenant_id** | **str**| Required for bi-directional scenario | [optional]

### Return type

[**ChangeRequest**](ChangeRequest.md)

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

# **get_change_requests_page**
> ChangeRequestsPage get_change_requests_page(page, page_size)

Returns a filtered list of change requests.

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import incident_change_requests_api
from python_msx_sdk.model.change_requests_page import ChangeRequestsPage
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
    api_instance = incident_change_requests_api.IncidentChangeRequestsApi(api_client)
    page = 0 # int | 
    page_size = 10 # int | 
    tenant_id = "tenantId_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a filtered list of change requests.
        api_response = api_instance.get_change_requests_page(page, page_size)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling IncidentChangeRequestsApi->get_change_requests_page: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a filtered list of change requests.
        api_response = api_instance.get_change_requests_page(page, page_size, tenant_id=tenant_id)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling IncidentChangeRequestsApi->get_change_requests_page: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  |
 **page_size** | **int**|  |
 **tenant_id** | **str**|  | [optional]

### Return type

[**ChangeRequestsPage**](ChangeRequestsPage.md)

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

# **update_change_request**
> ChangeRequest update_change_request(id, change_request_update)

Updates a change request.

Update change requests. Returns not found, if passed in tenant's serviceNow instance does not hold the record.

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import incident_change_requests_api
from python_msx_sdk.model.change_request_update import ChangeRequestUpdate
from python_msx_sdk.model.change_request import ChangeRequest
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
    api_instance = incident_change_requests_api.IncidentChangeRequestsApi(api_client)
    id = "id_example" # str | 
    change_request_update = ChangeRequestUpdate(
        name="name_example",
        description="description_example",
        attributes={},
        tenant_id="tenant_id_example",
    ) # ChangeRequestUpdate | 

    # example passing only required values which don't have defaults set
    try:
        # Updates a change request.
        api_response = api_instance.update_change_request(id, change_request_update)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling IncidentChangeRequestsApi->update_change_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **change_request_update** | [**ChangeRequestUpdate**](ChangeRequestUpdate.md)|  |

### Return type

[**ChangeRequest**](ChangeRequest.md)

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

