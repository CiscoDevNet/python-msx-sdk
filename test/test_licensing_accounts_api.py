"""
    MSX SDK

    MSX SDK client.  # noqa: E501

    The version of the OpenAPI document: 1.0.7
    Generated by: https://openapi-generator.tech
"""


import unittest

import python_msx_sdk
from python_msx_sdk.api.licensing_accounts_api import LicensingAccountsApi  # noqa: E501


class TestLicensingAccountsApi(unittest.TestCase):
    """LicensingAccountsApi unit test stubs"""

    def setUp(self):
        self.api = LicensingAccountsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_user_accounts_list(self):
        """Test case for get_user_accounts_list

        Returns a filtered page of smart accounts.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
