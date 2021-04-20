# python_msx_sdk.HealthApi

All URIs are relative to *http://localhost:8765*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_devices_health_list**](HealthApi.md#get_devices_health_list) | **GET** /monitor/api/v8/health/devices/list | 
[**get_services_health_list**](HealthApi.md#get_services_health_list) | **GET** /monitor/api/v8/health/services/list | 


# **get_devices_health_list**
> [ResourceHealth] get_devices_health_list(ids)



### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import health_api
from python_msx_sdk.model.resource_health import ResourceHealth
from python_msx_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8765
# See configuration.py for a list of all supported configuration parameters.
configuration = python_msx_sdk.Configuration(
    host = "http://localhost:8765"
)


# Enter a context with an instance of the API client
with python_msx_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = health_api.HealthApi(api_client)
    ids = [
        "ids_example",
    ] # [str] | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_devices_health_list(ids)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling HealthApi->get_devices_health_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **[str]**|  |

### Return type

[**[ResourceHealth]**](ResourceHealth.md)

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

# **get_services_health_list**
> [ResourceHealth] get_services_health_list(ids)



### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import health_api
from python_msx_sdk.model.resource_health import ResourceHealth
from python_msx_sdk.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8765
# See configuration.py for a list of all supported configuration parameters.
configuration = python_msx_sdk.Configuration(
    host = "http://localhost:8765"
)


# Enter a context with an instance of the API client
with python_msx_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = health_api.HealthApi(api_client)
    ids = [
        "ids_example",
    ] # [str] | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_services_health_list(ids)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling HealthApi->get_services_health_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **[str]**|  |

### Return type

[**[ResourceHealth]**](ResourceHealth.md)

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

