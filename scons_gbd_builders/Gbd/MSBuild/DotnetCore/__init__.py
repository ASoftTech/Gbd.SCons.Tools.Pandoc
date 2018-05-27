"""
If the user requests "Gbd.MSBuild.DotnetCore" then this will call this script as a tool
In which case we include all the builders
"""
from __future__ import (division, print_function,
                        absolute_import, unicode_literals)

from . import DotnetCoreBuild


def generate(env):
    DotnetCoreBuild.generate(env)


def exists(env):
    if not DotnetCoreBuild.exists(env):
        return False
    return True
