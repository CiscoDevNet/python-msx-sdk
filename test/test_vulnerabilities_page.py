"""
    MSX SDK

    MSX SDK client.  # noqa: E501

    The version of the OpenAPI document: 1.0.10
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import python_msx_sdk
from python_msx_sdk.model.page_header import PageHeader
from python_msx_sdk.model.vulnerabilities_page_all_of import VulnerabilitiesPageAllOf
from python_msx_sdk.model.vulnerability import Vulnerability
globals()['PageHeader'] = PageHeader
globals()['VulnerabilitiesPageAllOf'] = VulnerabilitiesPageAllOf
globals()['Vulnerability'] = Vulnerability
from python_msx_sdk.model.vulnerabilities_page import VulnerabilitiesPage


class TestVulnerabilitiesPage(unittest.TestCase):
    """VulnerabilitiesPage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testVulnerabilitiesPage(self):
        """Test VulnerabilitiesPage"""
        # FIXME: construct object with mandatory attributes with example values
        # model = VulnerabilitiesPage()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
