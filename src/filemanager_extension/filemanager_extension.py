##############################################################################
# COPYRIGHT Ericsson AB 2018
#
# The copyright to the computer program(s) herein is the property of
# Ericsson AB. The programs may be used and/or copied only with written
# permission from Ericsson AB. or in accordance with the terms and
# conditions stipulated in the agreement/contract under which the
# program(s) have been supplied.
##############################################################################

from litp.core.model_type import ItemType, Property, Collection
from litp.core.extension import ModelExtension


class FileManagerExtension(ModelExtension):
    """
    LITP filemanager extension
    """

    def define_item_types(self):
        item_types = []
        item_types.append(
            ItemType(
                'managed-file-list',
                extend_item='managed-file-base',
                item_description='A list of files to be managed',
                managed_file_list=Collection('managed-file'),

            ))
        item_types.append(
            ItemType(
                'managed-file',
                extend_item='managed-file-base',
                item_description='A file to be managed',
                path=Property('path_string',
                              prop_description='Absolute path of the file to '
                                               'be managed',
                              required=True),
                mode=Property('file_mode',
                              prop_description='File permission to be set on '
                                               'the file to be managed',
                              required=True
                              ),
            )
        )
        return item_types
