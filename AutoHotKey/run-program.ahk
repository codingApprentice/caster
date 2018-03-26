#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

; This is a simple and pretty generic example of an AutoHotkey script to run a
; program when you press a keyboard shortcut. Add as many of these as you want
; to a .ahk file, and set that to be run at startup.

; See the Hotkeys reference [1] for details of the modifiers and keys available.

; [1]: http://www.autohotkey.com/docs/Hotkeys.htm


; ctrl+Alt+shift+A - Open dragon NaturallySpeaking 13
^!+a::
    Run "C:\Program Files (x86)\Nuance\NaturallySpeaking13\Program\natspeak.exe" 
    Return
