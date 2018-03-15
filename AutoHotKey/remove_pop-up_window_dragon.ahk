#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.
#Persistent
SetTimer, CloseUnwantedWindow, 250
Return

CloseUnwantedWindow:
IfWinExist,, R6034
{
	WinClose,, R6034
}
Return
