# python_msx_sdk.AuditingGenericEventsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_generic_event**](AuditingGenericEventsApi.md#create_generic_event) | **POST** /auditing/api/v8/genericevents | Create Generic Event


# **create_generic_event**
> GenericEvent create_generic_event(generic_event_create)

Create Generic Event

Needs CREATE_AUDIT_GENERIC_EVENT_PERMISSION to create a Generic Event.

### Example


```python
import time
import python_msx_sdk
from python_msx_sdk.api import auditing_generic_events_api
from python_msx_sdk.model.generic_event import GenericEvent
from python_msx_sdk.model.generic_event_create import GenericEventCreate
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
    api_instance = auditing_generic_events_api.AuditingGenericEventsApi(api_client)
    generic_event_create = GenericEventCreate(
        severity=GenericEventSeverity("CRITICAL"),
        subtype="subtype_example",
        service="service_example",
        keywords="keyword_1 keyword_2 keyword_3",
        details={
            "key": "key_example",
        },
        trace=GenericEventTrace(
            trace_id="trace_id_example",
            span_id="span_id_example",
            parent_id="parent_id_example",
        ),
        security=GenericEventSecurity(
            client_id="client_id_example",
            user_id="user_id_example",
            username="username_example",
            tenant_id="tenant_id_example",
            tenant_name="tenant_name_example",
            provider_id="provider_id_example",
            original_username="original_username_example",
        ),
        description="description_example",
    ) # GenericEventCreate | 

    # example passing only required values which don't have defaults set
    try:
        # Create Generic Event
        api_response = api_instance.create_generic_event(generic_event_create)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling AuditingGenericEventsApi->create_generic_event: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generic_event_create** | [**GenericEventCreate**](GenericEventCreate.md)|  |

### Return type

[**GenericEvent**](GenericEvent.md)

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

