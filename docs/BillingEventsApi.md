# python_msx_sdk.BillingEventsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_cost_summary**](BillingEventsApi.md#get_cost_summary) | **GET** /billing/api/v8/events/costs | Retrieve a summary for tenant cost.
[**get_event**](BillingEventsApi.md#get_event) | **GET** /billing/api/v8/events/{id} | Get an Event.
[**get_events_page**](BillingEventsApi.md#get_events_page) | **GET** /billing/api/v8/events | Retrieve a page of events for tenant.


# **get_cost_summary**
> BillingCostsReport get_cost_summary(tenant_id)

Retrieve a summary for tenant cost.

Needs VIEW_COSTS permission to view cost details.

### Example


```python
import time
import python_msx_sdk
from python_msx_sdk.api import billing_events_api
from python_msx_sdk.model.billing_costs_report import BillingCostsReport
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
    api_instance = billing_events_api.BillingEventsApi(api_client)
    tenant_id = "tenantId_example" # str | 
    from_date = dateutil_parser('2020-09-18T18:37:33.81Z') # datetime |  (optional)
    to_date = dateutil_parser('2020-09-19T18:37:33.81Z') # datetime |  (optional)
    group_by = "type, subtype or service" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a summary for tenant cost.
        api_response = api_instance.get_cost_summary(tenant_id)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling BillingEventsApi->get_cost_summary: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve a summary for tenant cost.
        api_response = api_instance.get_cost_summary(tenant_id, from_date=from_date, to_date=to_date, group_by=group_by)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling BillingEventsApi->get_cost_summary: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  |
 **from_date** | **datetime**|  | [optional]
 **to_date** | **datetime**|  | [optional]
 **group_by** | **str**|  | [optional]

### Return type

[**BillingCostsReport**](BillingCostsReport.md)

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

# **get_event**
> BillingEvent get_event(id)

Get an Event.

Needs VIEW_EVENTS permission to get a billing event.

### Example


```python
import time
import python_msx_sdk
from python_msx_sdk.api import billing_events_api
from python_msx_sdk.model.billing_event import BillingEvent
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
    api_instance = billing_events_api.BillingEventsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get an Event.
        api_response = api_instance.get_event(id)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling BillingEventsApi->get_event: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**BillingEvent**](BillingEvent.md)

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

# **get_events_page**
> BillingEventsPage get_events_page(tenant_id, page, page_size)

Retrieve a page of events for tenant.

Needs VIEW_EVENTS permission to view the billing events.

### Example


```python
import time
import python_msx_sdk
from python_msx_sdk.api import billing_events_api
from python_msx_sdk.model.billing_events_page import BillingEventsPage
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
    api_instance = billing_events_api.BillingEventsApi(api_client)
    tenant_id = "tenantId_example" # str | 
    page = 0 # int | 
    page_size = 10 # int | 
    from_date = dateutil_parser('2020-09-18T18:37:33.81Z') # datetime |  (optional)
    to_date = dateutil_parser('2020-09-19T18:37:33.81Z') # datetime |  (optional)
    type = "type_example" # str |  (optional)
    subtype = "subtype_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a page of events for tenant.
        api_response = api_instance.get_events_page(tenant_id, page, page_size)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling BillingEventsApi->get_events_page: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve a page of events for tenant.
        api_response = api_instance.get_events_page(tenant_id, page, page_size, from_date=from_date, to_date=to_date, type=type, subtype=subtype)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling BillingEventsApi->get_events_page: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  |
 **page** | **int**|  |
 **page_size** | **int**|  |
 **from_date** | **datetime**|  | [optional]
 **to_date** | **datetime**|  | [optional]
 **type** | **str**|  | [optional]
 **subtype** | **str**|  | [optional]

### Return type

[**BillingEventsPage**](BillingEventsPage.md)

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

