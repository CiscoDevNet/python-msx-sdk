"""
    MSX SDK

    MSX SDK client.  # noqa: E501

    The version of the OpenAPI document: 1.0.8
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import python_msx_sdk
from python_msx_sdk.model.incident import Incident
from python_msx_sdk.model.incidents_page_all_of import IncidentsPageAllOf
from python_msx_sdk.model.page_header import PageHeader
globals()['Incident'] = Incident
globals()['IncidentsPageAllOf'] = IncidentsPageAllOf
globals()['PageHeader'] = PageHeader
from python_msx_sdk.model.incidents_page import IncidentsPage


class TestIncidentsPage(unittest.TestCase):
    """IncidentsPage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testIncidentsPage(self):
        """Test IncidentsPage"""
        # FIXME: construct object with mandatory attributes with example values
        # model = IncidentsPage()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
