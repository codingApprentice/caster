from castervoice.lib.imports import *


class PotPlayerRule(MergeRule):
    pronunciation = "pot player"

    mapping = {
        # "pause video": R(Text(r"cd C:/")+Key("enter"), rdescript="CMD: Go To C:"),
        "(pause | play | resume) video":
            R(Key("space"), rdescript="PotPlayer: play or pause video"),
        #speed
        "normal speed":
            R(Text("z"), rdescript="PotPlayer: play at normal speed"),
        "faster":
            R(Text("c"), rdescript="PotPlayer: play at faster speed"),
        "slower":
            R(Text("x"), rdescript="PotPlayer: play at slower speed"),
        #volume
        "increase [the] volume":
            R(Key("up"), rdescript="PotPlayer: increase the volume"),
        "decrease [the] volume":
            R(Key("down"), rdescript="PotPlayer: decrease the volume"),
        "silence [the] video":
            R(Text("m"), rdescript="PotPlayer: mute the volume"),
        #screen size
        "[toggle] fullscreen":
            R(Key("a-enter"), rdescript="PotPlayer: toggle full screen"),
        "minimise window":
            R(Key("escape"), rdescript="PotPlayer: minimise window"),
        #jump to
        "beginning":
            R(Key("backspace"), rdescript="PotPlayer: go to the start of video"),
        "middle":
            R(Key("c-backspace"), rdescript="PotPlayer: go to the middle of video"),
        "finish":
            R(Key("s-backspace"), rdescript="PotPlayer: go to the end of video"),
        #move frame by frame
        "[go to] previous frame":
            R(Text("d"), rdescript="PotPlayer: go to previous frame"),
        "[go to] next frame":
            R(Text("f"), rdescript="PotPlayer: go to next frame"),

        #jump in time
        #5 seconds
        "[fast] forward five":
            R(Key("right"), rdescript="PotPlayer: go forward five seconds"),
        "(rewind | backwards) five":
            R(Key("left"), rdescript="PotPlayer: go backwards five seconds"),
        #30 seconds
        "[fast] forward thirty":
            R(Key("c-right"), rdescript="PotPlayer: go forward thirty seconds"),
        "(rewind | backwards) thirty":
            R(Key("c-left"), rdescript="PotPlayer: go backwards thirty seconds"),
        #1 minute
        "[fast] forward sixty":
            R(Key("s-right"), rdescript="PotPlayer: go forward sixty seconds"),
        "(rewind | backwards) sixty":
            R(Key("s-left"), rdescript="PotPlayer: go backwards sixty seconds"),
        #5 minutes
        "[fast] forward three hundred":
            R(Key("control:down,a-right,control:up"),
              rdescript="PotPlayer: go forward three hundred seconds"),
        "(rewind | backwards) three hundred":
            R(Key("control:down,a-left,control:up"),
              rdescript="PotPlayer: go backwards three hundred seconds"),
    }
    extras = []
    defaults = {}


context = AppContext(executable="PotPlayerMini64", title="PotPlayer")
control.non_ccr_app_rule(PotPlayerRule(), context=context)

