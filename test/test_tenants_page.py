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
from python_msx_sdk.model.tenant import Tenant
from python_msx_sdk.model.tenants_page_all_of import TenantsPageAllOf
globals()['PageHeader'] = PageHeader
globals()['Tenant'] = Tenant
globals()['TenantsPageAllOf'] = TenantsPageAllOf
from python_msx_sdk.model.tenants_page import TenantsPage


class TestTenantsPage(unittest.TestCase):
    """TenantsPage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTenantsPage(self):
        """Test TenantsPage"""
        # FIXME: construct object with mandatory attributes with example values
        # model = TenantsPage()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
