# python_msx_sdk.LicensingAccountsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_user_accounts_list**](LicensingAccountsApi.md#get_user_accounts_list) | **GET** /licensing/api/v8/accounts/smart/list | Returns a filtered page of smart accounts.


# **get_user_accounts_list**
> SmartUserAccounts get_user_accounts_list(user_id)

Returns a filtered page of smart accounts.

### Example


```python
import time
import python_msx_sdk
from python_msx_sdk.api import licensing_accounts_api
from python_msx_sdk.model.smart_account_type import SmartAccountType
from python_msx_sdk.model.error import Error
from python_msx_sdk.model.smart_user_accounts import SmartUserAccounts
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = python_msx_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with python_msx_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = licensing_accounts_api.LicensingAccountsApi(api_client)
    user_id = "bdavis" # str | User Id
    domain = "abhtest001.cisco.com" # str | Smart Account domain (optional)
    role_name = "AccountAdmin" # str | Role Name (optional)
    type = SmartAccountType("CUSTOMER") # SmartAccountType |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a filtered page of smart accounts.
        api_response = api_instance.get_user_accounts_list(user_id)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling LicensingAccountsApi->get_user_accounts_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a filtered page of smart accounts.
        api_response = api_instance.get_user_accounts_list(user_id, domain=domain, role_name=role_name, type=type)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling LicensingAccountsApi->get_user_accounts_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User Id |
 **domain** | **str**| Smart Account domain | [optional]
 **role_name** | **str**| Role Name | [optional]
 **type** | **SmartAccountType**|  | [optional]

### Return type

[**SmartUserAccounts**](SmartUserAccounts.md)

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

