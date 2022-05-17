# python_msx_sdk.SitesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_devices_to_site**](SitesApi.md#add_devices_to_site) | **POST** /manage/api/v8/sites/{id}/devices/add | Add devices to a site.
[**add_services_to_site**](SitesApi.md#add_services_to_site) | **POST** /manage/api/v8/sites/{id}/services/add | Add services to a site.
[**create_site**](SitesApi.md#create_site) | **POST** /manage/api/v8/sites | Creates a new site.
[**delete_site**](SitesApi.md#delete_site) | **DELETE** /manage/api/v8/sites/{id} | Deletes a site.
[**get_site**](SitesApi.md#get_site) | **GET** /manage/api/v8/sites/{id} | Returns a site.
[**get_sites_page**](SitesApi.md#get_sites_page) | **GET** /manage/api/v8/sites | Returns a page of Sites. Only one filter is supported at a time.
[**remove_devices_from_site**](SitesApi.md#remove_devices_from_site) | **POST** /manage/api/v8/sites/{id}/devices/remove | Removes devices from a site.
[**remove_services_from_site**](SitesApi.md#remove_services_from_site) | **POST** /manage/api/v8/sites/{id}/services/remove | Remove services from a site.
[**update_site**](SitesApi.md#update_site) | **PUT** /manage/api/v8/sites/{id} | Updates a site.


# **add_devices_to_site**
> Site add_devices_to_site(id, request_body)

Add devices to a site.

### Example


```python
import time
import python_msx_sdk
from python_msx_sdk.api import sites_api
from python_msx_sdk.model.site import Site
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
    api_instance = sites_api.SitesApi(api_client)
    id = "id_example" # str | 
    request_body = [
        "request_body_example",
    ] # [str] | 

    # example passing only required values which don't have defaults set
    try:
        # Add devices to a site.
        api_response = api_instance.add_devices_to_site(id, request_body)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling SitesApi->add_devices_to_site: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **request_body** | **[str]**|  |

### Return type

[**Site**](Site.md)

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

# **add_services_to_site**
> Site add_services_to_site(id, request_body)

Add services to a site.

### Example


```python
import time
import python_msx_sdk
from python_msx_sdk.api import sites_api
from python_msx_sdk.model.site import Site
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
    api_instance = sites_api.SitesApi(api_client)
    id = "id_example" # str | 
    request_body = [
        "request_body_example",
    ] # [str] | 

    # example passing only required values which don't have defaults set
    try:
        # Add services to a site.
        api_response = api_instance.add_services_to_site(id, request_body)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling SitesApi->add_services_to_site: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **request_body** | **[str]**|  |

### Return type

[**Site**](Site.md)

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

# **create_site**
> Site create_site(site_create)

Creates a new site.

### Example


```python
import time
import python_msx_sdk
from python_msx_sdk.api import sites_api
from python_msx_sdk.model.site_create import SiteCreate
from python_msx_sdk.model.site import Site
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
    api_instance = sites_api.SitesApi(api_client)
    site_create = SiteCreate(None) # SiteCreate | 

    # example passing only required values which don't have defaults set
    try:
        # Creates a new site.
        api_response = api_instance.create_site(site_create)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling SitesApi->create_site: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_create** | [**SiteCreate**](SiteCreate.md)|  |

### Return type

[**Site**](Site.md)

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

# **delete_site**
> delete_site(id)

Deletes a site.

### Example


```python
import time
import python_msx_sdk
from python_msx_sdk.api import sites_api
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
    api_instance = sites_api.SitesApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Deletes a site.
        api_instance.delete_site(id)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling SitesApi->delete_site: %s\n" % e)
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

# **get_site**
> Site get_site(id)

Returns a site.

### Example


```python
import time
import python_msx_sdk
from python_msx_sdk.api import sites_api
from python_msx_sdk.model.site import Site
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
    api_instance = sites_api.SitesApi(api_client)
    id = "id_example" # str | 
    show_image = False # bool |  (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Returns a site.
        api_response = api_instance.get_site(id)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling SitesApi->get_site: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a site.
        api_response = api_instance.get_site(id, show_image=show_image)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling SitesApi->get_site: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **show_image** | **bool**|  | [optional] if omitted the server will use the default value of False

### Return type

[**Site**](Site.md)

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

# **get_sites_page**
> SitesPage get_sites_page(page, page_size)

Returns a page of Sites. Only one filter is supported at a time.

### Example


```python
import time
import python_msx_sdk
from python_msx_sdk.api import sites_api
from python_msx_sdk.model.sites_page import SitesPage
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
    api_instance = sites_api.SitesApi(api_client)
    page = 0 # int | 
    page_size = 10 # int | 
    tenant_id = "tenantId_example" # str |  (optional)
    include_subtenants = False # bool |  (optional) if omitted the server will use the default value of False
    service_id = "serviceId_example" # str |  (optional)
    service_type = "serviceType_example" # str |  (optional)
    device_id = "deviceId_example" # str |  (optional)
    parent_id = "parentId_example" # str |  (optional)
    type = "type_example" # str |  (optional)
    managing_control_plane_id = "managingControlPlaneId_example" # str |  (optional)
    show_image = False # bool |  (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Returns a page of Sites. Only one filter is supported at a time.
        api_response = api_instance.get_sites_page(page, page_size)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling SitesApi->get_sites_page: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a page of Sites. Only one filter is supported at a time.
        api_response = api_instance.get_sites_page(page, page_size, tenant_id=tenant_id, include_subtenants=include_subtenants, service_id=service_id, service_type=service_type, device_id=device_id, parent_id=parent_id, type=type, managing_control_plane_id=managing_control_plane_id, show_image=show_image)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling SitesApi->get_sites_page: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  |
 **page_size** | **int**|  |
 **tenant_id** | **str**|  | [optional]
 **include_subtenants** | **bool**|  | [optional] if omitted the server will use the default value of False
 **service_id** | **str**|  | [optional]
 **service_type** | **str**|  | [optional]
 **device_id** | **str**|  | [optional]
 **parent_id** | **str**|  | [optional]
 **type** | **str**|  | [optional]
 **managing_control_plane_id** | **str**|  | [optional]
 **show_image** | **bool**|  | [optional] if omitted the server will use the default value of False

### Return type

[**SitesPage**](SitesPage.md)

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

# **remove_devices_from_site**
> Site remove_devices_from_site(id, request_body)

Removes devices from a site.

### Example


```python
import time
import python_msx_sdk
from python_msx_sdk.api import sites_api
from python_msx_sdk.model.site import Site
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
    api_instance = sites_api.SitesApi(api_client)
    id = "id_example" # str | 
    request_body = [
        "request_body_example",
    ] # [str] | 

    # example passing only required values which don't have defaults set
    try:
        # Removes devices from a site.
        api_response = api_instance.remove_devices_from_site(id, request_body)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling SitesApi->remove_devices_from_site: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **request_body** | **[str]**|  |

### Return type

[**Site**](Site.md)

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

# **remove_services_from_site**
> Site remove_services_from_site(id, request_body)

Remove services from a site.

### Example


```python
import time
import python_msx_sdk
from python_msx_sdk.api import sites_api
from python_msx_sdk.model.site import Site
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
    api_instance = sites_api.SitesApi(api_client)
    id = "id_example" # str | 
    request_body = [
        "request_body_example",
    ] # [str] | 

    # example passing only required values which don't have defaults set
    try:
        # Remove services from a site.
        api_response = api_instance.remove_services_from_site(id, request_body)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling SitesApi->remove_services_from_site: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **request_body** | **[str]**|  |

### Return type

[**Site**](Site.md)

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

# **update_site**
> Site update_site(id, site_update)

Updates a site.

### Example


```python
import time
import python_msx_sdk
from python_msx_sdk.api import sites_api
from python_msx_sdk.model.site_update import SiteUpdate
from python_msx_sdk.model.site import Site
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
    api_instance = sites_api.SitesApi(api_client)
    id = "id_example" # str | 
    site_update = SiteUpdate(
        parent_id="parent_id_example",
        name="name_example",
        description="description_example",
        type="zBAMDTMv2D2ylmgd10Z3UB",
        address=SiteAddress(
            name="name_example",
            company="company_example",
            formatted_address="formatted_address_example",
            address1="address1_example",
            address2="address2_example",
            city="city_example",
            state="state_example",
            country="country_example",
            post_code="post_code_example",
        ),
        contact=SiteContact(
            name="name_example",
            phone="phone_example",
            email="email_example",
        ),
        location=SiteLocation(
            latitude=-90,
            longitude=-180,
        ),
        image="image_example",
        managing_control_plane_id="managing_control_plane_id_example",
        attributes={
            "key": "key_example",
        },
    ) # SiteUpdate | 
    send_notification = False # bool |  (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Updates a site.
        api_response = api_instance.update_site(id, site_update)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling SitesApi->update_site: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Updates a site.
        api_response = api_instance.update_site(id, site_update, send_notification=send_notification)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling SitesApi->update_site: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **site_update** | [**SiteUpdate**](SiteUpdate.md)|  |
 **send_notification** | **bool**|  | [optional] if omitted the server will use the default value of False

### Return type

[**Site**](Site.md)

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

