"""
    MSX SDK

    MSX SDK client.  # noqa: E501

    The version of the OpenAPI document: 1.0.8
    Generated by: https://openapi-generator.tech
"""


import unittest

import python_msx_sdk
from python_msx_sdk.api.billing_cycles_api import BillingCyclesApi  # noqa: E501


class TestBillingCyclesApi(unittest.TestCase):
    """BillingCyclesApi unit test stubs"""

    def setUp(self):
        self.api = BillingCyclesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_billing_cycle(self):
        """Test case for add_billing_cycle

        Add a billing cycle.  # noqa: E501
        """
        pass

    def test_delete_billing_cycle(self):
        """Test case for delete_billing_cycle

        Delete a billing cycle.  # noqa: E501
        """
        pass

    def test_get_billing_cycle(self):
        """Test case for get_billing_cycle

        Get a billing cycle.  # noqa: E501
        """
        pass

    def test_get_billing_cycles_page(self):
        """Test case for get_billing_cycles_page

        Retrieve a page of billing cycles.  # noqa: E501
        """
        pass

    def test_process_billing_cycle(self):
        """Test case for process_billing_cycle

        Process a billing cycle.  # noqa: E501
        """
        pass

    def test_update_billing_cycle(self):
        """Test case for update_billing_cycle

        Update billing cycle for an event type and tenant.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
