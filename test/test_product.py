"""
    MSX SDK

    MSX SDK client.  # noqa: E501

    The version of the OpenAPI document: 1.0.10
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import python_msx_sdk
from python_msx_sdk.model.nso_config_data_x_path import NSOConfigDataXPath
from python_msx_sdk.model.product_all_of import ProductAllOf
from python_msx_sdk.model.product_create import ProductCreate
from python_msx_sdk.model.service_element import ServiceElement
from python_msx_sdk.model.service_slmui_config import ServiceSLMUIConfig
from python_msx_sdk.model.service_ui_config import ServiceUIConfig
globals()['NSOConfigDataXPath'] = NSOConfigDataXPath
globals()['ProductAllOf'] = ProductAllOf
globals()['ProductCreate'] = ProductCreate
globals()['ServiceElement'] = ServiceElement
globals()['ServiceSLMUIConfig'] = ServiceSLMUIConfig
globals()['ServiceUIConfig'] = ServiceUIConfig
from python_msx_sdk.model.product import Product


class TestProduct(unittest.TestCase):
    """Product unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testProduct(self):
        """Test Product"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Product()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
