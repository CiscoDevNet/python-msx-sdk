"""
    MSX SDK

    MSX SDK client.  # noqa: E501

    The version of the OpenAPI document: 1.0.10
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import python_msx_sdk
from python_msx_sdk.model.product_all_of import ProductAllOf
from python_msx_sdk.model.template_create import TemplateCreate
from python_msx_sdk.model.template_status import TemplateStatus
from python_msx_sdk.model.template_status_meta import TemplateStatusMeta
globals()['ProductAllOf'] = ProductAllOf
globals()['TemplateCreate'] = TemplateCreate
globals()['TemplateStatus'] = TemplateStatus
globals()['TemplateStatusMeta'] = TemplateStatusMeta
from python_msx_sdk.model.template import Template


class TestTemplate(unittest.TestCase):
    """Template unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTemplate(self):
        """Test Template"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Template()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
