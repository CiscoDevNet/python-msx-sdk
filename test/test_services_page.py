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
from python_msx_sdk.model.service import Service
from python_msx_sdk.model.services_page_all_of import ServicesPageAllOf
globals()['PageHeader'] = PageHeader
globals()['Service'] = Service
globals()['ServicesPageAllOf'] = ServicesPageAllOf
from python_msx_sdk.model.services_page import ServicesPage


class TestServicesPage(unittest.TestCase):
    """ServicesPage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testServicesPage(self):
        """Test ServicesPage"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ServicesPage()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
