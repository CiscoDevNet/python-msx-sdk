# python_msx_sdk.UsersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user**](UsersApi.md#create_user) | **POST** /idm/api/v8/users | Creates a new user.
[**delete_user**](UsersApi.md#delete_user) | **DELETE** /idm/api/v8/users/{id} | Deletes a user by id.
[**get_current_user**](UsersApi.md#get_current_user) | **GET** /idm/api/v8/users/current | Returns the current user.
[**get_user**](UsersApi.md#get_user) | **GET** /idm/api/v8/users/{id} | Returns an existing user.
[**get_users_page**](UsersApi.md#get_users_page) | **GET** /idm/api/v8/users | Returns a page of users.
[**update_user**](UsersApi.md#update_user) | **PUT** /idm/api/v8/users/{id} | Updates an existing user.
[**update_user_password**](UsersApi.md#update_user_password) | **PUT** /idm/api/v8/users/updatepassword | Update a user password.


# **create_user**
> User create_user(user_create)

Creates a new user.

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import users_api
from python_msx_sdk.model.user import User
from python_msx_sdk.model.user_create import UserCreate
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
    api_instance = users_api.UsersApi(api_client)
    user_create = UserCreate() # UserCreate | 

    # example passing only required values which don't have defaults set
    try:
        # Creates a new user.
        api_response = api_instance.create_user(user_create)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling UsersApi->create_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_create** | [**UserCreate**](UserCreate.md)|  |

### Return type

[**User**](User.md)

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

# **delete_user**
> delete_user(id)

Deletes a user by id.

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import users_api
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
    api_instance = users_api.UsersApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Deletes a user by id.
        api_instance.delete_user(id)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling UsersApi->delete_user: %s\n" % e)
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

# **get_current_user**
> User get_current_user()

Returns the current user.

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import users_api
from python_msx_sdk.model.user import User
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
    api_instance = users_api.UsersApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Returns the current user.
        api_response = api_instance.get_current_user()
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling UsersApi->get_current_user: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthenticated |  -  |
**403** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> User get_user(id)

Returns an existing user.

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import users_api
from python_msx_sdk.model.user import User
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
    api_instance = users_api.UsersApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Returns an existing user.
        api_response = api_instance.get_user(id)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling UsersApi->get_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**User**](User.md)

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

# **get_users_page**
> UsersPage get_users_page(page, page_size)

Returns a page of users.

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import users_api
from python_msx_sdk.model.users_page import UsersPage
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
    api_instance = users_api.UsersApi(api_client)
    page = 0 # int | 
    page_size = 10 # int | 
    tenant_id = "tenantId_example" # str |  (optional)
    deleted = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a page of users.
        api_response = api_instance.get_users_page(page, page_size)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling UsersApi->get_users_page: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a page of users.
        api_response = api_instance.get_users_page(page, page_size, tenant_id=tenant_id, deleted=deleted)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling UsersApi->get_users_page: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  |
 **page_size** | **int**|  |
 **tenant_id** | **str**|  | [optional]
 **deleted** | **bool**|  | [optional]

### Return type

[**UsersPage**](UsersPage.md)

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

# **update_user**
> User update_user(id, user_update)

Updates an existing user.

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import users_api
from python_msx_sdk.model.user import User
from python_msx_sdk.model.user_update import UserUpdate
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
    api_instance = users_api.UsersApi(api_client)
    id = "id_example" # str | 
    user_update = UserUpdate(
        first_name="first_name_example",
        last_name="last_name_example",
        email="email_example",
        role_ids=[
            "role_ids_example",
        ],
        tenant_ids=[],
        password_policy_name="password_policy_name_example",
        locale="locale_example",
    ) # UserUpdate | 

    # example passing only required values which don't have defaults set
    try:
        # Updates an existing user.
        api_response = api_instance.update_user(id, user_update)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling UsersApi->update_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **user_update** | [**UserUpdate**](UserUpdate.md)|  |

### Return type

[**User**](User.md)

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

# **update_user_password**
> update_user_password(update_password)

Update a user password.

### Example

```python
import time
import python_msx_sdk
from python_msx_sdk.api import users_api
from python_msx_sdk.model.update_password import UpdatePassword
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
    api_instance = users_api.UsersApi(api_client)
    update_password = UpdatePassword(
        username="username_example",
        old_password="old_password_example",
        new_password="new_password_example",
    ) # UpdatePassword | 

    # example passing only required values which don't have defaults set
    try:
        # Update a user password.
        api_instance.update_user_password(update_password)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling UsersApi->update_user_password: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_password** | [**UpdatePassword**](UpdatePassword.md)|  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**401** | Unauthenticated |  -  |
**403** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

