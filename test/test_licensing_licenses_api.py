"""
    MSX SDK

    MSX SDK client.  # noqa: E501

    The version of the OpenAPI document: 1.0.7
    Generated by: https://openapi-generator.tech
"""


import unittest

import python_msx_sdk
from python_msx_sdk.api.licensing_licenses_api import LicensingLicensesApi  # noqa: E501


class TestLicensingLicensesApi(unittest.TestCase):
    """LicensingLicensesApi unit test stubs"""

    def setUp(self):
        self.api = LicensingLicensesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_licenses_list(self):
        """Test case for get_licenses_list

        Returns a filtered list of licenses.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()