# python_msx_sdk.TenantsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tenant**](TenantsApi.md#create_tenant) | **POST** /idm/api/v8/tenants | Creates a new tenant.
[**delete_tenant**](TenantsApi.md#delete_tenant) | **DELETE** /idm/api/v8/tenants/{id} | Deletes a tenant by id.
[**get_tenant**](TenantsApi.md#get_tenant) | **GET** /idm/api/v8/tenants/{id} | Returns a tenant by id.
[**get_tenant_by_external_id**](TenantsApi.md#get_tenant_by_external_id) | **GET** /idm/api/v8/tenants/externalId/{externalId} | Returns a tenant by externalId.
[**get_tenants_list**](TenantsApi.md#get_tenants_list) | **GET** /idm/api/v8/tenants/list | Returns a list of tenants.
[**get_tenants_page**](TenantsApi.md#get_tenants_page) | **GET** /idm/api/v8/tenants | Returns a page of tenants.
[**update_tenant**](TenantsApi.md#update_tenant) | **PUT** /idm/api/v8/tenants/{id} | Updates a tenant by id.


# **create_tenant**
> Tenant create_tenant(tenant_create)

Creates a new tenant.

### Example


```python
import time
import python_msx_sdk
from python_msx_sdk.api import tenants_api
from python_msx_sdk.model.tenant_create import TenantCreate
from python_msx_sdk.model.tenant import Tenant
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
    api_instance = tenants_api.TenantsApi(api_client)
    tenant_create = TenantCreate(None) # TenantCreate | 

    # example passing only required values which don't have defaults set
    try:
        # Creates a new tenant.
        api_response = api_instance.create_tenant(tenant_create)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling TenantsApi->create_tenant: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_create** | [**TenantCreate**](TenantCreate.md)|  |

### Return type

[**Tenant**](Tenant.md)

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

# **delete_tenant**
> delete_tenant(id)

Deletes a tenant by id.

### Example


```python
import time
import python_msx_sdk
from python_msx_sdk.api import tenants_api
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
    api_instance = tenants_api.TenantsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Deletes a tenant by id.
        api_instance.delete_tenant(id)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling TenantsApi->delete_tenant: %s\n" % e)
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
**409** | Conflict |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenant**
> Tenant get_tenant(id)

Returns a tenant by id.

### Example


```python
import time
import python_msx_sdk
from python_msx_sdk.api import tenants_api
from python_msx_sdk.model.tenant import Tenant
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
    api_instance = tenants_api.TenantsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Returns a tenant by id.
        api_response = api_instance.get_tenant(id)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling TenantsApi->get_tenant: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**Tenant**](Tenant.md)

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

# **get_tenant_by_external_id**
> Tenant get_tenant_by_external_id(external_id)

Returns a tenant by externalId.

### Example


```python
import time
import python_msx_sdk
from python_msx_sdk.api import tenants_api
from python_msx_sdk.model.tenant import Tenant
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
    api_instance = tenants_api.TenantsApi(api_client)
    external_id = "externalId_example" # str | 
    show_image = False # bool |  (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Returns a tenant by externalId.
        api_response = api_instance.get_tenant_by_external_id(external_id)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling TenantsApi->get_tenant_by_external_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a tenant by externalId.
        api_response = api_instance.get_tenant_by_external_id(external_id, show_image=show_image)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling TenantsApi->get_tenant_by_external_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_id** | **str**|  |
 **show_image** | **bool**|  | [optional] if omitted the server will use the default value of False

### Return type

[**Tenant**](Tenant.md)

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

# **get_tenants_list**
> [Tenant] get_tenants_list(ids)

Returns a list of tenants.

### Example


```python
import time
import python_msx_sdk
from python_msx_sdk.api import tenants_api
from python_msx_sdk.model.tenant import Tenant
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
    api_instance = tenants_api.TenantsApi(api_client)
    ids = [
        "ids_example",
    ] # [str] | 
    show_image = False # bool |  (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Returns a list of tenants.
        api_response = api_instance.get_tenants_list(ids)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling TenantsApi->get_tenants_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of tenants.
        api_response = api_instance.get_tenants_list(ids, show_image=show_image)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling TenantsApi->get_tenants_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **[str]**|  |
 **show_image** | **bool**|  | [optional] if omitted the server will use the default value of False

### Return type

[**[Tenant]**](Tenant.md)

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

# **get_tenants_page**
> TenantsPage get_tenants_page(page, page_size)

Returns a page of tenants.

### Example


```python
import time
import python_msx_sdk
from python_msx_sdk.api import tenants_api
from python_msx_sdk.model.tenants_page import TenantsPage
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
    api_instance = tenants_api.TenantsApi(api_client)
    page = 0 # int | 
    page_size = 10 # int | 
    parent_id = "parentId_example" # str |  (optional)
    show_image = False # bool |  (optional) if omitted the server will use the default value of False
    sort_by = "name" # str |  (optional)
    sort_order = "asc" # str |  (optional) if omitted the server will use the default value of "asc"

    # example passing only required values which don't have defaults set
    try:
        # Returns a page of tenants.
        api_response = api_instance.get_tenants_page(page, page_size)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling TenantsApi->get_tenants_page: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a page of tenants.
        api_response = api_instance.get_tenants_page(page, page_size, parent_id=parent_id, show_image=show_image, sort_by=sort_by, sort_order=sort_order)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling TenantsApi->get_tenants_page: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  |
 **page_size** | **int**|  |
 **parent_id** | **str**|  | [optional]
 **show_image** | **bool**|  | [optional] if omitted the server will use the default value of False
 **sort_by** | **str**|  | [optional]
 **sort_order** | **str**|  | [optional] if omitted the server will use the default value of "asc"

### Return type

[**TenantsPage**](TenantsPage.md)

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

# **update_tenant**
> Tenant update_tenant(id, tenant_update)

Updates a tenant by id.

### Example


```python
import time
import python_msx_sdk
from python_msx_sdk.api import tenants_api
from python_msx_sdk.model.tenant_update import TenantUpdate
from python_msx_sdk.model.tenant import Tenant
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
    api_instance = tenants_api.TenantsApi(api_client)
    id = "id_example" # str | 
    tenant_update = TenantUpdate(
        name="name_example",
        description="description_example",
        url="url_example",
        image="image_example",
        email="email_example",
    ) # TenantUpdate | 

    # example passing only required values which don't have defaults set
    try:
        # Updates a tenant by id.
        api_response = api_instance.update_tenant(id, tenant_update)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling TenantsApi->update_tenant: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **tenant_update** | [**TenantUpdate**](TenantUpdate.md)|  |

### Return type

[**Tenant**](Tenant.md)

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

