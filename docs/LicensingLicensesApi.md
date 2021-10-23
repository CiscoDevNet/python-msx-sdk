# python_msx_sdk.LicensingLicensesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_licenses_list**](LicensingLicensesApi.md#get_licenses_list) | **GET** /licensing/api/v8/licensing/api/v8/licenses/list | Returns a filtered list of licenses.


# **get_licenses_list**
> [LicenseSummary] get_licenses_list(smart_account_id, virtual_account_id)

Returns a filtered list of licenses.

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import licensing_licenses_api
from python_msx_sdk.model.license_summary import LicenseSummary
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
    api_instance = licensing_licenses_api.LicensingLicensesApi(api_client)
    smart_account_id = "295183" # str | Smart Account Identifier
    virtual_account_id = "123123" # str | Virtual Account Identifier

    # example passing only required values which don't have defaults set
    try:
        # Returns a filtered list of licenses.
        api_response = api_instance.get_licenses_list(smart_account_id, virtual_account_id)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling LicensingLicensesApi->get_licenses_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **smart_account_id** | **str**| Smart Account Identifier |
 **virtual_account_id** | **str**| Virtual Account Identifier |

### Return type

[**[LicenseSummary]**](LicenseSummary.md)

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

