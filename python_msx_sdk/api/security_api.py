"""
    MSX SDK

    MSX SDK client.  # noqa: E501

    The version of the OpenAPI document: 1.0.10
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
from python_msx_sdk.model.access_token import AccessToken


class SecurityApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.get_access_token_endpoint = _Endpoint(
            settings={
                'response_type': (AccessToken,),
                'auth': [],
                'endpoint_path': '/idm/v2/token',
                'operation_id': 'get_access_token',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'authorization',
                    'grant_type',
                    'username',
                    'password',
                    'access_token',
                    'switch_username',
                    'tenant_id',
                    'scope',
                    'nonce',
                    'tenant_name',
                ],
                'required': [
                    'authorization',
                    'grant_type',
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
                    'authorization':
                        (str,),
                    'grant_type':
                        (str,),
                    'username':
                        (str,),
                    'password':
                        (str,),
                    'access_token':
                        (str,),
                    'switch_username':
                        (str,),
                    'tenant_id':
                        (str,),
                    'scope':
                        (str,),
                    'nonce':
                        (str,),
                    'tenant_name':
                        (str,),
                },
                'attribute_map': {
                    'authorization': 'Authorization',
                    'grant_type': 'grant_type',
                    'username': 'username',
                    'password': 'password',
                    'access_token': 'access_token',
                    'switch_username': 'switch_username',
                    'tenant_id': 'tenant_id',
                    'scope': 'scope',
                    'nonce': 'nonce',
                    'tenant_name': 'tenant_name',
                },
                'location_map': {
                    'authorization': 'header',
                    'grant_type': 'form',
                    'username': 'form',
                    'password': 'form',
                    'access_token': 'form',
                    'switch_username': 'form',
                    'tenant_id': 'form',
                    'scope': 'form',
                    'nonce': 'form',
                    'tenant_name': 'form',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/x-www-form-urlencoded'
                ]
            },
            api_client=api_client
        )

    def get_access_token(
        self,
        authorization,
        grant_type,
        **kwargs
    ):
        """Returns an access token.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_access_token(authorization, grant_type, async_req=True)
        >>> result = thread.get()

        Args:
            authorization (str):
            grant_type (str):

        Keyword Args:
            username (str): [optional]
            password (str): [optional]
            access_token (str): [optional]
            switch_username (str): [optional]
            tenant_id (str): [optional]
            scope (str): [optional]
            nonce (str): [optional]
            tenant_name (str): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            AccessToken
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
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['authorization'] = \
            authorization
        kwargs['grant_type'] = \
            grant_type
        return self.get_access_token_endpoint.call_with_http_info(**kwargs)

