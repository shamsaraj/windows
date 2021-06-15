:loop2
set tm=%time%
set mm=%tm:~7,1%
	if %mm% EQU 1 goto end
goto loop2
:end 
wmic process where name="vina.exe" CALL setpriority 64 
goto loop2