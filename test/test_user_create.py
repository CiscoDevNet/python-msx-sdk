"""
    MSX SDK

    MSX SDK client.  # noqa: E501

    The version of the OpenAPI document: 1.0.7
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import python_msx_sdk
from python_msx_sdk.model.user_create_all_of import UserCreateAllOf
from python_msx_sdk.model.user_update import UserUpdate
globals()['UserCreateAllOf'] = UserCreateAllOf
globals()['UserUpdate'] = UserUpdate
from python_msx_sdk.model.user_create import UserCreate


class TestUserCreate(unittest.TestCase):
    """UserCreate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testUserCreate(self):
        """Test UserCreate"""
        # FIXME: construct object with mandatory attributes with example values
        # model = UserCreate()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
