#
# This file is a command-module for Dragonfly.
# (c) Copyright 2008 by Christo Butcher
# Licensed under the LGPL, see <http://www.gnu.org/licenses/>
#
"""
Command-module for git ssh
modified by codingapprentice 19/03/2018
"""
#---------------------------------------------------------------------------

from dragonfly import (Grammar, AppContext, MappingRule,
                       Key, Text)

from caster.lib import control
from caster.lib import settings
from caster.lib.dfplus.merge import gfilter
from caster.lib.dfplus.merge.mergerule import MergeRule
from caster.lib.dfplus.state.short import R


class WishRule(MergeRule):
    pronunciation = "wish"

    mapping = {
        "my ticket":   R(Text("")+Key("enter"), rdescript="Wish: my git token or ticket"),
        
        }
    extras = [
              
             ]
    defaults ={}


#---------------------------------------------------------------------------

context = AppContext(executable="wish")
grammar = Grammar("wish", context=context)

if settings.SETTINGS["apps"]["wish"]:
    if settings.SETTINGS["miscellaneous"]["rdp_mode"]:
        control.nexus().merger.add_global_rule(WishRule())
        print("added Wish")
    else:
        rule = WishRule(name="wish")
        gfilter.run_on(rule)
        grammar.add_rule(rule)
        grammar.load()