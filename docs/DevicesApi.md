# python_msx_sdk.DevicesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attach_device_templates**](DevicesApi.md#attach_device_templates) | **POST** /manage/api/v8/devices/{id}/templates | Attaches one or more device templates to a device instance.
[**batch_attach_device_templates**](DevicesApi.md#batch_attach_device_templates) | **POST** /manage/api/v8/devices/templates/attach | Attaches one or more device templates to a batch of device instances.
[**create_device**](DevicesApi.md#create_device) | **POST** /manage/api/v8/devices | Creates a device.
[**delete_device**](DevicesApi.md#delete_device) | **DELETE** /manage/api/v8/devices/{id} | Deletes a device.
[**detach_device_template**](DevicesApi.md#detach_device_template) | **DELETE** /manage/api/v8/devices/{id}/templates/{templateId} | Detaches a template from a device.
[**detach_device_templates**](DevicesApi.md#detach_device_templates) | **DELETE** /manage/api/v8/devices/{id}/templates | Detach device templates that are already attached to a device.
[**get_device**](DevicesApi.md#get_device) | **GET** /manage/api/v8/devices/{id} | Returns a device.
[**get_device_config**](DevicesApi.md#get_device_config) | **GET** /manage/api/v8/devices/{id}/config | Returns the running configuration for a device.
[**get_device_template_history**](DevicesApi.md#get_device_template_history) | **GET** /manage/api/v8/devices/{id}/templates | Returns device template history.
[**get_devices_page**](DevicesApi.md#get_devices_page) | **GET** /manage/api/v8/devices | Returns a page of devices.
[**patch_device**](DevicesApi.md#patch_device) | **PATCH** /manage/api/v8/devices/{id} | Update a device.
[**redeploy_device**](DevicesApi.md#redeploy_device) | **POST** /manage/api/v8/devices/{id}/redeploy | Dedeploys a device.
[**update_device**](DevicesApi.md#update_device) | **PUT** /manage/api/v8/devices/{id} | Update a device.
[**update_device_templates**](DevicesApi.md#update_device_templates) | **PUT** /manage/api/v8/devices/{id}/templates | Update device templates that are already attached to a device.


# **attach_device_templates**
> [DeviceTemplateHistory] attach_device_templates(id, device_template_attach_request)

Attaches one or more device templates to a device instance.

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import devices_api
from python_msx_sdk.model.device_template_attach_request import DeviceTemplateAttachRequest
from python_msx_sdk.model.manage_change_request_pending import ManageChangeRequestPending
from python_msx_sdk.model.device_template_history import DeviceTemplateHistory
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
    api_instance = devices_api.DevicesApi(api_client)
    id = "id_example" # str | 
    device_template_attach_request = DeviceTemplateAttachRequest(
        template_details=[
            DeviceTemplateDetails(
                template_id="template_id_example",
                template_params=[
                    NameValue(
                        name="name_example",
                        value="value_example",
                    ),
                ],
            ),
        ],
    ) # DeviceTemplateAttachRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Attaches one or more device templates to a device instance.
        api_response = api_instance.attach_device_templates(id, device_template_attach_request)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling DevicesApi->attach_device_templates: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **device_template_attach_request** | [**DeviceTemplateAttachRequest**](DeviceTemplateAttachRequest.md)|  |

### Return type

[**[DeviceTemplateHistory]**](DeviceTemplateHistory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**202** | Pending Approval |  -  |
**400** | Bad Request |  -  |
**401** | Unauthenticated |  -  |
**403** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **batch_attach_device_templates**
> [DeviceTemplateBatchAttachResponse] batch_attach_device_templates(device_template_batch_attach_request)

Attaches one or more device templates to a batch of device instances.

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import devices_api
from python_msx_sdk.model.manage_change_request_pending import ManageChangeRequestPending
from python_msx_sdk.model.device_template_batch_attach_request import DeviceTemplateBatchAttachRequest
from python_msx_sdk.model.device_template_batch_attach_response import DeviceTemplateBatchAttachResponse
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
    api_instance = devices_api.DevicesApi(api_client)
    device_template_batch_attach_request = DeviceTemplateBatchAttachRequest(
        device_ids=[
            "device_ids_example",
        ],
        template_details=[
            DeviceTemplateDetails(
                template_id="template_id_example",
                template_params=[
                    NameValue(
                        name="name_example",
                        value="value_example",
                    ),
                ],
            ),
        ],
    ) # DeviceTemplateBatchAttachRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Attaches one or more device templates to a batch of device instances.
        api_response = api_instance.batch_attach_device_templates(device_template_batch_attach_request)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling DevicesApi->batch_attach_device_templates: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_template_batch_attach_request** | [**DeviceTemplateBatchAttachRequest**](DeviceTemplateBatchAttachRequest.md)|  |

### Return type

[**[DeviceTemplateBatchAttachResponse]**](DeviceTemplateBatchAttachResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Pending Approval |  -  |
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthenticated |  -  |
**403** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_device**
> Device create_device(device_create)

Creates a device.

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import devices_api
from python_msx_sdk.model.device import Device
from python_msx_sdk.model.device_create import DeviceCreate
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
    api_instance = devices_api.DevicesApi(api_client)
    device_create = DeviceCreate() # DeviceCreate | 

    # example passing only required values which don't have defaults set
    try:
        # Creates a device.
        api_response = api_instance.create_device(device_create)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling DevicesApi->create_device: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_create** | [**DeviceCreate**](DeviceCreate.md)|  |

### Return type

[**Device**](Device.md)

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

# **delete_device**
> delete_device(id)

Deletes a device.

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import devices_api
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
    api_instance = devices_api.DevicesApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Deletes a device.
        api_instance.delete_device(id)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling DevicesApi->delete_device: %s\n" % e)
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

# **detach_device_template**
> [DeviceTemplateHistory] detach_device_template(id, template_id)

Detaches a template from a device.

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import devices_api
from python_msx_sdk.model.device_template_history import DeviceTemplateHistory
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
    api_instance = devices_api.DevicesApi(api_client)
    id = "id_example" # str | 
    template_id = "templateId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Detaches a template from a device.
        api_response = api_instance.detach_device_template(id, template_id)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling DevicesApi->detach_device_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **template_id** | **str**|  |

### Return type

[**[DeviceTemplateHistory]**](DeviceTemplateHistory.md)

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

# **detach_device_templates**
> [DeviceTemplateHistory] detach_device_templates(id)

Detach device templates that are already attached to a device.

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import devices_api
from python_msx_sdk.model.manage_change_request_pending import ManageChangeRequestPending
from python_msx_sdk.model.device_template_history import DeviceTemplateHistory
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
    api_instance = devices_api.DevicesApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Detach device templates that are already attached to a device.
        api_response = api_instance.detach_device_templates(id)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling DevicesApi->detach_device_templates: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**[DeviceTemplateHistory]**](DeviceTemplateHistory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthenticated |  -  |
**403** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device**
> Device get_device(id)

Returns a device.

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import devices_api
from python_msx_sdk.model.device import Device
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
    api_instance = devices_api.DevicesApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Returns a device.
        api_response = api_instance.get_device(id)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling DevicesApi->get_device: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**Device**](Device.md)

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

# **get_device_config**
> str get_device_config(id)

Returns the running configuration for a device.

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import devices_api
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
    api_instance = devices_api.DevicesApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Returns the running configuration for a device.
        api_response = api_instance.get_device_config(id)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling DevicesApi->get_device_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json


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

# **get_device_template_history**
> [DeviceTemplateHistory] get_device_template_history(id)

Returns device template history.

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import devices_api
from python_msx_sdk.model.device_template_history import DeviceTemplateHistory
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
    api_instance = devices_api.DevicesApi(api_client)
    id = "id_example" # str | 
    template_id = "templateId_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns device template history.
        api_response = api_instance.get_device_template_history(id)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling DevicesApi->get_device_template_history: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns device template history.
        api_response = api_instance.get_device_template_history(id, template_id=template_id)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling DevicesApi->get_device_template_history: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **template_id** | **str**|  | [optional]

### Return type

[**[DeviceTemplateHistory]**](DeviceTemplateHistory.md)

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

# **get_devices_page**
> DevicesPage get_devices_page(page, page_size)

Returns a page of devices.

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import devices_api
from python_msx_sdk.model.device_compliance_state import DeviceComplianceState
from python_msx_sdk.model.devices_page import DevicesPage
from python_msx_sdk.model.device_vulnerability_state import DeviceVulnerabilityState
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
    api_instance = devices_api.DevicesApi(api_client)
    page = 0 # int | 
    page_size = 10 # int | 
    device_ids = [
        "deviceIds_example",
    ] # [str] |  (optional)
    service_ids = [
        "serviceIds_example",
    ] # [str] |  (optional)
    types = [
        "types_example",
    ] # [str] |  (optional)
    serial_keys = [
        "serialKeys_example",
    ] # [str] |  (optional)
    service_types = [
        "serviceTypes_example",
    ] # [str] |  (optional)
    models = [
        "models_example",
    ] # [str] |  (optional)
    subtypes = [
        "subtypes_example",
    ] # [str] |  (optional)
    names = [
        "names_example",
    ] # [str] |  (optional)
    versions = [
        "versions_example",
    ] # [str] |  (optional)
    tenant_ids = [
        "tenantIds_example",
    ] # [str] |  (optional)
    include_subtenants = False # bool |  (optional) if omitted the server will use the default value of False
    severities = [
        "severities_example",
    ] # [str] |  (optional)
    compliance_states = [
        DeviceComplianceState("COMPLIANT"),
    ] # [DeviceComplianceState] |  (optional)
    vulnerability_states = [
        DeviceVulnerabilityState("VULNERABLE"),
    ] # [DeviceVulnerabilityState] |  (optional)
    sort_by = "name" # str |  (optional)
    sort_order = "asc" # str |  (optional) if omitted the server will use the default value of "asc"

    # example passing only required values which don't have defaults set
    try:
        # Returns a page of devices.
        api_response = api_instance.get_devices_page(page, page_size)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling DevicesApi->get_devices_page: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a page of devices.
        api_response = api_instance.get_devices_page(page, page_size, device_ids=device_ids, service_ids=service_ids, types=types, serial_keys=serial_keys, service_types=service_types, models=models, subtypes=subtypes, names=names, versions=versions, tenant_ids=tenant_ids, include_subtenants=include_subtenants, severities=severities, compliance_states=compliance_states, vulnerability_states=vulnerability_states, sort_by=sort_by, sort_order=sort_order)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling DevicesApi->get_devices_page: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  |
 **page_size** | **int**|  |
 **device_ids** | **[str]**|  | [optional]
 **service_ids** | **[str]**|  | [optional]
 **types** | **[str]**|  | [optional]
 **serial_keys** | **[str]**|  | [optional]
 **service_types** | **[str]**|  | [optional]
 **models** | **[str]**|  | [optional]
 **subtypes** | **[str]**|  | [optional]
 **names** | **[str]**|  | [optional]
 **versions** | **[str]**|  | [optional]
 **tenant_ids** | **[str]**|  | [optional]
 **include_subtenants** | **bool**|  | [optional] if omitted the server will use the default value of False
 **severities** | **[str]**|  | [optional]
 **compliance_states** | [**[DeviceComplianceState]**](DeviceComplianceState.md)|  | [optional]
 **vulnerability_states** | [**[DeviceVulnerabilityState]**](DeviceVulnerabilityState.md)|  | [optional]
 **sort_by** | **str**|  | [optional]
 **sort_order** | **str**|  | [optional] if omitted the server will use the default value of "asc"

### Return type

[**DevicesPage**](DevicesPage.md)

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

# **patch_device**
> Device patch_device(id, device_patch)

Update a device.

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import devices_api
from python_msx_sdk.model.device_patch import DevicePatch
from python_msx_sdk.model.device import Device
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
    api_instance = devices_api.DevicesApi(api_client)
    id = "id_example" # str | 
    device_patch = DevicePatch(
        name="name_example",
        model="model_example",
        type="type_example",
        sub_type="sub_type_example",
        serial_key="serial_key_example",
        version="version_example",
        compliance_state=DeviceComplianceState("COMPLIANT"),
    ) # DevicePatch | 

    # example passing only required values which don't have defaults set
    try:
        # Update a device.
        api_response = api_instance.patch_device(id, device_patch)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling DevicesApi->patch_device: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **device_patch** | [**DevicePatch**](DevicePatch.md)|  |

### Return type

[**Device**](Device.md)

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

# **redeploy_device**
> redeploy_device(id)

Dedeploys a device.

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import devices_api
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
    api_instance = devices_api.DevicesApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Dedeploys a device.
        api_instance.redeploy_device(id)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling DevicesApi->redeploy_device: %s\n" % e)
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
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthenticated |  -  |
**403** | Unauthorized |  -  |
**409** | Conflict |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device**
> Device update_device(id, device_update)

Update a device.

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import devices_api
from python_msx_sdk.model.device_update import DeviceUpdate
from python_msx_sdk.model.device import Device
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
    api_instance = devices_api.DevicesApi(api_client)
    id = "id_example" # str | 
    device_update = DeviceUpdate() # DeviceUpdate | 

    # example passing only required values which don't have defaults set
    try:
        # Update a device.
        api_response = api_instance.update_device(id, device_update)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling DevicesApi->update_device: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **device_update** | [**DeviceUpdate**](DeviceUpdate.md)|  |

### Return type

[**Device**](Device.md)

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

# **update_device_templates**
> [DeviceTemplateHistory] update_device_templates(id, device_template_update_request)

Update device templates that are already attached to a device.

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import devices_api
from python_msx_sdk.model.manage_change_request_pending import ManageChangeRequestPending
from python_msx_sdk.model.device_template_update_request import DeviceTemplateUpdateRequest
from python_msx_sdk.model.device_template_history import DeviceTemplateHistory
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
    api_instance = devices_api.DevicesApi(api_client)
    id = "id_example" # str | 
    device_template_update_request = DeviceTemplateUpdateRequest(
        template_details=[
            DeviceTemplateUpdateDetails(
                template_history_id="template_history_id_example",
                template_params=[
                    NameValue(
                        name="name_example",
                        value="value_example",
                    ),
                ],
            ),
        ],
    ) # DeviceTemplateUpdateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Update device templates that are already attached to a device.
        api_response = api_instance.update_device_templates(id, device_template_update_request)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling DevicesApi->update_device_templates: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **device_template_update_request** | [**DeviceTemplateUpdateRequest**](DeviceTemplateUpdateRequest.md)|  |

### Return type

[**[DeviceTemplateHistory]**](DeviceTemplateHistory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthenticated |  -  |
**403** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

