@echo off

title cat_ccmni
color 02
mode con: cols=50 lines=4
md history

:loop

echo %date% %time%
adb shell " ifconfig | grep ccmni "

echo %date% %time% >> history/ccmni.log
adb shell " ifconfig | grep ccmni "  >> history/ccmni.log

ping /n 5 127.1 >nul
goto loop