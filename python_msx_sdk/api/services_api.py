"""
    KAKAPO - MSX SDK

    MSX Platform SDK  # noqa: E501

    The version of the OpenAPI document: 1.0.2
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
from python_msx_sdk.model.legacy_service_order import LegacyServiceOrder
from python_msx_sdk.model.legacy_service_order_response import LegacyServiceOrderResponse
from python_msx_sdk.model.service import Service
from python_msx_sdk.model.services_page import ServicesPage


class ServicesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __delete_service(
            self,
            id,
            **kwargs
        ):
            """Deletes a service.  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.delete_service(id, async_req=True)
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

        self.delete_service = _Endpoint(
            settings={
                'response_type': None,
                'auth': [],
                'endpoint_path': '/manage/api/v8/services/{id}',
                'operation_id': 'delete_service',
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
            callable=__delete_service
        )

        def __get_service(
            self,
            id,
            **kwargs
        ):
            """Returns a service.  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_service(id, async_req=True)
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
                Service
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

        self.get_service = _Endpoint(
            settings={
                'response_type': (Service,),
                'auth': [],
                'endpoint_path': '/manage/api/v8/services/{id}',
                'operation_id': 'get_service',
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
            callable=__get_service
        )

        def __get_services_page(
            self,
            page,
            page_size,
            **kwargs
        ):
            """Returns a page of services.  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_services_page(page, page_size, async_req=True)
            >>> result = thread.get()

            Args:
                page (int):
                page_size (int):

            Keyword Args:
                tenant_ids ([str]): [optional]
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
                ServicesPage
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

        self.get_services_page = _Endpoint(
            settings={
                'response_type': (ServicesPage,),
                'auth': [],
                'endpoint_path': '/manage/api/v8/services',
                'operation_id': 'get_services_page',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'page',
                    'page_size',
                    'tenant_ids',
                ],
                'required': [
                    'page',
                    'page_size',
                ],
                'nullable': [
                ],
                'enum': [
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
                },
                'openapi_types': {
                    'page':
                        (int,),
                    'page_size':
                        (int,),
                    'tenant_ids':
                        ([str],),
                },
                'attribute_map': {
                    'page': 'page',
                    'page_size': 'pageSize',
                    'tenant_ids': 'tenantIds',
                },
                'location_map': {
                    'page': 'query',
                    'page_size': 'query',
                    'tenant_ids': 'query',
                },
                'collection_format_map': {
                    'tenant_ids': 'multi',
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_services_page
        )

        def __submit_order(
            self,
            product_id,
            offer_id,
            legacy_service_order,
            **kwargs
        ):
            """Submits an order.  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.submit_order(product_id, offer_id, legacy_service_order, async_req=True)
            >>> result = thread.get()

            Args:
                product_id (str):
                offer_id (str):
                legacy_service_order (LegacyServiceOrder):

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
                LegacyServiceOrderResponse
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
            kwargs['product_id'] = \
                product_id
            kwargs['offer_id'] = \
                offer_id
            kwargs['legacy_service_order'] = \
                legacy_service_order
            return self.call_with_http_info(**kwargs)

        self.submit_order = _Endpoint(
            settings={
                'response_type': (LegacyServiceOrderResponse,),
                'auth': [],
                'endpoint_path': '/manage/api/v8/services',
                'operation_id': 'submit_order',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'product_id',
                    'offer_id',
                    'legacy_service_order',
                ],
                'required': [
                    'product_id',
                    'offer_id',
                    'legacy_service_order',
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
                    'product_id':
                        (str,),
                    'offer_id':
                        (str,),
                    'legacy_service_order':
                        (LegacyServiceOrder,),
                },
                'attribute_map': {
                    'product_id': 'productId',
                    'offer_id': 'offerId',
                },
                'location_map': {
                    'product_id': 'query',
                    'offer_id': 'query',
                    'legacy_service_order': 'body',
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
            callable=__submit_order
        )

        def __update_order(
            self,
            product_id,
            offer_id,
            legacy_service_order,
            **kwargs
        ):
            """Updates an order.  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.update_order(product_id, offer_id, legacy_service_order, async_req=True)
            >>> result = thread.get()

            Args:
                product_id (str):
                offer_id (str):
                legacy_service_order (LegacyServiceOrder):

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
                LegacyServiceOrderResponse
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
            kwargs['product_id'] = \
                product_id
            kwargs['offer_id'] = \
                offer_id
            kwargs['legacy_service_order'] = \
                legacy_service_order
            return self.call_with_http_info(**kwargs)

        self.update_order = _Endpoint(
            settings={
                'response_type': (LegacyServiceOrderResponse,),
                'auth': [],
                'endpoint_path': '/manage/api/v8/services',
                'operation_id': 'update_order',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'product_id',
                    'offer_id',
                    'legacy_service_order',
                ],
                'required': [
                    'product_id',
                    'offer_id',
                    'legacy_service_order',
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
                    'product_id':
                        (str,),
                    'offer_id':
                        (str,),
                    'legacy_service_order':
                        (LegacyServiceOrder,),
                },
                'attribute_map': {
                    'product_id': 'productId',
                    'offer_id': 'offerId',
                },
                'location_map': {
                    'product_id': 'query',
                    'offer_id': 'query',
                    'legacy_service_order': 'body',
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
            callable=__update_order
        )
