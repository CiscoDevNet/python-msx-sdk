# python_msx_sdk.VulnerabilitiesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_ingest_vulnerabilities_tasks_page**](VulnerabilitiesApi.md#get_ingest_vulnerabilities_tasks_page) | **GET** /vulnerability/api/v8/vulnerabilities/ingests | Returns a filtered page of ingest tasks.
[**get_vulnerabilities_page**](VulnerabilitiesApi.md#get_vulnerabilities_page) | **GET** /vulnerability/api/v8/vulnerabilities | Returns a filtered page of vulnerabilities.
[**ingest_vulnerabilities**](VulnerabilitiesApi.md#ingest_vulnerabilities) | **POST** /vulnerability/api/v8/vulnerabilities/ingests | Ingests a CVE JSON feed into the Vulnerability Service datastore.


# **get_ingest_vulnerabilities_tasks_page**
> VulnerabilityIngestPage get_ingest_vulnerabilities_tasks_page(page, page_size)

Returns a filtered page of ingest tasks.

### Example


```python
import time
import python_msx_sdk
from python_msx_sdk.api import vulnerabilities_api
from python_msx_sdk.model.vulnerability_ingest_page import VulnerabilityIngestPage
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
    api_instance = vulnerabilities_api.VulnerabilitiesApi(api_client)
    page = 0 # int | 
    page_size = 10 # int | 
    start_date = dateutil_parser('2020-01-15T18:15:00Z') # datetime | Start date for date range filter on validation execution date. (optional)
    end_date = dateutil_parser('2021-01-15T18:15:00Z') # datetime | End date for date range filter on validation execution date. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a filtered page of ingest tasks.
        api_response = api_instance.get_ingest_vulnerabilities_tasks_page(page, page_size)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling VulnerabilitiesApi->get_ingest_vulnerabilities_tasks_page: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a filtered page of ingest tasks.
        api_response = api_instance.get_ingest_vulnerabilities_tasks_page(page, page_size, start_date=start_date, end_date=end_date)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling VulnerabilitiesApi->get_ingest_vulnerabilities_tasks_page: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  |
 **page_size** | **int**|  |
 **start_date** | **datetime**| Start date for date range filter on validation execution date. | [optional]
 **end_date** | **datetime**| End date for date range filter on validation execution date. | [optional]

### Return type

[**VulnerabilityIngestPage**](VulnerabilityIngestPage.md)

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

# **get_vulnerabilities_page**
> VulnerabilitiesPage get_vulnerabilities_page(page, page_size)

Returns a filtered page of vulnerabilities.

### Example


```python
import time
import python_msx_sdk
from python_msx_sdk.api import vulnerabilities_api
from python_msx_sdk.model.vulnerabilities_page import VulnerabilitiesPage
from python_msx_sdk.model.vulnerability_severity import VulnerabilitySeverity
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
    api_instance = vulnerabilities_api.VulnerabilitiesApi(api_client)
    page = 0 # int | 
    page_size = 10 # int | 
    cve_id = "CVE-2021-0202" # str | CVE identifer (https://www.cvedetails.com/cve-help.php) to filter by. (optional)
    vendor = "cisco" # str | Vendor identifier (as defined in NIST's CPE dictionary) to filter by. (optional)
    product = "ios_xe" # str | Product identifier (as defined in NIST's CPE dictionary) to filter by. (optional)
    version = "12.3" # str | Product version (as defined in NIST's CPE dictionary) filter to filter by. (optional)
    severity = VulnerabilitySeverity("NONE") # VulnerabilitySeverity | A CVSS severity level (https://nvd.nist.gov/vuln-metrics/cvss) to filter by. (optional)
    start_date = dateutil_parser('2020-01-15T18:15:00Z') # datetime | Start date for date range filter on CVE published date. (optional)
    end_date = dateutil_parser('2021-01-15T18:15:00Z') # datetime | End date for date range filter on CVE published date. (optional)
    year = 2019 # int | Year CVE published filter. (optional)
    sort_by = "publishedOn" # str |  (optional) if omitted the server will use the default value of "publishedOn"
    sort_order = "asc" # str |  (optional) if omitted the server will use the default value of "asc"

    # example passing only required values which don't have defaults set
    try:
        # Returns a filtered page of vulnerabilities.
        api_response = api_instance.get_vulnerabilities_page(page, page_size)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling VulnerabilitiesApi->get_vulnerabilities_page: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a filtered page of vulnerabilities.
        api_response = api_instance.get_vulnerabilities_page(page, page_size, cve_id=cve_id, vendor=vendor, product=product, version=version, severity=severity, start_date=start_date, end_date=end_date, year=year, sort_by=sort_by, sort_order=sort_order)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling VulnerabilitiesApi->get_vulnerabilities_page: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  |
 **page_size** | **int**|  |
 **cve_id** | **str**| CVE identifer (https://www.cvedetails.com/cve-help.php) to filter by. | [optional]
 **vendor** | **str**| Vendor identifier (as defined in NIST&#39;s CPE dictionary) to filter by. | [optional]
 **product** | **str**| Product identifier (as defined in NIST&#39;s CPE dictionary) to filter by. | [optional]
 **version** | **str**| Product version (as defined in NIST&#39;s CPE dictionary) filter to filter by. | [optional]
 **severity** | **VulnerabilitySeverity**| A CVSS severity level (https://nvd.nist.gov/vuln-metrics/cvss) to filter by. | [optional]
 **start_date** | **datetime**| Start date for date range filter on CVE published date. | [optional]
 **end_date** | **datetime**| End date for date range filter on CVE published date. | [optional]
 **year** | **int**| Year CVE published filter. | [optional]
 **sort_by** | **str**|  | [optional] if omitted the server will use the default value of "publishedOn"
 **sort_order** | **str**|  | [optional] if omitted the server will use the default value of "asc"

### Return type

[**VulnerabilitiesPage**](VulnerabilitiesPage.md)

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

# **ingest_vulnerabilities**
> VulnerabilityIngestion ingest_vulnerabilities(vulnerability_feed)

Ingests a CVE JSON feed into the Vulnerability Service datastore.

### Example


```python
import time
import python_msx_sdk
from python_msx_sdk.api import vulnerabilities_api
from python_msx_sdk.model.vulnerability_ingestion import VulnerabilityIngestion
from python_msx_sdk.model.vulnerability_feed import VulnerabilityFeed
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
    api_instance = vulnerabilities_api.VulnerabilitiesApi(api_client)
    vulnerability_feed = VulnerabilityFeed(
        name="CVE-Modified",
        file="nvdcve-1.1-modified.json.gz",
    ) # VulnerabilityFeed | 

    # example passing only required values which don't have defaults set
    try:
        # Ingests a CVE JSON feed into the Vulnerability Service datastore.
        api_response = api_instance.ingest_vulnerabilities(vulnerability_feed)
        pprint(api_response)
    except python_msx_sdk.ApiException as e:
        print("Exception when calling VulnerabilitiesApi->ingest_vulnerabilities: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vulnerability_feed** | [**VulnerabilityFeed**](VulnerabilityFeed.md)|  |

### Return type

[**VulnerabilityIngestion**](VulnerabilityIngestion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthenticated |  -  |
**403** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

