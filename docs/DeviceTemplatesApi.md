# python_msx_sdk.DeviceTemplatesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_device_template**](DeviceTemplatesApi.md#create_device_template) | **POST** /manage/api/v8/devicetemplates | Creates a device template.
[**create_device_template_version**](DeviceTemplatesApi.md#create_device_template_version) | **POST** /manage/api/v8/devicetemplates/versions | Creates a new version of an existing device template.
[**delete_device_template**](DeviceTemplatesApi.md#delete_device_template) | **DELETE** /manage/api/v8/devicetemplates/{id} | Deletes a device template.
[**get_device_template**](DeviceTemplatesApi.md#get_device_template) | **GET** /manage/api/v8/devicetemplates/{id} | Returns a device template.
[**get_device_templates_list**](DeviceTemplatesApi.md#get_device_templates_list) | **GET** /manage/api/v8/devicetemplates/list | Returns a list of device templates.
[**scan_device_template_parameters**](DeviceTemplatesApi.md#scan_device_template_parameters) | **POST** /manage/api/v8/devicetemplates/parameters/scan | API to scan parameters from the device template XML.
[**update_device_template_access**](DeviceTemplatesApi.md#update_device_template_access) | **PUT** /manage/api/v8/devicetemplates/{id}/access | Updates device template access.


# **create_device_template**
> DeviceTemplate create_device_template(device_template_create)

Creates a device template.

### Example


```python
import time
import python_msx_sdk
from python_msx_sdk.api import device_templates_api
from python_msx_sdk.model.device_template import DeviceTemplate
from python_msx_sdk.model.device_template_create import DeviceTemplateCreate
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
    api_instance = device_templates_api.DeviceTemplatesApi(api_client)
    device_template_create = DeviceTemplateCreate(
        name="name_example",
        description="description_example",
        version="version_example",
        service_type="service_type_example",
        device_models=[
            "device_models_example",
        ],
        config_content="config_content_example",
        resource_provider="resource_provider_example",
        template_standard="template_standard_example",
        tenant_access=DeviceTemplateAccess(
            tenant_ids=[
                "tenant_ids_example",
            ],
            _global=True,
        ),
        template_parameter_validators=[
            TemplateParameterValidator(
                name='''"eiVMSMy;m8X5a	c4rv5kzuY+,8CQgdA*c+^"GKqTVnnV
Z:zOBO1nvr<tqiK8<Ot,BBSHOb7:gqC*Igoeid'0BW
UF<<SePV*%j=@dAN,9$^emIe7
8o/ZRCEW4J;07HdF% </7$Z^@RsdoP/0h#GXx977D=R*'+5TaOkC:pUiK+2QCNN.gBF''',
                hint_text='''"eiVMSMy;m8X5a	c4rv5kzuY+,8CQgdA*c+^"GKqTVnnV
Z:zOBO1nvr<tqiK8<Ot,BBSHOb7:gqC*Igoeid'0BW
UF<<SePV*%j=@dAN,9$^emIe7
8o/ZRCEW4J;07HdF% </7$Z^@RsdoP/0h#GXx977D=R*'+5TaOkC:pUiK+2QCNN.gBF''',
                label='''"eiVMSMy;m8X5a	c4rv5kzuY+,8CQgdA*c+^"GKqTVnnV
Z:zOBO1nvr<tqiK8<Ot,BBSHOb7:gqC*Igoeid'0BW
UF<<SePV*%j=@dAN,9$^emIe7
8o/ZRCEW4J;07HdF% </7$Z^@RsdoP/0h#GXx977D=R*'+5TaOkC:pUiK+2QCNN.gBF''',
                type="Password",
                display_type="Textarea",
                allowed_values=[
                    "allowed_values_example",
                ],
                tool_tip_text="tool_tip_text_example",
            ),
        ],
        tags=[
            "tags_example",
        ],
    ) # DeviceTemplateCreate | 

    # example passing only required values which don't have defaults set
    try:
        # Creates a device template.
        api_response = api_instance.create_device_template(device_template_create)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling DeviceTemplatesApi->create_device_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_template_create** | [**DeviceTemplateCreate**](DeviceTemplateCreate.md)|  |

### Return type

[**DeviceTemplate**](DeviceTemplate.md)

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

# **create_device_template_version**
> DeviceTemplate create_device_template_version(device_template_version_create)

Creates a new version of an existing device template.

### Example


```python
import time
import python_msx_sdk
from python_msx_sdk.api import device_templates_api
from python_msx_sdk.model.device_template import DeviceTemplate
from python_msx_sdk.model.device_template_version_create import DeviceTemplateVersionCreate
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
    api_instance = device_templates_api.DeviceTemplatesApi(api_client)
    device_template_version_create = DeviceTemplateVersionCreate(
        name="name_example",
        config_content="config_content_example",
        template_parameter_validators=[
            TemplateParameterValidator(
                name='''"eiVMSMy;m8X5a	c4rv5kzuY+,8CQgdA*c+^"GKqTVnnV
Z:zOBO1nvr<tqiK8<Ot,BBSHOb7:gqC*Igoeid'0BW
UF<<SePV*%j=@dAN,9$^emIe7
8o/ZRCEW4J;07HdF% </7$Z^@RsdoP/0h#GXx977D=R*'+5TaOkC:pUiK+2QCNN.gBF''',
                hint_text='''"eiVMSMy;m8X5a	c4rv5kzuY+,8CQgdA*c+^"GKqTVnnV
Z:zOBO1nvr<tqiK8<Ot,BBSHOb7:gqC*Igoeid'0BW
UF<<SePV*%j=@dAN,9$^emIe7
8o/ZRCEW4J;07HdF% </7$Z^@RsdoP/0h#GXx977D=R*'+5TaOkC:pUiK+2QCNN.gBF''',
                label='''"eiVMSMy;m8X5a	c4rv5kzuY+,8CQgdA*c+^"GKqTVnnV
Z:zOBO1nvr<tqiK8<Ot,BBSHOb7:gqC*Igoeid'0BW
UF<<SePV*%j=@dAN,9$^emIe7
8o/ZRCEW4J;07HdF% </7$Z^@RsdoP/0h#GXx977D=R*'+5TaOkC:pUiK+2QCNN.gBF''',
                type="Password",
                display_type="Textarea",
                allowed_values=[
                    "allowed_values_example",
                ],
                tool_tip_text="tool_tip_text_example",
            ),
        ],
    ) # DeviceTemplateVersionCreate | 

    # example passing only required values which don't have defaults set
    try:
        # Creates a new version of an existing device template.
        api_response = api_instance.create_device_template_version(device_template_version_create)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling DeviceTemplatesApi->create_device_template_version: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_template_version_create** | [**DeviceTemplateVersionCreate**](DeviceTemplateVersionCreate.md)|  |

### Return type

[**DeviceTemplate**](DeviceTemplate.md)

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

# **delete_device_template**
> delete_device_template(id)

Deletes a device template.

### Example


```python
import time
import python_msx_sdk
from python_msx_sdk.api import device_templates_api
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
    api_instance = device_templates_api.DeviceTemplatesApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Deletes a device template.
        api_instance.delete_device_template(id)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling DeviceTemplatesApi->delete_device_template: %s\n" % e)
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

# **get_device_template**
> DeviceTemplate get_device_template(id)

Returns a device template.

### Example


```python
import time
import python_msx_sdk
from python_msx_sdk.api import device_templates_api
from python_msx_sdk.model.device_template import DeviceTemplate
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
    api_instance = device_templates_api.DeviceTemplatesApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Returns a device template.
        api_response = api_instance.get_device_template(id)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling DeviceTemplatesApi->get_device_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**DeviceTemplate**](DeviceTemplate.md)

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

# **get_device_templates_list**
> [DeviceTemplate] get_device_templates_list()

Returns a list of device templates.

### Example


```python
import time
import python_msx_sdk
from python_msx_sdk.api import device_templates_api
from python_msx_sdk.model.device_template import DeviceTemplate
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
    api_instance = device_templates_api.DeviceTemplatesApi(api_client)
    all_versions = False # bool |  (optional) if omitted the server will use the default value of False
    service_type = "manageddevice" # str |  (optional)
    tenant_id = "2664f157-18d8-4ecd-8c78-66b7cb7e1e25" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of device templates.
        api_response = api_instance.get_device_templates_list(all_versions=all_versions, service_type=service_type, tenant_id=tenant_id)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling DeviceTemplatesApi->get_device_templates_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **all_versions** | **bool**|  | [optional] if omitted the server will use the default value of False
 **service_type** | **str**|  | [optional]
 **tenant_id** | **str**|  | [optional]

### Return type

[**[DeviceTemplate]**](DeviceTemplate.md)

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

# **scan_device_template_parameters**
> [str] scan_device_template_parameters()

API to scan parameters from the device template XML.

### Example


```python
import time
import python_msx_sdk
from python_msx_sdk.api import device_templates_api
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
    api_instance = device_templates_api.DeviceTemplatesApi(api_client)
    file = open('/path/to/file', 'rb') # file_type | The XML template file of a device template (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # API to scan parameters from the device template XML.
        api_response = api_instance.scan_device_template_parameters(file=file)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling DeviceTemplatesApi->scan_device_template_parameters: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file_type**| The XML template file of a device template | [optional]

### Return type

**[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**400** | Bad Request |  -  |
**401** | Unauthenticated |  -  |
**403** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device_template_access**
> DeviceTemplateAccessResponse update_device_template_access(id, device_template_access)

Updates device template access.

### Example


```python
import time
import python_msx_sdk
from python_msx_sdk.api import device_templates_api
from python_msx_sdk.model.device_template_access import DeviceTemplateAccess
from python_msx_sdk.model.device_template_access_response import DeviceTemplateAccessResponse
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
    api_instance = device_templates_api.DeviceTemplatesApi(api_client)
    id = "id_example" # str | 
    device_template_access = DeviceTemplateAccess(
        tenant_ids=[
            "tenant_ids_example",
        ],
        _global=True,
    ) # DeviceTemplateAccess | 

    # example passing only required values which don't have defaults set
    try:
        # Updates device template access.
        api_response = api_instance.update_device_template_access(id, device_template_access)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling DeviceTemplatesApi->update_device_template_access: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **device_template_access** | [**DeviceTemplateAccess**](DeviceTemplateAccess.md)|  |

### Return type

[**DeviceTemplateAccessResponse**](DeviceTemplateAccessResponse.md)

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

