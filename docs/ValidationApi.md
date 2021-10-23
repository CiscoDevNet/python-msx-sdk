# python_msx_sdk.ValidationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_validate_product_version_page**](ValidationApi.md#get_validate_product_version_page) | **GET** /vulnerability/api/v8/vulnerabilities/validations | Returns a filtered page of validations.
[**validate_product_version**](ValidationApi.md#validate_product_version) | **POST** /vulnerability/api/v8/vulnerabilities/validations | Validate registered product / verison combinations for vulnerabilities.


# **get_validate_product_version_page**
> VulnerabilityValidationPage get_validate_product_version_page(page, page_size)

Returns a filtered page of validations.

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import validation_api
from python_msx_sdk.model.vulnerability_validation_page import VulnerabilityValidationPage
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
    api_instance = validation_api.ValidationApi(api_client)
    page = 0 # int | 
    page_size = 10 # int | 
    start_date = dateutil_parser('2020-01-15T18:15:00Z') # datetime | Start date for date range filter on validation execution date. (optional)
    end_date = dateutil_parser('2021-01-15T18:15:00Z') # datetime | End date for date range filter on validation execution date. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a filtered page of validations.
        api_response = api_instance.get_validate_product_version_page(page, page_size)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling ValidationApi->get_validate_product_version_page: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a filtered page of validations.
        api_response = api_instance.get_validate_product_version_page(page, page_size, start_date=start_date, end_date=end_date)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling ValidationApi->get_validate_product_version_page: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  |
 **page_size** | **int**|  |
 **start_date** | **datetime**| Start date for date range filter on validation execution date. | [optional]
 **end_date** | **datetime**| End date for date range filter on validation execution date. | [optional]

### Return type

[**VulnerabilityValidationPage**](VulnerabilityValidationPage.md)

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

# **validate_product_version**
> VulnerabilityValidation validate_product_version()

Validate registered product / verison combinations for vulnerabilities.

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import validation_api
from python_msx_sdk.model.vulnerability_validation import VulnerabilityValidation
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
    api_instance = validation_api.ValidationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Validate registered product / verison combinations for vulnerabilities.
        api_response = api_instance.validate_product_version()
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling ValidationApi->validate_product_version: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**VulnerabilityValidation**](VulnerabilityValidation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
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

