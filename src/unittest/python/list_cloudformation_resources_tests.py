from mockito import mock, verify
import unittest

from list_cloudformation_resources import list_resources

class ListCloudFormationResourcesTest(unittest.TestCase):

  def test_list_resources_succeeds(self):
      list_resources()
