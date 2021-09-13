# python_msx_sdk.OffersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_offer**](OffersApi.md#create_offer) | **POST** /consume/api/v8/offers | Creates a product offer.
[**delete_offer**](OffersApi.md#delete_offer) | **DELETE** /consume/api/v8/offers/{id} | Deletes a product offer
[**get_offer**](OffersApi.md#get_offer) | **GET** /consume/api/v8/offers/{id} | Returns a product offer.
[**get_offer_assignments_list**](OffersApi.md#get_offer_assignments_list) | **GET** /consume/api/v8/offers/{id}/assignments/list | Returns a list of tenant assignments for a product offer.
[**get_offers_count**](OffersApi.md#get_offers_count) | **GET** /consume/api/v8/offers/count | Returns the number of product offers.
[**get_offers_page**](OffersApi.md#get_offers_page) | **GET** /consume/api/v8/offers | Returns a page of product offers.
[**update_offer**](OffersApi.md#update_offer) | **PUT** /consume/api/v8/offers/{id} | Updates a product offer.
[**update_offer_assignments**](OffersApi.md#update_offer_assignments) | **PUT** /consume/api/v8/offers/{id}/assignments | Updates the tenant assignemnts for a product offer.


# **create_offer**
> Offer create_offer(offer_create)

Creates a product offer.

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import offers_api
from python_msx_sdk.model.offer_create import OfferCreate
from python_msx_sdk.model.offer import Offer
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
    api_instance = offers_api.OffersApi(api_client)
    offer_create = OfferCreate() # OfferCreate | 

    # example passing only required values which don't have defaults set
    try:
        # Creates a product offer.
        api_response = api_instance.create_offer(offer_create)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling OffersApi->create_offer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offer_create** | [**OfferCreate**](OfferCreate.md)|  |

### Return type

[**Offer**](Offer.md)

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

# **delete_offer**
> delete_offer(id)

Deletes a product offer

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import offers_api
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
    api_instance = offers_api.OffersApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Deletes a product offer
        api_instance.delete_offer(id)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling OffersApi->delete_offer: %s\n" % e)
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

# **get_offer**
> Offer get_offer(id)

Returns a product offer.

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import offers_api
from python_msx_sdk.model.offer import Offer
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
    api_instance = offers_api.OffersApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Returns a product offer.
        api_response = api_instance.get_offer(id)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling OffersApi->get_offer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**Offer**](Offer.md)

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

# **get_offer_assignments_list**
> [CatalogAssignment] get_offer_assignments_list(id)

Returns a list of tenant assignments for a product offer.

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import offers_api
from python_msx_sdk.model.catalog_assignment import CatalogAssignment
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
    api_instance = offers_api.OffersApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Returns a list of tenant assignments for a product offer.
        api_response = api_instance.get_offer_assignments_list(id)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling OffersApi->get_offer_assignments_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**[CatalogAssignment]**](CatalogAssignment.md)

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

# **get_offers_count**
> int get_offers_count()

Returns the number of product offers.

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import offers_api
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
    api_instance = offers_api.OffersApi(api_client)
    product_id = "productId_example" # str |  (optional)
    tenant_id = "tenantId_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns the number of product offers.
        api_response = api_instance.get_offers_count(product_id=product_id, tenant_id=tenant_id)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling OffersApi->get_offers_count: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**|  | [optional]
 **tenant_id** | **str**|  | [optional]

### Return type

**int**

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

# **get_offers_page**
> OffersPage get_offers_page(page, page_size)

Returns a page of product offers.

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import offers_api
from python_msx_sdk.model.offers_page import OffersPage
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
    api_instance = offers_api.OffersApi(api_client)
    page = 0 # int | 
    page_size = 10 # int | 
    product_id = "productId_example" # str |  (optional)
    tenant_ids = [
        "tenantIds_example",
    ] # [str] |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a page of product offers.
        api_response = api_instance.get_offers_page(page, page_size)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling OffersApi->get_offers_page: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a page of product offers.
        api_response = api_instance.get_offers_page(page, page_size, product_id=product_id, tenant_ids=tenant_ids)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling OffersApi->get_offers_page: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  |
 **page_size** | **int**|  |
 **product_id** | **str**|  | [optional]
 **tenant_ids** | **[str]**|  | [optional]

### Return type

[**OffersPage**](OffersPage.md)

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

# **update_offer**
> Offer update_offer(id, offer_update)

Updates a product offer.

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import offers_api
from python_msx_sdk.model.offer_update import OfferUpdate
from python_msx_sdk.model.offer import Offer
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
    api_instance = offers_api.OffersApi(api_client)
    id = "id_example" # str | 
    offer_update = OfferUpdate(
        name="name_example",
        label="label_example",
        description="description_example",
        product_id="product_id_example",
        version=1,
        display_order=1,
        image="image_example",
        price="price_example",
        type="type_example",
        supported_properties=[
            "supported_properties_example",
        ],
        supported_options=[
            NameValue(
                name="name_example",
                value="value_example",
            ),
        ],
        approvals={
            "key": None,
        },
    ) # OfferUpdate | 

    # example passing only required values which don't have defaults set
    try:
        # Updates a product offer.
        api_response = api_instance.update_offer(id, offer_update)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling OffersApi->update_offer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **offer_update** | [**OfferUpdate**](OfferUpdate.md)|  |

### Return type

[**Offer**](Offer.md)

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

# **update_offer_assignments**
> [CatalogAssignment] update_offer_assignments(id, request_body)

Updates the tenant assignemnts for a product offer.

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import offers_api
from python_msx_sdk.model.catalog_assignment import CatalogAssignment
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
    api_instance = offers_api.OffersApi(api_client)
    id = "id_example" # str | 
    request_body = ["e8ff9360-c8f1-4f06-84d8-d8105bd29e1e","3c64b303-ec28-4fe2-99b5-13f521b92700","48feaddb-45d0-4126-a216-3e450bfdbba4"] # [str] | 

    # example passing only required values which don't have defaults set
    try:
        # Updates the tenant assignemnts for a product offer.
        api_response = api_instance.update_offer_assignments(id, request_body)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling OffersApi->update_offer_assignments: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **request_body** | **[str]**|  |

### Return type

[**[CatalogAssignment]**](CatalogAssignment.md)

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

