"""
    MSX SDK

    MSX SDK client.  # noqa: E501

    The version of the OpenAPI document: 1.0.5
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import python_msx_sdk
from python_msx_sdk.model.page_header import PageHeader
from python_msx_sdk.model.user import User
from python_msx_sdk.model.users_page_all_of import UsersPageAllOf
globals()['PageHeader'] = PageHeader
globals()['User'] = User
globals()['UsersPageAllOf'] = UsersPageAllOf
from python_msx_sdk.model.users_page import UsersPage


class TestUsersPage(unittest.TestCase):
    """UsersPage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testUsersPage(self):
        """Test UsersPage"""
        # FIXME: construct object with mandatory attributes with example values
        # model = UsersPage()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
