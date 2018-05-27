"""
If the user requests "Gbd.Finders" then this will call this script as a tool
In which case we include all the builders
"""
from __future__ import (division, print_function,
                        absolute_import, unicode_literals)

from . import FindATK


def generate(env):
    FindATK.generate(env)


def exists(env):
    if not FindATK.exists(env):
        return False
    return True
