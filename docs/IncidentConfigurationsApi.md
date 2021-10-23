# python_msx_sdk.IncidentConfigurationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_service_now_configuration**](IncidentConfigurationsApi.md#create_service_now_configuration) | **POST** /incident/api/v8/configurations | Creates a ServiceNow configuration.
[**delete_service_now_configuration**](IncidentConfigurationsApi.md#delete_service_now_configuration) | **DELETE** /incident/api/v8/configurations/{id} | Deletes a ServiceNow configuration.
[**get_configuration**](IncidentConfigurationsApi.md#get_configuration) | **GET** /incident/api/v1/config | API to get configuration of encloud service.
[**get_service_now_configuration**](IncidentConfigurationsApi.md#get_service_now_configuration) | **GET** /incident/api/v8/configurations/{id} | Returns a ServiceNow configuration.
[**get_service_now_configurations_page**](IncidentConfigurationsApi.md#get_service_now_configurations_page) | **GET** /incident/api/v8/configurations | Returns a ServiceNow configurations.
[**patch_configuration**](IncidentConfigurationsApi.md#patch_configuration) | **PATCH** /incident/api/v1/config | API to patch configure encloud service
[**update_configuration**](IncidentConfigurationsApi.md#update_configuration) | **PUT** /incident/api/v1/config | API to configure encloud service.


# **create_service_now_configuration**
> ServiceNowConfiguration create_service_now_configuration(service_now_configuration_create)

Creates a ServiceNow configuration.

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import incident_configurations_api
from python_msx_sdk.model.service_now_configuration import ServiceNowConfiguration
from python_msx_sdk.model.service_now_configuration_create import ServiceNowConfigurationCreate
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
    api_instance = incident_configurations_api.IncidentConfigurationsApi(api_client)
    service_now_configuration_create = ServiceNowConfigurationCreate() # ServiceNowConfigurationCreate | 

    # example passing only required values which don't have defaults set
    try:
        # Creates a ServiceNow configuration.
        api_response = api_instance.create_service_now_configuration(service_now_configuration_create)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling IncidentConfigurationsApi->create_service_now_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_now_configuration_create** | [**ServiceNowConfigurationCreate**](ServiceNowConfigurationCreate.md)|  |

### Return type

[**ServiceNowConfiguration**](ServiceNowConfiguration.md)

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

# **delete_service_now_configuration**
> delete_service_now_configuration(id)

Deletes a ServiceNow configuration.

Delete service now configuration, only if no associated entities exists.

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import incident_configurations_api
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
    api_instance = incident_configurations_api.IncidentConfigurationsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Deletes a ServiceNow configuration.
        api_instance.delete_service_now_configuration(id)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling IncidentConfigurationsApi->delete_service_now_configuration: %s\n" % e)
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
**400** | Bad Request |  -  |
**401** | Unauthenticated |  -  |
**403** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_configuration**
> IncidentConfig get_configuration()

API to get configuration of encloud service.

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import incident_configurations_api
from python_msx_sdk.model.incident_config import IncidentConfig
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
    api_instance = incident_configurations_api.IncidentConfigurationsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # API to get configuration of encloud service.
        api_response = api_instance.get_configuration()
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling IncidentConfigurationsApi->get_configuration: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**IncidentConfig**](IncidentConfig.md)

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

# **get_service_now_configuration**
> ServiceNowConfiguration get_service_now_configuration(id)

Returns a ServiceNow configuration.

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import incident_configurations_api
from python_msx_sdk.model.service_now_configuration import ServiceNowConfiguration
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
    api_instance = incident_configurations_api.IncidentConfigurationsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Returns a ServiceNow configuration.
        api_response = api_instance.get_service_now_configuration(id)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling IncidentConfigurationsApi->get_service_now_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**ServiceNowConfiguration**](ServiceNowConfiguration.md)

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

# **get_service_now_configurations_page**
> ServiceNowConfigurationsPage get_service_now_configurations_page(page, page_size)

Returns a ServiceNow configurations.

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import incident_configurations_api
from python_msx_sdk.model.service_now_configurations_page import ServiceNowConfigurationsPage
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
    api_instance = incident_configurations_api.IncidentConfigurationsApi(api_client)
    page = 0 # int | 
    page_size = 10 # int | 
    tenant_id = "tenantId_example" # str |  (optional)
    domain = "domain_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a ServiceNow configurations.
        api_response = api_instance.get_service_now_configurations_page(page, page_size)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling IncidentConfigurationsApi->get_service_now_configurations_page: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a ServiceNow configurations.
        api_response = api_instance.get_service_now_configurations_page(page, page_size, tenant_id=tenant_id, domain=domain)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling IncidentConfigurationsApi->get_service_now_configurations_page: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  |
 **page_size** | **int**|  |
 **tenant_id** | **str**|  | [optional]
 **domain** | **str**|  | [optional]

### Return type

[**ServiceNowConfigurationsPage**](ServiceNowConfigurationsPage.md)

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

# **patch_configuration**
> IncidentConfig patch_configuration(incident_config_patch)

API to patch configure encloud service

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import incident_configurations_api
from python_msx_sdk.model.incident_config import IncidentConfig
from python_msx_sdk.model.incident_config_patch import IncidentConfigPatch
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
    api_instance = incident_configurations_api.IncidentConfigurationsApi(api_client)
    incident_config_patch = IncidentConfigPatch(
        client_id="client_id_example",
        client_secret="client_secret_example",
        critical_event=True,
        domain="domain_example",
        password="password_example",
        user_name="user_name_example",
    ) # IncidentConfigPatch | 

    # example passing only required values which don't have defaults set
    try:
        # API to patch configure encloud service
        api_response = api_instance.patch_configuration(incident_config_patch)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling IncidentConfigurationsApi->patch_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **incident_config_patch** | [**IncidentConfigPatch**](IncidentConfigPatch.md)|  |

### Return type

[**IncidentConfig**](IncidentConfig.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_configuration**
> IncidentConfig update_configuration(incident_config_update)

API to configure encloud service.

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import incident_configurations_api
from python_msx_sdk.model.incident_config import IncidentConfig
from python_msx_sdk.model.incident_config_update import IncidentConfigUpdate
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
    api_instance = incident_configurations_api.IncidentConfigurationsApi(api_client)
    incident_config_update = IncidentConfigUpdate(
        client_id="client_id_example",
        client_secret="client_secret_example",
        critical_event=True,
        domain="domain_example",
        password="password_example",
        user_name="user_name_example",
        proxy="proxy_example",
    ) # IncidentConfigUpdate | 

    # example passing only required values which don't have defaults set
    try:
        # API to configure encloud service.
        api_response = api_instance.update_configuration(incident_config_update)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling IncidentConfigurationsApi->update_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **incident_config_update** | [**IncidentConfigUpdate**](IncidentConfigUpdate.md)|  |

### Return type

[**IncidentConfig**](IncidentConfig.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

