##############################################################################
# COPYRIGHT Ericsson AB 2018
#
# The copyright to the computer program(s) herein is the property of
# Ericsson AB. The programs may be used and/or copied only with written
# permission from Ericsson AB. or in accordance with the terms and
# conditions stipulated in the agreement/contract under which the
# program(s) have been supplied.
##############################################################################

from filemanager_extension.filemanager_extension import FileManagerExtension

from litp.extensions.core_extension import CoreExtension
from litp.core.model_manager import ModelManager
from litp.core.plugin_manager import PluginManager
from litp.core.plugin_context_api import PluginApiContext

import unittest


class TestFileManagerExtension(unittest.TestCase):

    def setUp(self):
        """
        Construct a model, sufficient for test cases
        that you wish to implement in this suite.
        """
        self.model = ModelManager()
        # Instantiate a plugin API context to pass to plugin
        self.context = PluginApiContext(self.model)
        self.ext_manager = PluginManager(self.model)
        # Use add_property_types to add property types defined in
        # model extenstions
        # For example, from CoreExtensions (recommended)
        self.ext_manager.add_property_types(
            CoreExtension().define_property_types())

        # Instantiate your plugin and register with PluginManager
        self.ext = FileManagerExtension()

    def test_item_types_registered(self):
        # Assert that only extension's item types
        # are defined.
        item_types_expected = ["managed-file-list", 'managed-file']
        item_types = [it.item_type_id for it in
                      self.ext.define_item_types()]
        self.assertEquals(item_types_expected, item_types)



if __name__ == '__main__':
    unittest.main()
