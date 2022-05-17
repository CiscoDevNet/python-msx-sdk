# python_msx_sdk.RegistrationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_registered_product_version**](RegistrationApi.md#delete_registered_product_version) | **DELETE** /vulnerability/api/v8/vulnerabilities/registrations/{id} | Delete a registration.
[**get_registered_product_version_page**](RegistrationApi.md#get_registered_product_version_page) | **GET** /vulnerability/api/v8/vulnerabilities/registrations | Returns a filtered page of registered products / versions.
[**register_product_version**](RegistrationApi.md#register_product_version) | **POST** /vulnerability/api/v8/vulnerabilities/registrations | Register a product / verison combination for vulnerability inspection.


# **delete_registered_product_version**
> delete_registered_product_version(id)

Delete a registration.

### Example


```python
import time
import python_msx_sdk
from python_msx_sdk.api import registration_api
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
    api_instance = registration_api.RegistrationApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete a registration.
        api_instance.delete_registered_product_version(id)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling RegistrationApi->delete_registered_product_version: %s\n" % e)
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
**401** | Unauthenticated |  -  |
**403** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_registered_product_version_page**
> VulnerabilitiesRegistrationPage get_registered_product_version_page(page, page_size)

Returns a filtered page of registered products / versions.

### Example


```python
import time
import python_msx_sdk
from python_msx_sdk.api import registration_api
from python_msx_sdk.model.vulnerabilities_registration_page import VulnerabilitiesRegistrationPage
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
    api_instance = registration_api.RegistrationApi(api_client)
    page = 0 # int | 
    page_size = 10 # int | 
    product = "ios_xe" # str | Product identifier (as defined in NIST's CPE dictionary) to filter by. (optional)
    version = "12.3" # str | Product version (as defined in NIST's CPE dictionary) filter to filter by. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a filtered page of registered products / versions.
        api_response = api_instance.get_registered_product_version_page(page, page_size)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling RegistrationApi->get_registered_product_version_page: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a filtered page of registered products / versions.
        api_response = api_instance.get_registered_product_version_page(page, page_size, product=product, version=version)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling RegistrationApi->get_registered_product_version_page: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  |
 **page_size** | **int**|  |
 **product** | **str**| Product identifier (as defined in NIST&#39;s CPE dictionary) to filter by. | [optional]
 **version** | **str**| Product version (as defined in NIST&#39;s CPE dictionary) filter to filter by. | [optional]

### Return type

[**VulnerabilitiesRegistrationPage**](VulnerabilitiesRegistrationPage.md)

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

# **register_product_version**
> VulnerabilityRegistration register_product_version(vulnerability_registration_create)

Register a product / verison combination for vulnerability inspection.

### Example


```python
import time
import python_msx_sdk
from python_msx_sdk.api import registration_api
from python_msx_sdk.model.vulnerability_registration import VulnerabilityRegistration
from python_msx_sdk.model.error import Error
from python_msx_sdk.model.vulnerability_registration_create import VulnerabilityRegistrationCreate
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = python_msx_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with python_msx_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = registration_api.RegistrationApi(api_client)
    vulnerability_registration_create = VulnerabilityRegistrationCreate(
        product="ios_xe",
        version="14.3.2",
    ) # VulnerabilityRegistrationCreate | 

    # example passing only required values which don't have defaults set
    try:
        # Register a product / verison combination for vulnerability inspection.
        api_response = api_instance.register_product_version(vulnerability_registration_create)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling RegistrationApi->register_product_version: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vulnerability_registration_create** | [**VulnerabilityRegistrationCreate**](VulnerabilityRegistrationCreate.md)|  |

### Return type

[**VulnerabilityRegistration**](VulnerabilityRegistration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthenticated |  -  |
**403** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

