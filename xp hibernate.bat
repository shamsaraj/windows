@echo off
:loop3
set /p hour= Enter hour (00-23):
	if %hour% gtr 23 goto loop3
	if %hour% LSS 0 goto loop3
:loop4
set /p min= Enter min (00-59):
	if %min% gtr 59 goto loop4
	if %min% LSS 0 goto loop4
echo The time to go is %hour%:%min%
:loop1
set tm=%time%
set hh=%tm:~0,2%
	if %hh% EQU %hour% goto minute
goto loop1
:minute
:loop2
set tm=%time%
set mm=%tm:~3,2%
	if %mm% EQU %min% goto end
goto loop2
:end 
echo "It is time to go home" 
%windir%\System32\rundll32.exe powrprof.dll,SetSuspendState 