"""
If the user requests "Gbd.MSBuild.VC" then this will call this script as a tool
In which case we include all the builders
"""
from __future__ import (division, print_function,
                        absolute_import, unicode_literals)

from . import Dll2Lib


def generate(env):
    Dll2Lib.generate(env)


def exists(env):
    if not Dll2Lib.exists(env):
        return False
    return True
