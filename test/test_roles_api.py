"""
    MSX SDK

    MSX SDK client.  # noqa: E501

    The version of the OpenAPI document: 1.0.5
    Generated by: https://openapi-generator.tech
"""


import unittest

import python_msx_sdk
from python_msx_sdk.api.roles_api import RolesApi  # noqa: E501


class TestRolesApi(unittest.TestCase):
    """RolesApi unit test stubs"""

    def setUp(self):
        self.api = RolesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_role_by_name(self):
        """Test case for get_role_by_name

        Returns a role by name.  # noqa: E501
        """
        pass

    def test_get_roles_list(self):
        """Test case for get_roles_list

        Returns a list of roles.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
