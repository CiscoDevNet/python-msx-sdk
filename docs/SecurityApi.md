# python_msx_sdk.SecurityApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_access_token**](SecurityApi.md#get_access_token) | **POST** /idm/v2/token | Returns an access token.


# **get_access_token**
> AccessToken get_access_token(authorization, grant_type)

Returns an access token.

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import security_api
from python_msx_sdk.model.access_token import AccessToken
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = python_msx_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with python_msx_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = security_api.SecurityApi(api_client)
    authorization = "Authorization_example" # str | 
    grant_type = "grant_type_example" # str | 
    username = "username_example" # str |  (optional)
    password = "password_example" # str |  (optional)
    access_token = "access_token_example" # str |  (optional)
    switch_username = "switch_username_example" # str |  (optional)
    tenant_id = "tenant_id_example" # str |  (optional)
    scope = "scope_example" # str |  (optional)
    nonce = "nonce_example" # str |  (optional)
    tenant_name = "tenant_name_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns an access token.
        api_response = api_instance.get_access_token(authorization, grant_type)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling SecurityApi->get_access_token: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns an access token.
        api_response = api_instance.get_access_token(authorization, grant_type, username=username, password=password, access_token=access_token, switch_username=switch_username, tenant_id=tenant_id, scope=scope, nonce=nonce, tenant_name=tenant_name)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling SecurityApi->get_access_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **grant_type** | **str**|  |
 **username** | **str**|  | [optional]
 **password** | **str**|  | [optional]
 **access_token** | **str**|  | [optional]
 **switch_username** | **str**|  | [optional]
 **tenant_id** | **str**|  | [optional]
 **scope** | **str**|  | [optional]
 **nonce** | **str**|  | [optional]
 **tenant_name** | **str**|  | [optional]

### Return type

[**AccessToken**](AccessToken.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

