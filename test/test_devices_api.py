"""
    MSX SDK

    MSX SDK client.  # noqa: E501

    The version of the OpenAPI document: 1.0.5
    Generated by: https://openapi-generator.tech
"""


import unittest

import python_msx_sdk
from python_msx_sdk.api.devices_api import DevicesApi  # noqa: E501


class TestDevicesApi(unittest.TestCase):
    """DevicesApi unit test stubs"""

    def setUp(self):
        self.api = DevicesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_attach_device_templates(self):
        """Test case for attach_device_templates

        Attaches one or more device templates to a device instance.  # noqa: E501
        """
        pass

    def test_create_device(self):
        """Test case for create_device

        Creates a device.  # noqa: E501
        """
        pass

    def test_delete_device(self):
        """Test case for delete_device

        Deletes a device.  # noqa: E501
        """
        pass

    def test_detach_device_template(self):
        """Test case for detach_device_template

        Detaches a template from a device.  # noqa: E501
        """
        pass

    def test_detach_device_templates(self):
        """Test case for detach_device_templates

        Detach device templates that are already attached to a device.  # noqa: E501
        """
        pass

    def test_get_device(self):
        """Test case for get_device

        Returns a device.  # noqa: E501
        """
        pass

    def test_get_device_config(self):
        """Test case for get_device_config

        Returns the running configuration for a device.  # noqa: E501
        """
        pass

    def test_get_device_template_history(self):
        """Test case for get_device_template_history

        Returns device template history.  # noqa: E501
        """
        pass

    def test_get_devices_page(self):
        """Test case for get_devices_page

        Returns a page of devices.  # noqa: E501
        """
        pass

    def test_patch_device(self):
        """Test case for patch_device

        Update a device.  # noqa: E501
        """
        pass

    def test_redeploy_device(self):
        """Test case for redeploy_device

        Dedeploys a device.  # noqa: E501
        """
        pass

    def test_update_device(self):
        """Test case for update_device

        Update a device.  # noqa: E501
        """
        pass

    def test_update_device_templates(self):
        """Test case for update_device_templates

        Update device templates that are already attached to a device.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
