"""
    MSX SDK

    MSX SDK client.  # noqa: E501

    The version of the OpenAPI document: 1.0.7
    Generated by: https://openapi-generator.tech
"""


import unittest

import python_msx_sdk
from python_msx_sdk.api.registration_api import RegistrationApi  # noqa: E501


class TestRegistrationApi(unittest.TestCase):
    """RegistrationApi unit test stubs"""

    def setUp(self):
        self.api = RegistrationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_registered_product_version(self):
        """Test case for delete_registered_product_version

        Delete a registration.  # noqa: E501
        """
        pass

    def test_get_registered_product_version_page(self):
        """Test case for get_registered_product_version_page

        Returns a filtered page of registered products / versions.  # noqa: E501
        """
        pass

    def test_register_product_version(self):
        """Test case for register_product_version

        Register a product / verison combination for vulnerability inspection.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
