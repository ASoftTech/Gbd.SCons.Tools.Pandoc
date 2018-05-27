"""
Used by scons on startup to look for plugins / tools
"""

from __future__ import (division, print_function,
                        absolute_import, unicode_literals)

from Scons.Plugins import BasePlugin


class scons_gbd_builders(SconsBasePlugin):

    def get_metadata(self):
        """return metadata associated with the plugin"""
        self.metadata = {
            'name' = 'scons_gbd_builders',
            'api' = '1.0.0',
            'description' = 'Builder tools for use with SCons, e.g. dotnet core',
            'author' = 'grbd'}
        return self.metadata

    def on_tool_load(self):
        """return a list of namespace / toolpath pairs"""
        tools =
        [
            {'namespace': 'Gbd.Finders',
             'toolpath': PyPackageDir('scons_gbd_docs.Gbd.Finders').abspath},
            {'namespace': 'Gbd.MSBuild',
             'toolpath': PyPackageDir('scons_gbd_docs.Gbd.MSBuild').abspath}
        ]
        self.toolspecs = tools
        return self.toolspecs
