"""
    MSX SDK

    MSX SDK client.  # noqa: E501

    The version of the OpenAPI document: 1.0.8
    Generated by: https://openapi-generator.tech
"""


import unittest

import python_msx_sdk
from python_msx_sdk.api.services_api import ServicesApi  # noqa: E501


class TestServicesApi(unittest.TestCase):
    """ServicesApi unit test stubs"""

    def setUp(self):
        self.api = ServicesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_service(self):
        """Test case for delete_service

        Deletes a service.  # noqa: E501
        """
        pass

    def test_get_service(self):
        """Test case for get_service

        Returns a service.  # noqa: E501
        """
        pass

    def test_get_services_page(self):
        """Test case for get_services_page

        Returns a page of services.  # noqa: E501
        """
        pass

    def test_submit_order(self):
        """Test case for submit_order

        Submits an order.  # noqa: E501
        """
        pass

    def test_update_order(self):
        """Test case for update_order

        Updates an order.  # noqa: E501
        """
        pass

    def test_update_service(self):
        """Test case for update_service

        Updates a service.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
