from castervoice.lib.imports import *

class MinttyRule(MergeRule):
    pronunciation = "git bash"

    mapping = {
        "see drive":
            R(Text(r"cd /c") + Key("enter"), rdescript="git bash: Go To C:"),
        "CD up":
            R(Text("cd ..") + Key("enter"), rdescript="git bash: Up Directory"),
        "CD":
            R(Text("cd "), rdescript="git bash: Navigate Directory"),
        "list":
            R(Text("ls -l") + Key("enter"), rdescript="git bash: List Files"),
        "make directory":
            R(Text("mkdir "), rdescript="git bash: Make directory"),
        "open dragonfly":
            R(Text(r"cd /c/dragonfly") + Key("enter"),
              rdescript="git bash: Go To dragonfly repository"),
        "install dragonfly":
            R(Text(r"python setup.py install") + Key("enter"),
              rdescript="git bash: install dragonfly"),
        "open Jpractice":
            R(Text(r"cd /e/GitHub/javaPractice") + Key("enter"),
              rdescript="git bash: Go To javaPractice"),
        "open my website":
            R(Text(r"cd /e/GitHub/codingApprentice.github.io") + Key("enter"),
              rdescript="git bash: Go To javaPractice"),
        "open macro system":
            R(Text(r"cd /c/NatLink/NatLink/MacroSystem") + Key("enter"),
              rdescript="git bash: Go To MacroSystem"),
        "open Sikuli folder":
            R(Text(r"cd /c/Users/barry/AppData/Roaming/Sikulix/Lib") + Key("enter"),
              rdescript="git bash: Go To MacroSystem"),

        #github commands
        "push origin master":
            R(Text("git push origin master") + Key("enter"),
              rdescript="git bash: push to the origin of the master"),
        "push origin":
            R(Text("git push origin "), rdescript="git bash: push to the origin"),
        "check out":
            R(Text("git checkout "), rdescript="git bash: check out"),
        "check out master":
            R(Text("git checkout master"), rdescript="git bash: check out master"),
        "my username":
            R(Text("codingApprentice") + Key("enter"), rdescript="git bash: username"),
        "check status":
            R(Text("git status") + Key("enter"), rdescript="git bash: check git status"),
        "add all files":
            R(Text(r"git add -A") + Key("enter"),
              rdescript="git bash: add all files to commit"),
        "submit a commit":
            R(Text(r"git commit -m ''") + Key("left"),
              rdescript="git bash: submit a commit with a message"),
        "check out new branch":
            R(Text(r"git checkout -b "), rdescript="git bash: checkout a new branch"),
        "exit":
            R(Text("exit") + Key("enter"), rdescript="git bash: Exit"),
    }
    extras = []
    defaults = {}


context = AppContext(executable="mintty")
control.non_ccr_app_rule(MinttyRule(), context=context)
