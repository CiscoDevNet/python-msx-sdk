"""
    MSX SDK

    MSX SDK client.  # noqa: E501

    The version of the OpenAPI document: 1.0.7
    Generated by: https://openapi-generator.tech
"""


import unittest

import python_msx_sdk
from python_msx_sdk.api.security_api import SecurityApi  # noqa: E501


class TestSecurityApi(unittest.TestCase):
    """SecurityApi unit test stubs"""

    def setUp(self):
        self.api = SecurityApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_access_token(self):
        """Test case for get_access_token

        Returns an access token.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
