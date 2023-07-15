@echo off

title ps
color 03
mode con: cols=100 lines=14
md history

:loop

echo %date% %time%
adb shell " ps -aux | grep eu_ecall"
adb shell " ps -aux | grep gnss "
adb shell " ps -aux | grep monitor "

echo %date% %time% >> history/ps.log
adb shell " ps -aux | grep eu_ecall" >> history/ps.log
adb shell " ps -aux | grep gnss " >> history/ps.log
adb shell " ps -aux | grep monitor " >> history/ps.log

ping /n 5 127.1 >nul
goto loop
