"""
    KAKAPO - MSX SDK

    MSX Platform SDK  # noqa: E501

    The version of the OpenAPI document: 1.0.2
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import python_msx_sdk
from python_msx_sdk.model.device import Device
from python_msx_sdk.model.devices_page_all_of import DevicesPageAllOf
from python_msx_sdk.model.page_header import PageHeader
globals()['Device'] = Device
globals()['DevicesPageAllOf'] = DevicesPageAllOf
globals()['PageHeader'] = PageHeader
from python_msx_sdk.model.devices_page import DevicesPage


class TestDevicesPage(unittest.TestCase):
    """DevicesPage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDevicesPage(self):
        """Test DevicesPage"""
        # FIXME: construct object with mandatory attributes with example values
        # model = DevicesPage()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()