@echo off

title info
color 06
mode con: cols=100 lines=27
md history

:loop

echo %date% %time%

adb devices
adb shell " cat /sdcard/log/bdlog/bdLog | grep "testEcallNum" | tail -3 "
adb shell " cat /etc/tbox-version "
adb shell " cat /gwmapp/config/version.json "

echo %date% %time%  >> history/info.log
adb devices >> history/info.log
adb shell " cat /sdcard/log/bdlog/bdLog | grep "testEcallNum" | tail -3 "  >> history/info.log
adb shell " cat /etc/tbox-version "  >> history/info.log
adb shell " cat /gwmapp/config/version.json "  >> history/info.log

ping /n 5 127.1 >nul

goto loop