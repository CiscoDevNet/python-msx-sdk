# python_msx_sdk.BillingCyclesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_billing_cycle**](BillingCyclesApi.md#add_billing_cycle) | **POST** /billing/api/v8/cycles | Add a billing cycle.
[**delete_billing_cycle**](BillingCyclesApi.md#delete_billing_cycle) | **DELETE** /billing/api/v8/cycles/{id} | Delete a billing cycle.
[**get_billing_cycle**](BillingCyclesApi.md#get_billing_cycle) | **GET** /billing/api/v8/cycles/{id} | Get a billing cycle.
[**get_billing_cycles_page**](BillingCyclesApi.md#get_billing_cycles_page) | **GET** /billing/api/v8/cycles | Retrieve a page of billing cycles.
[**process_billing_cycle**](BillingCyclesApi.md#process_billing_cycle) | **POST** /billing/api/v8/cycles/process | Process a billing cycle.
[**update_billing_cycle**](BillingCyclesApi.md#update_billing_cycle) | **PUT** /billing/api/v8/cycles/{id} | Update billing cycle for an event type and tenant.


# **add_billing_cycle**
> BillingCycle add_billing_cycle(billing_cycle_create)

Add a billing cycle.

Needs MANAGE_BILLINGCYCLE permission to allow for the creation a billing cycle.

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import billing_cycles_api
from python_msx_sdk.model.billing_cycle_create import BillingCycleCreate
from python_msx_sdk.model.billing_cycle import BillingCycle
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
    api_instance = billing_cycles_api.BillingCyclesApi(api_client)
    billing_cycle_create = BillingCycleCreate() # BillingCycleCreate | 

    # example passing only required values which don't have defaults set
    try:
        # Add a billing cycle.
        api_response = api_instance.add_billing_cycle(billing_cycle_create)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling BillingCyclesApi->add_billing_cycle: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **billing_cycle_create** | [**BillingCycleCreate**](BillingCycleCreate.md)|  |

### Return type

[**BillingCycle**](BillingCycle.md)

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

# **delete_billing_cycle**
> delete_billing_cycle(id)

Delete a billing cycle.

Needs MANAGE_BILLINGCYCLE permission to delete a billing cycle.

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import billing_cycles_api
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
    api_instance = billing_cycles_api.BillingCyclesApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete a billing cycle.
        api_instance.delete_billing_cycle(id)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling BillingCyclesApi->delete_billing_cycle: %s\n" % e)
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

# **get_billing_cycle**
> BillingCycle get_billing_cycle(id)

Get a billing cycle.

Needs VIEW_BILLINGCYCLE permission to get billing cycle detail.

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import billing_cycles_api
from python_msx_sdk.model.billing_cycle import BillingCycle
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
    api_instance = billing_cycles_api.BillingCyclesApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get a billing cycle.
        api_response = api_instance.get_billing_cycle(id)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling BillingCyclesApi->get_billing_cycle: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**BillingCycle**](BillingCycle.md)

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

# **get_billing_cycles_page**
> BillingCyclesPage get_billing_cycles_page(tenant_id, page, page_size)

Retrieve a page of billing cycles.

Needs VIEW_BILLINGCYCLE permission to view the billing cycle details.

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import billing_cycles_api
from python_msx_sdk.model.billing_cycles_page import BillingCyclesPage
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
    api_instance = billing_cycles_api.BillingCyclesApi(api_client)
    tenant_id = "tenantId_example" # str | 
    page = 0 # int | 
    page_size = 10 # int | 
    next_billed_on = dateutil_parser('2020-09-18T18:37:33.81Z') # datetime |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a page of billing cycles.
        api_response = api_instance.get_billing_cycles_page(tenant_id, page, page_size)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling BillingCyclesApi->get_billing_cycles_page: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve a page of billing cycles.
        api_response = api_instance.get_billing_cycles_page(tenant_id, page, page_size, next_billed_on=next_billed_on)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling BillingCyclesApi->get_billing_cycles_page: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  |
 **page** | **int**|  |
 **page_size** | **int**|  |
 **next_billed_on** | **datetime**|  | [optional]

### Return type

[**BillingCyclesPage**](BillingCyclesPage.md)

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

# **process_billing_cycle**
> BillingCycleProcessAccepted process_billing_cycle(billing_cycle_process)

Process a billing cycle.

Needs MANAGE_BILLINGCYCLE permission to allow for the creation a billing cycle.

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import billing_cycles_api
from python_msx_sdk.model.billing_cycle_process import BillingCycleProcess
from python_msx_sdk.model.billing_cycle_process_accepted import BillingCycleProcessAccepted
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
    api_instance = billing_cycles_api.BillingCyclesApi(api_client)
    billing_cycle_process = BillingCycleProcess(
        next_billed_on="2020-09-18T18:37:33.810Z",
    ) # BillingCycleProcess | 

    # example passing only required values which don't have defaults set
    try:
        # Process a billing cycle.
        api_response = api_instance.process_billing_cycle(billing_cycle_process)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling BillingCyclesApi->process_billing_cycle: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **billing_cycle_process** | [**BillingCycleProcess**](BillingCycleProcess.md)|  |

### Return type

[**BillingCycleProcessAccepted**](BillingCycleProcessAccepted.md)

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

# **update_billing_cycle**
> BillingCycle update_billing_cycle(id, billing_cycle_update)

Update billing cycle for an event type and tenant.

Needs MANAGE_BILLINGCYCLE permission to update a billing cycle detail.

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import billing_cycles_api
from python_msx_sdk.model.billing_cycle_update import BillingCycleUpdate
from python_msx_sdk.model.billing_cycle import BillingCycle
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
    api_instance = billing_cycles_api.BillingCyclesApi(api_client)
    id = "id_example" # str | 
    billing_cycle_update = BillingCycleUpdate(
        event_id="event_id_example",
        last_billed_on="2020-09-18T18:37:33.810Z",
        next_billed_on="2020-09-18T18:37:33.810Z",
        tenant_id="tenant_id_example",
    ) # BillingCycleUpdate | 

    # example passing only required values which don't have defaults set
    try:
        # Update billing cycle for an event type and tenant.
        api_response = api_instance.update_billing_cycle(id, billing_cycle_update)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling BillingCyclesApi->update_billing_cycle: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **billing_cycle_update** | [**BillingCycleUpdate**](BillingCycleUpdate.md)|  |

### Return type

[**BillingCycle**](BillingCycle.md)

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

