"""
    MSX SDK

    MSX SDK client.  # noqa: E501

    The version of the OpenAPI document: 1.0.7
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import python_msx_sdk
from python_msx_sdk.model.service_all_of import ServiceAllOf
from python_msx_sdk.model.service_update import ServiceUpdate
globals()['ServiceAllOf'] = ServiceAllOf
globals()['ServiceUpdate'] = ServiceUpdate
from python_msx_sdk.model.service import Service


class TestService(unittest.TestCase):
    """Service unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testService(self):
        """Test Service"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Service()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
