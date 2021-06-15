#python 3.2.2, 2.5
import time
import os
hour = 25
while hour > 23 or hour < 0: 
    hour = int(raw_input("Enter hour (00-23): "))
minute=60
while minute > 59 or minute < 0:
    minute = int (raw_input ("Enter min (00-59): "))
operatingsystem = "null"
while operatingsystem <> "win7" and operatingsystem <> "winxp":
    operatingsystem = raw_input("Enter your operating system type: (win7 or winxp):")
events = "null"
while events <> "shutdown" and events <> "hybernate" and events <> "restart":
    events = raw_input("Enter your desired event: (shutdown, hybernate or restart):")	
print "The time to go is " , hour , ":" , minute	
timeob = time.localtime()
hh = timeob.tm_hour
while hh <> hour :
    timeob = time.localtime()
    hh = timeob.tm_hour    
mm = timeob.tm_min
while mm <> minute :
    timeob = time.localtime()
    mm = timeob.tm_min
print "It is time to go home"
print "."
print "."
print "."
s=11
for i in range (1, 12):
	time.sleep(1)
	s=s-1
	print s
if operatingsystem == "win7" and events == "hybernate" :
	os.system ("%windir%\system32\shutdown /h")
if operatingsystem == "win7" and events == "shutdown" :
	os.system ("%windir%\system32\shutdown /s")
if operatingsystem == "win7" and events == "restart" :
	os.system ("%windir%\system32\shutdown /r")
if operatingsystem == "winxp" and events == "hybernate" :
	os.system ("%windir%\System32\rundll32.exe powrprof.dll,SetSuspendState ")
if operatingsystem == "winxp" and events == "shutdown" :
	os.system ("%windir%\System32\shutdown -s")
if operatingsystem == "winxp" and events == "restart" :
	os.system ("%windir%\System32\shutdown -r")