"""
    MSX SDK

    MSX SDK client.  # noqa: E501

    The version of the OpenAPI document: 1.0.10
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import python_msx_sdk
from python_msx_sdk.model.generic_event_all_of import GenericEventAllOf
from python_msx_sdk.model.generic_event_create import GenericEventCreate
from python_msx_sdk.model.generic_event_security import GenericEventSecurity
from python_msx_sdk.model.generic_event_severity import GenericEventSeverity
from python_msx_sdk.model.generic_event_trace import GenericEventTrace
globals()['GenericEventAllOf'] = GenericEventAllOf
globals()['GenericEventCreate'] = GenericEventCreate
globals()['GenericEventSecurity'] = GenericEventSecurity
globals()['GenericEventSeverity'] = GenericEventSeverity
globals()['GenericEventTrace'] = GenericEventTrace
from python_msx_sdk.model.generic_event import GenericEvent


class TestGenericEvent(unittest.TestCase):
    """GenericEvent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGenericEvent(self):
        """Test GenericEvent"""
        # FIXME: construct object with mandatory attributes with example values
        # model = GenericEvent()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
