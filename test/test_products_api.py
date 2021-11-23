"""
    MSX SDK

    MSX SDK client.  # noqa: E501

    The version of the OpenAPI document: 1.0.8
    Generated by: https://openapi-generator.tech
"""


import unittest

import python_msx_sdk
from python_msx_sdk.api.products_api import ProductsApi  # noqa: E501


class TestProductsApi(unittest.TestCase):
    """ProductsApi unit test stubs"""

    def setUp(self):
        self.api = ProductsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_product(self):
        """Test case for create_product

        Creates a product.  # noqa: E501
        """
        pass

    def test_delete_product(self):
        """Test case for delete_product

        Deletes a product.  # noqa: E501
        """
        pass

    def test_get_product(self):
        """Test case for get_product

        Returns a product.  # noqa: E501
        """
        pass

    def test_get_product_assignments_list(self):
        """Test case for get_product_assignments_list

        Returns a list of tenant assignments for a product .  # noqa: E501
        """
        pass

    def test_get_products_count(self):
        """Test case for get_products_count

        Returns the number of products.  # noqa: E501
        """
        pass

    def test_get_products_page(self):
        """Test case for get_products_page

        Returns a page of products.  # noqa: E501
        """
        pass

    def test_update_product(self):
        """Test case for update_product

        Updates a product.  # noqa: E501
        """
        pass

    def test_update_product_assignments(self):
        """Test case for update_product_assignments

        Updates the tenant assignments for a product.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
