"""
    MSX SDK

    MSX SDK client.  # noqa: E501

    The version of the OpenAPI document: 1.0.10
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import python_msx_sdk
from python_msx_sdk.model.page_header import PageHeader
from python_msx_sdk.model.product import Product
from python_msx_sdk.model.products_page_all_of import ProductsPageAllOf
globals()['PageHeader'] = PageHeader
globals()['Product'] = Product
globals()['ProductsPageAllOf'] = ProductsPageAllOf
from python_msx_sdk.model.products_page import ProductsPage


class TestProductsPage(unittest.TestCase):
    """ProductsPage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testProductsPage(self):
        """Test ProductsPage"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ProductsPage()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
