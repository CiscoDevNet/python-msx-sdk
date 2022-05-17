# python_msx_sdk.BillingPricesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_price**](BillingPricesApi.md#add_price) | **POST** /billing/api/v8/prices | Add price for tenant and event type.
[**delete_price**](BillingPricesApi.md#delete_price) | **DELETE** /billing/api/v8/prices/{id} | Delete a price.
[**get_price**](BillingPricesApi.md#get_price) | **GET** /billing/api/v8/prices/{id} | Get a price.
[**get_prices_page**](BillingPricesApi.md#get_prices_page) | **GET** /billing/api/v8/prices | Retrieve a page of prices.
[**update_price**](BillingPricesApi.md#update_price) | **PUT** /billing/api/v8/prices/{id} | Update price for an event type and tenant.


# **add_price**
> BillingPrice add_price(billing_price_create)

Add price for tenant and event type.

Needs MANAGE_PRICES permission to allow for the creation of a price.

### Example


```python
import time
import python_msx_sdk
from python_msx_sdk.api import billing_prices_api
from python_msx_sdk.model.billing_price import BillingPrice
from python_msx_sdk.model.billing_price_create import BillingPriceCreate
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
    api_instance = billing_prices_api.BillingPricesApi(api_client)
    billing_price_create = BillingPriceCreate(None) # BillingPriceCreate | 

    # example passing only required values which don't have defaults set
    try:
        # Add price for tenant and event type.
        api_response = api_instance.add_price(billing_price_create)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling BillingPricesApi->add_price: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **billing_price_create** | [**BillingPriceCreate**](BillingPriceCreate.md)|  |

### Return type

[**BillingPrice**](BillingPrice.md)

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

# **delete_price**
> delete_price(id)

Delete a price.

Needs MANAGE_PRICES permission to delete a price.

### Example


```python
import time
import python_msx_sdk
from python_msx_sdk.api import billing_prices_api
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
    api_instance = billing_prices_api.BillingPricesApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete a price.
        api_instance.delete_price(id)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling BillingPricesApi->delete_price: %s\n" % e)
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

# **get_price**
> BillingPrice get_price(id)

Get a price.

Needs VIEW_PRICES permission to get pricing detail.

### Example


```python
import time
import python_msx_sdk
from python_msx_sdk.api import billing_prices_api
from python_msx_sdk.model.billing_price import BillingPrice
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
    api_instance = billing_prices_api.BillingPricesApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get a price.
        api_response = api_instance.get_price(id)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling BillingPricesApi->get_price: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**BillingPrice**](BillingPrice.md)

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

# **get_prices_page**
> BillingPricesPage get_prices_page(tenant_id, page, page_size)

Retrieve a page of prices.

Needs VIEW_PRICES permission to view the pricing details.

### Example


```python
import time
import python_msx_sdk
from python_msx_sdk.api import billing_prices_api
from python_msx_sdk.model.billing_prices_page import BillingPricesPage
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
    api_instance = billing_prices_api.BillingPricesApi(api_client)
    tenant_id = "tenantId_example" # str | 
    page = 0 # int | 
    page_size = 10 # int | 
    type = "type_example" # str |  (optional)
    subtype = "subtype_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a page of prices.
        api_response = api_instance.get_prices_page(tenant_id, page, page_size)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling BillingPricesApi->get_prices_page: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve a page of prices.
        api_response = api_instance.get_prices_page(tenant_id, page, page_size, type=type, subtype=subtype)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling BillingPricesApi->get_prices_page: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  |
 **page** | **int**|  |
 **page_size** | **int**|  |
 **type** | **str**|  | [optional]
 **subtype** | **str**|  | [optional]

### Return type

[**BillingPricesPage**](BillingPricesPage.md)

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

# **update_price**
> BillingPrice update_price(id, billing_price_update)

Update price for an event type and tenant.

Needs MANAGE_PRICES permission to update a pricing detail.

### Example


```python
import time
import python_msx_sdk
from python_msx_sdk.api import billing_prices_api
from python_msx_sdk.model.billing_price import BillingPrice
from python_msx_sdk.model.billing_price_update import BillingPriceUpdate
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
    api_instance = billing_prices_api.BillingPricesApi(api_client)
    id = "id_example" # str | 
    billing_price_update = BillingPriceUpdate(
        name="name_example",
        description="description_example",
        type="type_example",
        subtype="subtype_example",
        source="source_example",
        price=0,
        billing_period=1,
        service="service_example",
        tenant_id="tenant_id_example",
    ) # BillingPriceUpdate | 

    # example passing only required values which don't have defaults set
    try:
        # Update price for an event type and tenant.
        api_response = api_instance.update_price(id, billing_price_update)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling BillingPricesApi->update_price: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **billing_price_update** | [**BillingPriceUpdate**](BillingPriceUpdate.md)|  |

### Return type

[**BillingPrice**](BillingPrice.md)

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

