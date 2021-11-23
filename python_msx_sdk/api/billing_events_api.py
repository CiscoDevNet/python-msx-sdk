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
from python_msx_sdk.model.billing_costs_report import BillingCostsReport
from python_msx_sdk.model.billing_event import BillingEvent
from python_msx_sdk.model.billing_events_page import BillingEventsPage
from python_msx_sdk.model.error import Error


class BillingEventsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __get_cost_summary(
            self,
            tenant_id,
            **kwargs
        ):
            """Retrieve a summary for tenant cost.  # noqa: E501

            Needs VIEW_COSTS permission to view cost details.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_cost_summary(tenant_id, async_req=True)
            >>> result = thread.get()

            Args:
                tenant_id (str):

            Keyword Args:
                from_date (datetime): [optional]
                to_date (datetime): [optional]
                group_by (str): [optional]
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
                BillingCostsReport
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
            kwargs['tenant_id'] = \
                tenant_id
            return self.call_with_http_info(**kwargs)

        self.get_cost_summary = _Endpoint(
            settings={
                'response_type': (BillingCostsReport,),
                'auth': [],
                'endpoint_path': '/billing/api/v8/events/costs',
                'operation_id': 'get_cost_summary',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'tenant_id',
                    'from_date',
                    'to_date',
                    'group_by',
                ],
                'required': [
                    'tenant_id',
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
                    'tenant_id':
                        (str,),
                    'from_date':
                        (datetime,),
                    'to_date':
                        (datetime,),
                    'group_by':
                        (str,),
                },
                'attribute_map': {
                    'tenant_id': 'tenantId',
                    'from_date': 'fromDate',
                    'to_date': 'toDate',
                    'group_by': 'groupBy',
                },
                'location_map': {
                    'tenant_id': 'query',
                    'from_date': 'query',
                    'to_date': 'query',
                    'group_by': 'query',
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
            callable=__get_cost_summary
        )

        def __get_event(
            self,
            id,
            **kwargs
        ):
            """Get an Event.  # noqa: E501

            Needs VIEW_EVENTS permission to get a billing event.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_event(id, async_req=True)
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
                BillingEvent
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

        self.get_event = _Endpoint(
            settings={
                'response_type': (BillingEvent,),
                'auth': [],
                'endpoint_path': '/billing/api/v8/events/{id}',
                'operation_id': 'get_event',
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
            callable=__get_event
        )

        def __get_events_page(
            self,
            tenant_id,
            page,
            page_size,
            **kwargs
        ):
            """Retrieve a page of events for tenant.  # noqa: E501

            Needs VIEW_EVENTS permission to view the billing events.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_events_page(tenant_id, page, page_size, async_req=True)
            >>> result = thread.get()

            Args:
                tenant_id (str):
                page (int):
                page_size (int):

            Keyword Args:
                from_date (datetime): [optional]
                to_date (datetime): [optional]
                type (str): [optional]
                subtype (str): [optional]
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
                BillingEventsPage
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
            kwargs['tenant_id'] = \
                tenant_id
            kwargs['page'] = \
                page
            kwargs['page_size'] = \
                page_size
            return self.call_with_http_info(**kwargs)

        self.get_events_page = _Endpoint(
            settings={
                'response_type': (BillingEventsPage,),
                'auth': [],
                'endpoint_path': '/billing/api/v8/events',
                'operation_id': 'get_events_page',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'tenant_id',
                    'page',
                    'page_size',
                    'from_date',
                    'to_date',
                    'type',
                    'subtype',
                ],
                'required': [
                    'tenant_id',
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
                    'tenant_id':
                        (str,),
                    'page':
                        (int,),
                    'page_size':
                        (int,),
                    'from_date':
                        (datetime,),
                    'to_date':
                        (datetime,),
                    'type':
                        (str,),
                    'subtype':
                        (str,),
                },
                'attribute_map': {
                    'tenant_id': 'tenantId',
                    'page': 'page',
                    'page_size': 'pageSize',
                    'from_date': 'fromDate',
                    'to_date': 'toDate',
                    'type': 'type',
                    'subtype': 'subtype',
                },
                'location_map': {
                    'tenant_id': 'query',
                    'page': 'query',
                    'page_size': 'query',
                    'from_date': 'query',
                    'to_date': 'query',
                    'type': 'query',
                    'subtype': 'query',
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
            callable=__get_events_page
        )
