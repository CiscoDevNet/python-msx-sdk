"""
    MSX SDK

    MSX SDK client.  # noqa: E501

    The version of the OpenAPI document: 1.0.8
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from python_msx_sdk.api_client import ApiClient, Endpoint as _Endpoint
from python_msx_sdk.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from python_msx_sdk.model.error import Error
from python_msx_sdk.model.tenant import Tenant
from python_msx_sdk.model.tenant_create import TenantCreate
from python_msx_sdk.model.tenant_update import TenantUpdate
from python_msx_sdk.model.tenants_page import TenantsPage


class TenantsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __create_tenant(
            self,
            tenant_create,
            **kwargs
        ):
            """Creates a new tenant.  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.create_tenant(tenant_create, async_req=True)
            >>> result = thread.get()

            Args:
                tenant_create (TenantCreate):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                Tenant
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['tenant_create'] = \
                tenant_create
            return self.call_with_http_info(**kwargs)

        self.create_tenant = _Endpoint(
            settings={
                'response_type': (Tenant,),
                'auth': [],
                'endpoint_path': '/idm/api/v8/tenants',
                'operation_id': 'create_tenant',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'tenant_create',
                ],
                'required': [
                    'tenant_create',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'tenant_create':
                        (TenantCreate,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'tenant_create': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__create_tenant
        )

        def __delete_tenant(
            self,
            id,
            **kwargs
        ):
            """Deletes a tenant by id.  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.delete_tenant(id, async_req=True)
            >>> result = thread.get()

            Args:
                id (str):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                None
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['id'] = \
                id
            return self.call_with_http_info(**kwargs)

        self.delete_tenant = _Endpoint(
            settings={
                'response_type': None,
                'auth': [],
                'endpoint_path': '/idm/api/v8/tenants/{id}',
                'operation_id': 'delete_tenant',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                ],
                'required': [
                    'id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'id':
                        (str,),
                },
                'attribute_map': {
                    'id': 'id',
                },
                'location_map': {
                    'id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__delete_tenant
        )

        def __get_tenant(
            self,
            id,
            **kwargs
        ):
            """Returns a tenant by id.  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_tenant(id, async_req=True)
            >>> result = thread.get()

            Args:
                id (str):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                Tenant
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['id'] = \
                id
            return self.call_with_http_info(**kwargs)

        self.get_tenant = _Endpoint(
            settings={
                'response_type': (Tenant,),
                'auth': [],
                'endpoint_path': '/idm/api/v8/tenants/{id}',
                'operation_id': 'get_tenant',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                ],
                'required': [
                    'id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'id':
                        (str,),
                },
                'attribute_map': {
                    'id': 'id',
                },
                'location_map': {
                    'id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_tenant
        )

        def __get_tenants_list(
            self,
            ids,
            **kwargs
        ):
            """Returns a list of tenants.  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_tenants_list(ids, async_req=True)
            >>> result = thread.get()

            Args:
                ids ([str]):

            Keyword Args:
                show_image (bool): [optional] if omitted the server will use the default value of False
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                [Tenant]
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['ids'] = \
                ids
            return self.call_with_http_info(**kwargs)

        self.get_tenants_list = _Endpoint(
            settings={
                'response_type': ([Tenant],),
                'auth': [],
                'endpoint_path': '/idm/api/v8/tenants/list',
                'operation_id': 'get_tenants_list',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'ids',
                    'show_image',
                ],
                'required': [
                    'ids',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'ids':
                        ([str],),
                    'show_image':
                        (bool,),
                },
                'attribute_map': {
                    'ids': 'ids',
                    'show_image': 'showImage',
                },
                'location_map': {
                    'ids': 'query',
                    'show_image': 'query',
                },
                'collection_format_map': {
                    'ids': 'multi',
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_tenants_list
        )

        def __get_tenants_page(
            self,
            page,
            page_size,
            **kwargs
        ):
            """Returns a page of tenants.  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_tenants_page(page, page_size, async_req=True)
            >>> result = thread.get()

            Args:
                page (int):
                page_size (int):

            Keyword Args:
                parent_id (str): [optional]
                show_image (bool): [optional] if omitted the server will use the default value of False
                sort_by (str): [optional]
                sort_order (str): [optional] if omitted the server will use the default value of "asc"
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                TenantsPage
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['page'] = \
                page
            kwargs['page_size'] = \
                page_size
            return self.call_with_http_info(**kwargs)

        self.get_tenants_page = _Endpoint(
            settings={
                'response_type': (TenantsPage,),
                'auth': [],
                'endpoint_path': '/idm/api/v8/tenants',
                'operation_id': 'get_tenants_page',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'page',
                    'page_size',
                    'parent_id',
                    'show_image',
                    'sort_by',
                    'sort_order',
                ],
                'required': [
                    'page',
                    'page_size',
                ],
                'nullable': [
                ],
                'enum': [
                    'sort_order',
                ],
                'validation': [
                    'page',
                    'page_size',
                ]
            },
            root_map={
                'validations': {
                    ('page',): {

                        'inclusive_minimum': 0,
                    },
                    ('page_size',): {

                        'inclusive_maximum': 1000,
                        'inclusive_minimum': 1,
                    },
                },
                'allowed_values': {
                    ('sort_order',): {

                        "ASC": "asc",
                        "DESC": "desc"
                    },
                },
                'openapi_types': {
                    'page':
                        (int,),
                    'page_size':
                        (int,),
                    'parent_id':
                        (str,),
                    'show_image':
                        (bool,),
                    'sort_by':
                        (str,),
                    'sort_order':
                        (str,),
                },
                'attribute_map': {
                    'page': 'page',
                    'page_size': 'pageSize',
                    'parent_id': 'parentId',
                    'show_image': 'showImage',
                    'sort_by': 'sortBy',
                    'sort_order': 'sortOrder',
                },
                'location_map': {
                    'page': 'query',
                    'page_size': 'query',
                    'parent_id': 'query',
                    'show_image': 'query',
                    'sort_by': 'query',
                    'sort_order': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_tenants_page
        )

        def __update_tenant(
            self,
            id,
            tenant_update,
            **kwargs
        ):
            """Updates a tenant by id.  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.update_tenant(id, tenant_update, async_req=True)
            >>> result = thread.get()

            Args:
                id (str):
                tenant_update (TenantUpdate):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                Tenant
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['id'] = \
                id
            kwargs['tenant_update'] = \
                tenant_update
            return self.call_with_http_info(**kwargs)

        self.update_tenant = _Endpoint(
            settings={
                'response_type': (Tenant,),
                'auth': [],
                'endpoint_path': '/idm/api/v8/tenants/{id}',
                'operation_id': 'update_tenant',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                    'tenant_update',
                ],
                'required': [
                    'id',
                    'tenant_update',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'id':
                        (str,),
                    'tenant_update':
                        (TenantUpdate,),
                },
                'attribute_map': {
                    'id': 'id',
                },
                'location_map': {
                    'id': 'path',
                    'tenant_update': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__update_tenant
        )
