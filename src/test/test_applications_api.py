"""
    Apis

    IGT Cloud entities  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import igtcloud.client.services.entities
from igtcloud.client.services.entities.api.applications_api import ApplicationsApi  # noqa: E501


class TestApplicationsApi(unittest.TestCase):
    """ApplicationsApi unit test stubs"""

    def setUp(self):
        self.api = ApplicationsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_applications(self):
        """Test case for get_applications

        """
        pass

    def test_get_training_application_guide(self):
        """Test case for get_training_application_guide

        """
        pass

    def test_get_training_application_storage(self):
        """Test case for get_training_application_storage

        """
        pass

    def test_get_training_applications(self):
        """Test case for get_training_applications

        """
        pass


if __name__ == '__main__':
    unittest.main()
