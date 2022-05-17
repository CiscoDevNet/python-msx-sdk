"""
    MSX SDK

    MSX SDK client.  # noqa: E501

    The version of the OpenAPI document: 1.0.10
    Generated by: https://openapi-generator.tech
"""


import unittest

import python_msx_sdk
from python_msx_sdk.api.workflow_categories_api import WorkflowCategoriesApi  # noqa: E501


class TestWorkflowCategoriesApi(unittest.TestCase):
    """WorkflowCategoriesApi unit test stubs"""

    def setUp(self):
        self.api = WorkflowCategoriesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_workflow_category(self):
        """Test case for create_workflow_category

        Creates a new workflow category.  # noqa: E501
        """
        pass

    def test_delete_workflow_category(self):
        """Test case for delete_workflow_category

        Deletes a workflow category.  # noqa: E501
        """
        pass

    def test_get_workflow_categories_list(self):
        """Test case for get_workflow_categories_list

        Returns a list of workflow categories.  # noqa: E501
        """
        pass

    def test_get_workflow_category(self):
        """Test case for get_workflow_category

        Returns a workflow category.  # noqa: E501
        """
        pass

    def test_update_workflow_category(self):
        """Test case for update_workflow_category

        Updates a workflow category.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
