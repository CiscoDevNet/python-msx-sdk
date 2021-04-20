# python_msx_sdk.RolesApi

All URIs are relative to *http://localhost:8765*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_role_by_name**](RolesApi.md#get_role_by_name) | **GET** /idm/api/v8/roles/name/{name} | Returns a role by name.
[**get_roles_list**](RolesApi.md#get_roles_list) | **GET** /idm/api/v8/roles/list | Returns a list of roles.


# **get_role_by_name**
> Role get_role_by_name(name)

Returns a role by name.

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import roles_api
from python_msx_sdk.model.role import Role
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
    api_instance = roles_api.RolesApi(api_client)
    name = "CONSUMER" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Returns a role by name.
        api_response = api_instance.get_role_by_name(name)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling RolesApi->get_role_by_name: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  |

### Return type

[**Role**](Role.md)

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

# **get_roles_list**
> [Role] get_roles_list(ids)

Returns a list of roles.

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import roles_api
from python_msx_sdk.model.role import Role
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
    api_instance = roles_api.RolesApi(api_client)
    ids = [
        "ids_example",
    ] # [str] | 

    # example passing only required values which don't have defaults set
    try:
        # Returns a list of roles.
        api_response = api_instance.get_roles_list(ids)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling RolesApi->get_roles_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **[str]**|  |

### Return type

[**[Role]**](Role.md)

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

