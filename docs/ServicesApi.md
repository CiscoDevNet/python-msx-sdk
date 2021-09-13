# python_msx_sdk.ServicesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_service**](ServicesApi.md#delete_service) | **DELETE** /manage/api/v8/services/{id} | Deletes a service.
[**get_service**](ServicesApi.md#get_service) | **GET** /manage/api/v8/services/{id} | Returns a service.
[**get_services_page**](ServicesApi.md#get_services_page) | **GET** /manage/api/v8/services | Returns a page of services.
[**submit_order**](ServicesApi.md#submit_order) | **POST** /manage/api/v8/services | Submits an order.
[**update_order**](ServicesApi.md#update_order) | **PUT** /manage/api/v8/services | Updates an order.
[**update_service**](ServicesApi.md#update_service) | **PUT** /manage/api/v8/services/{id} | Updates a service.


# **delete_service**
> delete_service(id)

Deletes a service.

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import services_api
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
    api_instance = services_api.ServicesApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Deletes a service.
        api_instance.delete_service(id)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling ServicesApi->delete_service: %s\n" % e)
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

# **get_service**
> Service get_service(id)

Returns a service.

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import services_api
from python_msx_sdk.model.service import Service
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
    api_instance = services_api.ServicesApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Returns a service.
        api_response = api_instance.get_service(id)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling ServicesApi->get_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**Service**](Service.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthenticated |  -  |
**403** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_services_page**
> ServicesPage get_services_page(page, page_size)

Returns a page of services.

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import services_api
from python_msx_sdk.model.services_page import ServicesPage
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
    api_instance = services_api.ServicesApi(api_client)
    page = 0 # int | 
    page_size = 10 # int | 
    tenant_ids = [
        "tenantIds_example",
    ] # [str] |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a page of services.
        api_response = api_instance.get_services_page(page, page_size)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling ServicesApi->get_services_page: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a page of services.
        api_response = api_instance.get_services_page(page, page_size, tenant_ids=tenant_ids)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling ServicesApi->get_services_page: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  |
 **page_size** | **int**|  |
 **tenant_ids** | **[str]**|  | [optional]

### Return type

[**ServicesPage**](ServicesPage.md)

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

# **submit_order**
> LegacyServiceOrderResponse submit_order(product_id, offer_id, legacy_service_order)

Submits an order.

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import services_api
from python_msx_sdk.model.legacy_service_order import LegacyServiceOrder
from python_msx_sdk.model.legacy_service_order_response import LegacyServiceOrderResponse
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
    api_instance = services_api.ServicesApi(api_client)
    product_id = "productId_example" # str | 
    offer_id = "offerId_example" # str | 
    legacy_service_order = LegacyServiceOrder(
        message_id="message_id_example",
        type="type_example",
        service_type="service_type_example",
        action="action_example",
        schedule=LegacyScheduleConfig(
            method="method_example",
            relative=LegacyRelativeConfig(
                schedule_in="2h 10m 30s",
            ),
            absolute=LegacyAbsoluteConfig(
                date_time="2017-08-01 13:56:44 -0700",
            ),
        ),
        payload=LegacyServiceOrderDetail(
            service={
                "key": "key_example",
            },
            tenant={
                "key": "key_example",
            },
            user={
                "key": "key_example",
            },
            provider={
                "key": "key_example",
            },
            offer={
                "key": "key_example",
            },
            cost={
                "key": "key_example",
            },
            subscription_id="subscription_id_example",
            subscription_name="subscription_name_example",
            subscription_detail=LegacySubscriptionDetail(
                site_count={},
                sites=[
                    LegacySite(
                        site_id="site_id_example",
                        site_name="site_name_example",
                        display_name="display_name_example",
                        address=LegacyAddress(
                            name="name_example",
                            display_name="display_name_example",
                            company="company_example",
                            address1="address1_example",
                            address2="address2_example",
                            city="city_example",
                            state="state_example",
                            country="country_example",
                            post_code="post_code_example",
                        ),
                        devices=[
                            LegacySiteDevice(
                                device_id="device_id_example",
                                name="name_example",
                                model="model_example",
                                type="type_example",
                                device_attributes={
                                    "key": None,
                                },
                                device_onboarding=LegacySiteDeviceOnboard(
                                    device_instance_id="device_instance_id_example",
                                    tenant_id="tenant_id_example",
                                    device_name="device_name_example",
                                    managed=True,
                                    device_model="device_model_example",
                                    device_onboarding_type="device_onboarding_type_example",
                                    device_onboard_information={
                                        "key": None,
                                    },
                                ),
                                delete=True,
                            ),
                        ],
                        site_attributes={
                            "key": None,
                        },
                        delete=True,
                        operational_status="operational_status_example",
                    ),
                ],
                offer_selection={
                    "key": None,
                },
                service_instance_detail={
                    "key": None,
                },
                price_detail={
                    "key": None,
                },
                dealer_code="dealer_code_example",
                price_plan_id="price_plan_id_example",
                terms_and_condition_id="terms_and_condition_id_example",
                configuration={
                    "key": "key_example",
                },
            ),
            service_downgrade={
                "key": None,
            },
            nso_response_types=LegacyNsoResponseTypes(
                create_operation="create_operation_example",
                update_operation="update_operation_example",
                delete_operation="delete_operation_example",
            ),
        ),
        transaction_uuid="transaction_uuid_example",
    ) # LegacyServiceOrder | 

    # example passing only required values which don't have defaults set
    try:
        # Submits an order.
        api_response = api_instance.submit_order(product_id, offer_id, legacy_service_order)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling ServicesApi->submit_order: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**|  |
 **offer_id** | **str**|  |
 **legacy_service_order** | [**LegacyServiceOrder**](LegacyServiceOrder.md)|  |

### Return type

[**LegacyServiceOrderResponse**](LegacyServiceOrderResponse.md)

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

# **update_order**
> LegacyServiceOrderResponse update_order(product_id, offer_id, legacy_service_order)

Updates an order.

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import services_api
from python_msx_sdk.model.legacy_service_order import LegacyServiceOrder
from python_msx_sdk.model.legacy_service_order_response import LegacyServiceOrderResponse
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
    api_instance = services_api.ServicesApi(api_client)
    product_id = "productId_example" # str | 
    offer_id = "offerId_example" # str | 
    legacy_service_order = LegacyServiceOrder(
        message_id="message_id_example",
        type="type_example",
        service_type="service_type_example",
        action="action_example",
        schedule=LegacyScheduleConfig(
            method="method_example",
            relative=LegacyRelativeConfig(
                schedule_in="2h 10m 30s",
            ),
            absolute=LegacyAbsoluteConfig(
                date_time="2017-08-01 13:56:44 -0700",
            ),
        ),
        payload=LegacyServiceOrderDetail(
            service={
                "key": "key_example",
            },
            tenant={
                "key": "key_example",
            },
            user={
                "key": "key_example",
            },
            provider={
                "key": "key_example",
            },
            offer={
                "key": "key_example",
            },
            cost={
                "key": "key_example",
            },
            subscription_id="subscription_id_example",
            subscription_name="subscription_name_example",
            subscription_detail=LegacySubscriptionDetail(
                site_count={},
                sites=[
                    LegacySite(
                        site_id="site_id_example",
                        site_name="site_name_example",
                        display_name="display_name_example",
                        address=LegacyAddress(
                            name="name_example",
                            display_name="display_name_example",
                            company="company_example",
                            address1="address1_example",
                            address2="address2_example",
                            city="city_example",
                            state="state_example",
                            country="country_example",
                            post_code="post_code_example",
                        ),
                        devices=[
                            LegacySiteDevice(
                                device_id="device_id_example",
                                name="name_example",
                                model="model_example",
                                type="type_example",
                                device_attributes={
                                    "key": None,
                                },
                                device_onboarding=LegacySiteDeviceOnboard(
                                    device_instance_id="device_instance_id_example",
                                    tenant_id="tenant_id_example",
                                    device_name="device_name_example",
                                    managed=True,
                                    device_model="device_model_example",
                                    device_onboarding_type="device_onboarding_type_example",
                                    device_onboard_information={
                                        "key": None,
                                    },
                                ),
                                delete=True,
                            ),
                        ],
                        site_attributes={
                            "key": None,
                        },
                        delete=True,
                        operational_status="operational_status_example",
                    ),
                ],
                offer_selection={
                    "key": None,
                },
                service_instance_detail={
                    "key": None,
                },
                price_detail={
                    "key": None,
                },
                dealer_code="dealer_code_example",
                price_plan_id="price_plan_id_example",
                terms_and_condition_id="terms_and_condition_id_example",
                configuration={
                    "key": "key_example",
                },
            ),
            service_downgrade={
                "key": None,
            },
            nso_response_types=LegacyNsoResponseTypes(
                create_operation="create_operation_example",
                update_operation="update_operation_example",
                delete_operation="delete_operation_example",
            ),
        ),
        transaction_uuid="transaction_uuid_example",
    ) # LegacyServiceOrder | 

    # example passing only required values which don't have defaults set
    try:
        # Updates an order.
        api_response = api_instance.update_order(product_id, offer_id, legacy_service_order)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling ServicesApi->update_order: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**|  |
 **offer_id** | **str**|  |
 **legacy_service_order** | [**LegacyServiceOrder**](LegacyServiceOrder.md)|  |

### Return type

[**LegacyServiceOrderResponse**](LegacyServiceOrderResponse.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_service**
> Service update_service(id, service_update)

Updates a service.

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import services_api
from python_msx_sdk.model.service import Service
from python_msx_sdk.model.error import Error
from python_msx_sdk.model.service_update import ServiceUpdate
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = python_msx_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with python_msx_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = services_api.ServicesApi(api_client)
    id = "id_example" # str | 
    service_update = ServiceUpdate(
        status={
            "key": None,
        },
        definition_attributes={},
        attributes={},
    ) # ServiceUpdate | 

    # example passing only required values which don't have defaults set
    try:
        # Updates a service.
        api_response = api_instance.update_service(id, service_update)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling ServicesApi->update_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **service_update** | [**ServiceUpdate**](ServiceUpdate.md)|  |

### Return type

[**Service**](Service.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

