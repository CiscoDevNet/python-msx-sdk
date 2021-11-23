# python_msx_sdk.ProductsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_product**](ProductsApi.md#create_product) | **POST** /consume/api/v8/products | Creates a product.
[**delete_product**](ProductsApi.md#delete_product) | **DELETE** /consume/api/v8/products/{id} | Deletes a product.
[**get_product**](ProductsApi.md#get_product) | **GET** /consume/api/v8/products/{id} | Returns a product.
[**get_product_assignments_list**](ProductsApi.md#get_product_assignments_list) | **GET** /consume/api/v8/products/{id}/assignments/list | Returns a list of tenant assignments for a product .
[**get_products_count**](ProductsApi.md#get_products_count) | **GET** /consume/api/v8/products/count | Returns the number of products.
[**get_products_page**](ProductsApi.md#get_products_page) | **GET** /consume/api/v8/products | Returns a page of products.
[**update_product**](ProductsApi.md#update_product) | **PUT** /consume/api/v8/products/{id} | Updates a product.
[**update_product_assignments**](ProductsApi.md#update_product_assignments) | **PUT** /consume/api/v8/products/{id}/assignments | Updates the tenant assignments for a product.


# **create_product**
> Product create_product(product_create)

Creates a product.

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import products_api
from python_msx_sdk.model.product import Product
from python_msx_sdk.model.product_create import ProductCreate
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
    api_instance = products_api.ProductsApi(api_client)
    product_create = ProductCreate() # ProductCreate | 

    # example passing only required values which don't have defaults set
    try:
        # Creates a product.
        api_response = api_instance.create_product(product_create)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling ProductsApi->create_product: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_create** | [**ProductCreate**](ProductCreate.md)|  |

### Return type

[**Product**](Product.md)

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

# **delete_product**
> delete_product(id)

Deletes a product.

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import products_api
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
    api_instance = products_api.ProductsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Deletes a product.
        api_instance.delete_product(id)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling ProductsApi->delete_product: %s\n" % e)
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

# **get_product**
> Product get_product(id)

Returns a product.

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import products_api
from python_msx_sdk.model.product import Product
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
    api_instance = products_api.ProductsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Returns a product.
        api_response = api_instance.get_product(id)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling ProductsApi->get_product: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**Product**](Product.md)

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

# **get_product_assignments_list**
> [CatalogAssignment] get_product_assignments_list(id)

Returns a list of tenant assignments for a product .

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import products_api
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
    api_instance = products_api.ProductsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Returns a list of tenant assignments for a product .
        api_response = api_instance.get_product_assignments_list(id)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling ProductsApi->get_product_assignments_list: %s\n" % e)
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

# **get_products_count**
> int get_products_count()

Returns the number of products.

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import products_api
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
    api_instance = products_api.ProductsApi(api_client)
    tenant_id = "tenantId_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns the number of products.
        api_response = api_instance.get_products_count(tenant_id=tenant_id)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling ProductsApi->get_products_count: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **get_products_page**
> ProductsPage get_products_page(page, page_size)

Returns a page of products.

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import products_api
from python_msx_sdk.model.products_page import ProductsPage
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
    api_instance = products_api.ProductsApi(api_client)
    page = 0 # int | 
    page_size = 10 # int | 
    tenant_id = "tenantId_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a page of products.
        api_response = api_instance.get_products_page(page, page_size)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling ProductsApi->get_products_page: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a page of products.
        api_response = api_instance.get_products_page(page, page_size, tenant_id=tenant_id)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling ProductsApi->get_products_page: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  |
 **page_size** | **int**|  |
 **tenant_id** | **str**|  | [optional]

### Return type

[**ProductsPage**](ProductsPage.md)

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

# **update_product**
> Product update_product(id, product_update)

Updates a product.

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import products_api
from python_msx_sdk.model.product import Product
from python_msx_sdk.model.product_update import ProductUpdate
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
    api_instance = products_api.ProductsApi(api_client)
    id = "id_example" # str | 
    product_update = ProductUpdate(
        name="name_example",
        label="label_example",
        version=1,
        description="description_example",
        image="image_example",
        multiple_instance_allowed=True,
        price="price_example",
        display_order=1,
        active=True,
        order_limit=1,
        options=[
            ServiceElement(
                name="name_example",
                label="label_example",
                header="header_example",
                description="description_example",
                hint="hint_example",
                input_type="input_type_example",
                type="type_example",
                component="component_example",
                max_limit="max_limit_example",
                min_limit="min_limit_example",
                value="value_example",
                value_list=[
                    {},
                ],
                allowed_option_values=[
                    "allowed_option_values_example",
                ],
                allowed_values=[
                    {
                        "key": None,
                    },
                ],
                mandatory=True,
                section="section_example",
                billable=True,
                hidden=True,
                parent_name="parent_name_example",
                supported=True,
                dynamic_data=True,
                min_value=1,
                max_value=1,
                step_size=1,
                pricing_atttributes=ServiceElementPrice(
                    one_time_price="one_time_price_example",
                    periodic_price="periodic_price_example",
                    time_period="time_period_example",
                    unit_of_measure="unit_of_measure_example",
                    included_quantity=1,
                    additional_one_time_price="additional_one_time_price_example",
                    additional_periodic_price="additional_periodic_price_example",
                    additional_quantity=1,
                ),
                child_elements=[
                    ServiceElement(ServiceElement),
                ],
            ),
        ],
        properties=[
            ServiceElement(
                name="name_example",
                label="label_example",
                header="header_example",
                description="description_example",
                hint="hint_example",
                input_type="input_type_example",
                type="type_example",
                component="component_example",
                max_limit="max_limit_example",
                min_limit="min_limit_example",
                value="value_example",
                value_list=None,
                allowed_option_values=[],
                allowed_values=None,
                mandatory=True,
                section="section_example",
                billable=True,
                hidden=True,
                parent_name="parent_name_example",
                supported=True,
                dynamic_data=True,
                min_value=1,
                max_value=1,
                step_size=1,
                pricing_atttributes=ServiceElementPrice(
                    one_time_price="one_time_price_example",
                    periodic_price="periodic_price_example",
                    time_period="time_period_example",
                    unit_of_measure="unit_of_measure_example",
                    included_quantity=1,
                    additional_one_time_price="additional_one_time_price_example",
                    additional_periodic_price="additional_periodic_price_example",
                    additional_quantity=1,
                ),
                child_elements=None,
            ),
        ],
        configuration={
            "key": "key_example",
        },
        is_resource=True,
        has_children=True,
        parent_id="parent_id_example",
        service_extensions=[
            NSOConfigDataXPath(
                service_instance_x_path="service_instance_x_path_example",
                service_type="service_type_example",
                possible_x_path_locations=[
                    "possible_x_path_locations_example",
                ],
            ),
        ],
        service_config_query_root_x_paths=[
            "service_config_query_root_x_paths_example",
        ],
        ui_config=ServiceUIConfig(
            banner_image="banner_image_example",
            links=[
                ServiceUILink(
                    type="type_example",
                    label="label_example",
                    address="address_example",
                    target="target_example",
                ),
            ],
        ),
        slm_ui_config=ServiceSLMUIConfig(
            type="type_example",
            resources=[
                ServiceUIResource(
                    type="type_example",
                    href="href_example",
                ),
            ],
        ),
        external_id="external_id_example",
        tags=[
            "tags_example",
        ],
    ) # ProductUpdate | 

    # example passing only required values which don't have defaults set
    try:
        # Updates a product.
        api_response = api_instance.update_product(id, product_update)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling ProductsApi->update_product: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **product_update** | [**ProductUpdate**](ProductUpdate.md)|  |

### Return type

[**Product**](Product.md)

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

# **update_product_assignments**
> [CatalogAssignment] update_product_assignments(id, request_body)

Updates the tenant assignments for a product.

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import products_api
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
    api_instance = products_api.ProductsApi(api_client)
    id = "id_example" # str | 
    request_body = ["e8ff9360-c8f1-4f06-84d8-d8105bd29e1e","3c64b303-ec28-4fe2-99b5-13f521b92700","48feaddb-45d0-4126-a216-3e450bfdbba4"] # [str] | 

    # example passing only required values which don't have defaults set
    try:
        # Updates the tenant assignments for a product.
        api_response = api_instance.update_product_assignments(id, request_body)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling ProductsApi->update_product_assignments: %s\n" % e)
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

