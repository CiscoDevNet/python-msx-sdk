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
from python_msx_sdk.model.error import Error
from python_msx_sdk.model.vulnerabilities_page import VulnerabilitiesPage
from python_msx_sdk.model.vulnerability_feed import VulnerabilityFeed
from python_msx_sdk.model.vulnerability_ingest_page import VulnerabilityIngestPage
from python_msx_sdk.model.vulnerability_ingestion import VulnerabilityIngestion
from python_msx_sdk.model.vulnerability_severity import VulnerabilitySeverity


class VulnerabilitiesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.get_ingest_vulnerabilities_tasks_page_endpoint = _Endpoint(
            settings={
                'response_type': (VulnerabilityIngestPage,),
                'auth': [],
                'endpoint_path': '/vulnerability/api/v8/vulnerabilities/ingests',
                'operation_id': 'get_ingest_vulnerabilities_tasks_page',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'page',
                    'page_size',
                    'start_date',
                    'end_date',
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
                    'start_date':
                        (datetime,),
                    'end_date':
                        (datetime,),
                },
                'attribute_map': {
                    'page': 'page',
                    'page_size': 'pageSize',
                    'start_date': 'startDate',
                    'end_date': 'endDate',
                },
                'location_map': {
                    'page': 'query',
                    'page_size': 'query',
                    'start_date': 'query',
                    'end_date': 'query',
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
            api_client=api_client
        )
        self.get_vulnerabilities_page_endpoint = _Endpoint(
            settings={
                'response_type': (VulnerabilitiesPage,),
                'auth': [],
                'endpoint_path': '/vulnerability/api/v8/vulnerabilities',
                'operation_id': 'get_vulnerabilities_page',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'page',
                    'page_size',
                    'cve_id',
                    'vendor',
                    'product',
                    'version',
                    'severity',
                    'start_date',
                    'end_date',
                    'year',
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
                    'sort_by',
                    'sort_order',
                ],
                'validation': [
                    'page',
                    'page_size',
                    'year',
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
                    ('year',): {

                        'inclusive_maximum': 9999,
                        'inclusive_minimum': 1970,
                    },
                },
                'allowed_values': {
                    ('sort_by',): {

                        "PUBLISHEDON": "publishedOn",
                        "MODIFIEDON": "modifiedOn"
                    },
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
                    'cve_id':
                        (str,),
                    'vendor':
                        (str,),
                    'product':
                        (str,),
                    'version':
                        (str,),
                    'severity':
                        (VulnerabilitySeverity,),
                    'start_date':
                        (datetime,),
                    'end_date':
                        (datetime,),
                    'year':
                        (int,),
                    'sort_by':
                        (str,),
                    'sort_order':
                        (str,),
                },
                'attribute_map': {
                    'page': 'page',
                    'page_size': 'pageSize',
                    'cve_id': 'cveId',
                    'vendor': 'vendor',
                    'product': 'product',
                    'version': 'version',
                    'severity': 'severity',
                    'start_date': 'startDate',
                    'end_date': 'endDate',
                    'year': 'year',
                    'sort_by': 'sortBy',
                    'sort_order': 'sortOrder',
                },
                'location_map': {
                    'page': 'query',
                    'page_size': 'query',
                    'cve_id': 'query',
                    'vendor': 'query',
                    'product': 'query',
                    'version': 'query',
                    'severity': 'query',
                    'start_date': 'query',
                    'end_date': 'query',
                    'year': 'query',
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
            api_client=api_client
        )
        self.ingest_vulnerabilities_endpoint = _Endpoint(
            settings={
                'response_type': (VulnerabilityIngestion,),
                'auth': [],
                'endpoint_path': '/vulnerability/api/v8/vulnerabilities/ingests',
                'operation_id': 'ingest_vulnerabilities',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'vulnerability_feed',
                ],
                'required': [
                    'vulnerability_feed',
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
                    'vulnerability_feed':
                        (VulnerabilityFeed,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'vulnerability_feed': 'body',
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
            api_client=api_client
        )

    def get_ingest_vulnerabilities_tasks_page(
        self,
        page,
        page_size,
        **kwargs
    ):
        """Returns a filtered page of ingest tasks.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_ingest_vulnerabilities_tasks_page(page, page_size, async_req=True)
        >>> result = thread.get()

        Args:
            page (int):
            page_size (int):

        Keyword Args:
            start_date (datetime): Start date for date range filter on validation execution date.. [optional]
            end_date (datetime): End date for date range filter on validation execution date.. [optional]
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
            VulnerabilityIngestPage
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
        kwargs['page'] = \
            page
        kwargs['page_size'] = \
            page_size
        return self.get_ingest_vulnerabilities_tasks_page_endpoint.call_with_http_info(**kwargs)

    def get_vulnerabilities_page(
        self,
        page,
        page_size,
        **kwargs
    ):
        """Returns a filtered page of vulnerabilities.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_vulnerabilities_page(page, page_size, async_req=True)
        >>> result = thread.get()

        Args:
            page (int):
            page_size (int):

        Keyword Args:
            cve_id (str): CVE identifer (https://www.cvedetails.com/cve-help.php) to filter by.. [optional]
            vendor (str): Vendor identifier (as defined in NIST's CPE dictionary) to filter by.. [optional]
            product (str): Product identifier (as defined in NIST's CPE dictionary) to filter by.. [optional]
            version (str): Product version (as defined in NIST's CPE dictionary) filter to filter by.. [optional]
            severity (VulnerabilitySeverity): A CVSS severity level (https://nvd.nist.gov/vuln-metrics/cvss) to filter by.. [optional]
            start_date (datetime): Start date for date range filter on CVE published date.. [optional]
            end_date (datetime): End date for date range filter on CVE published date.. [optional]
            year (int): Year CVE published filter.. [optional]
            sort_by (str): [optional] if omitted the server will use the default value of "publishedOn"
            sort_order (str): [optional] if omitted the server will use the default value of "asc"
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
            VulnerabilitiesPage
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
        kwargs['page'] = \
            page
        kwargs['page_size'] = \
            page_size
        return self.get_vulnerabilities_page_endpoint.call_with_http_info(**kwargs)

    def ingest_vulnerabilities(
        self,
        vulnerability_feed,
        **kwargs
    ):
        """Ingests a CVE JSON feed into the Vulnerability Service datastore.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.ingest_vulnerabilities(vulnerability_feed, async_req=True)
        >>> result = thread.get()

        Args:
            vulnerability_feed (VulnerabilityFeed):

        Keyword Args:
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
            VulnerabilityIngestion
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
        kwargs['vulnerability_feed'] = \
            vulnerability_feed
        return self.ingest_vulnerabilities_endpoint.call_with_http_info(**kwargs)

