"""
If the user requests "Gbd.MSBuild" then this will call this script as a tool
In which case we include all the builders
"""
from __future__ import (division, print_function,
                        absolute_import, unicode_literals)

from . import DotnetCore
from . import VC


def generate(env):
    DotnetCore.generate(env)
    VC.generate(env)


def exists(env):
    if not DotnetCore.exists(env):
        return False
    if not VC.exists(env):
        return False
    return True
