"""
    MSX SDK

    MSX SDK client.  # noqa: E501

    The version of the OpenAPI document: 1.0.9
    Generated by: https://openapi-generator.tech
"""


import unittest

import python_msx_sdk
from python_msx_sdk.api.workflow_targets_api import WorkflowTargetsApi  # noqa: E501


class TestWorkflowTargetsApi(unittest.TestCase):
    """WorkflowTargetsApi unit test stubs"""

    def setUp(self):
        self.api = WorkflowTargetsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_workflow_target(self):
        """Test case for create_workflow_target

        Creates a new workflow target.  # noqa: E501
        """
        pass

    def test_delete_workflow_target(self):
        """Test case for delete_workflow_target

        Deletes a workflow target.  # noqa: E501
        """
        pass

    def test_get_workflow_target(self):
        """Test case for get_workflow_target

        Returns a workflow target.  # noqa: E501
        """
        pass

    def test_get_workflow_targets_list(self):
        """Test case for get_workflow_targets_list

        Returns a list of workflow targets.  # noqa: E501
        """
        pass

    def test_update_workflow_target(self):
        """Test case for update_workflow_target

        Updates a workflow target.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
