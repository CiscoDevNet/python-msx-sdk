"""
    MSX SDK

    MSX SDK client.  # noqa: E501

    The version of the OpenAPI document: 1.0.10
    Generated by: https://openapi-generator.tech
"""


import unittest

import python_msx_sdk
from python_msx_sdk.api.sites_api import SitesApi  # noqa: E501


class TestSitesApi(unittest.TestCase):
    """SitesApi unit test stubs"""

    def setUp(self):
        self.api = SitesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_devices_to_site(self):
        """Test case for add_devices_to_site

        Add devices to a site.  # noqa: E501
        """
        pass

    def test_add_services_to_site(self):
        """Test case for add_services_to_site

        Add services to a site.  # noqa: E501
        """
        pass

    def test_create_site(self):
        """Test case for create_site

        Creates a new site.  # noqa: E501
        """
        pass

    def test_delete_site(self):
        """Test case for delete_site

        Deletes a site.  # noqa: E501
        """
        pass

    def test_get_site(self):
        """Test case for get_site

        Returns a site.  # noqa: E501
        """
        pass

    def test_get_sites_page(self):
        """Test case for get_sites_page

        Returns a page of Sites. Only one filter is supported at a time.  # noqa: E501
        """
        pass

    def test_remove_devices_from_site(self):
        """Test case for remove_devices_from_site

        Removes devices from a site.  # noqa: E501
        """
        pass

    def test_remove_services_from_site(self):
        """Test case for remove_services_from_site

        Remove services from a site.  # noqa: E501
        """
        pass

    def test_update_site(self):
        """Test case for update_site

        Updates a site.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
