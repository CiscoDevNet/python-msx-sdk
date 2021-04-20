"""
    KAKAPO - MSX SDK

    MSX Platform SDK  # noqa: E501

    The version of the OpenAPI document: 1.0.2
    Generated by: https://openapi-generator.tech
"""


import unittest

import python_msx_sdk
from python_msx_sdk.api.users_api import UsersApi  # noqa: E501


class TestUsersApi(unittest.TestCase):
    """UsersApi unit test stubs"""

    def setUp(self):
        self.api = UsersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_user(self):
        """Test case for create_user

        Creates a new user.  # noqa: E501
        """
        pass

    def test_delete_user(self):
        """Test case for delete_user

        Deletes a user by id.  # noqa: E501
        """
        pass

    def test_get_current_user(self):
        """Test case for get_current_user

        Returns the current user.  # noqa: E501
        """
        pass

    def test_get_user(self):
        """Test case for get_user

        Returns an existing user.  # noqa: E501
        """
        pass

    def test_get_users_page(self):
        """Test case for get_users_page

        Returns a page of users.  # noqa: E501
        """
        pass

    def test_update_user(self):
        """Test case for update_user

        Updates an existing user.  # noqa: E501
        """
        pass

    def test_update_user_password(self):
        """Test case for update_user_password

        Update a user password.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
