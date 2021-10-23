# python_msx_sdk.LicensingConfigurationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_smart_account_configuration**](LicensingConfigurationsApi.md#create_smart_account_configuration) | **POST** /licensing/api/v8/configuration | Creates a smart account configuration.
[**get_smart_account_configuration**](LicensingConfigurationsApi.md#get_smart_account_configuration) | **GET** /licensing/api/v8/configuration | Returns a smart account configuration.
[**update_smart_account_configuration**](LicensingConfigurationsApi.md#update_smart_account_configuration) | **PUT** /licensing/api/v8/configuration | Updates a smart account configuration.


# **create_smart_account_configuration**
> SmartAccountConfiguration create_smart_account_configuration(smart_account_configuration_create)

Creates a smart account configuration.

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import licensing_configurations_api
from python_msx_sdk.model.smart_account_configuration_create import SmartAccountConfigurationCreate
from python_msx_sdk.model.smart_account_configuration import SmartAccountConfiguration
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
    api_instance = licensing_configurations_api.LicensingConfigurationsApi(api_client)
    smart_account_configuration_create = SmartAccountConfigurationCreate() # SmartAccountConfigurationCreate | 

    # example passing only required values which don't have defaults set
    try:
        # Creates a smart account configuration.
        api_response = api_instance.create_smart_account_configuration(smart_account_configuration_create)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling LicensingConfigurationsApi->create_smart_account_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **smart_account_configuration_create** | [**SmartAccountConfigurationCreate**](SmartAccountConfigurationCreate.md)|  |

### Return type

[**SmartAccountConfiguration**](SmartAccountConfiguration.md)

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

# **get_smart_account_configuration**
> SmartAccountConfiguration get_smart_account_configuration()

Returns a smart account configuration.

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import licensing_configurations_api
from python_msx_sdk.model.smart_account_configuration import SmartAccountConfiguration
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
    api_instance = licensing_configurations_api.LicensingConfigurationsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Returns a smart account configuration.
        api_response = api_instance.get_smart_account_configuration()
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling LicensingConfigurationsApi->get_smart_account_configuration: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**SmartAccountConfiguration**](SmartAccountConfiguration.md)

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

# **update_smart_account_configuration**
> SmartAccountConfiguration update_smart_account_configuration(smart_account_configuration_update)

Updates a smart account configuration.

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import licensing_configurations_api
from python_msx_sdk.model.smart_account_configuration_update import SmartAccountConfigurationUpdate
from python_msx_sdk.model.smart_account_configuration import SmartAccountConfiguration
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
    api_instance = licensing_configurations_api.LicensingConfigurationsApi(api_client)
    smart_account_configuration_update = SmartAccountConfigurationUpdate(
        base_auth_url="base_auth_url_example",
        base_smart_url="base_smart_url_example",
        content_type="content_type_example",
        grant_type="grant_type_example",
        client_id="client_id_example",
        client_secret="client_secret_example",
    ) # SmartAccountConfigurationUpdate | 

    # example passing only required values which don't have defaults set
    try:
        # Updates a smart account configuration.
        api_response = api_instance.update_smart_account_configuration(smart_account_configuration_update)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling LicensingConfigurationsApi->update_smart_account_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **smart_account_configuration_update** | [**SmartAccountConfigurationUpdate**](SmartAccountConfigurationUpdate.md)|  |

### Return type

[**SmartAccountConfiguration**](SmartAccountConfiguration.md)

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

