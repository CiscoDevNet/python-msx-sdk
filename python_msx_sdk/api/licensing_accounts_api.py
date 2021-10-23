"""
    MSX SDK

    MSX SDK client.  # noqa: E501

    The version of the OpenAPI document: 1.0.7
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
from python_msx_sdk.model.smart_account_type import SmartAccountType
from python_msx_sdk.model.smart_user_accounts import SmartUserAccounts


class LicensingAccountsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __get_user_accounts_list(
            self,
            user_id,
            **kwargs
        ):
            """Returns a filtered page of smart accounts.  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_user_accounts_list(user_id, async_req=True)
            >>> result = thread.get()

            Args:
                user_id (str): User Id

            Keyword Args:
                domain (str): Smart Account domain. [optional]
                role_name (str): Role Name. [optional]
                type (SmartAccountType): [optional]
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
                SmartUserAccounts
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
            kwargs['user_id'] = \
                user_id
            return self.call_with_http_info(**kwargs)

        self.get_user_accounts_list = _Endpoint(
            settings={
                'response_type': (SmartUserAccounts,),
                'auth': [],
                'endpoint_path': '/licensing/api/v8/accounts/smart/list',
                'operation_id': 'get_user_accounts_list',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'user_id',
                    'domain',
                    'role_name',
                    'type',
                ],
                'required': [
                    'user_id',
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
                    'user_id':
                        (str,),
                    'domain':
                        (str,),
                    'role_name':
                        (str,),
                    'type':
                        (SmartAccountType,),
                },
                'attribute_map': {
                    'user_id': 'userId',
                    'domain': 'domain',
                    'role_name': 'roleName',
                    'type': 'type',
                },
                'location_map': {
                    'user_id': 'query',
                    'domain': 'query',
                    'role_name': 'query',
                    'type': 'query',
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
            callable=__get_user_accounts_list
        )
