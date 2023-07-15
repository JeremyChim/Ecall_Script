@echo off

title menu
mode con: cols=50 lines=30

:menu

cls
echo author : Jer
echo date : 2023-7-15
echo version : v3.0
echo.

echo 0	monitor
echo 1	pull_log
echo 2	auto_call
echo 3	manual_call
echo 4	update_num
echo 5	tailf_bdLog
echo 6	airplane_mode_on
echo 7	airplane_mode_off
echo 8	reboot
echo 9	sound
echo 10	cat_network
echo 11	ql_sdk_api_test
echo 12	cat_iccid
echo 13	tailf_dislog
echo 14	debug
echo 15	cat_bdLog
echo 16	start_log.sh
echo 17	done_log.sh.bat
echo 18	grep_signa
echo 19	grep_eu_ecall
echo 20	grep_gnss
echo 21	grep_monitor
echo 22	grep_logread
echo -1	exit
echo.

set /p a= ...... 

if %a%== -1		exit
if %a%== 0		goto monitor
if %a%== 1		start pull_log.bat
if %a%== 2		start auto_call.bat
if %a%== 3		start manual_call.bat
if %a%== 4		start update_num.bat
if %a%== 5		start tailf_bdLog.bat
if %a%== 6		start airplane_mode_on.bat
if %a%== 7		start airplane_mode_off.bat
if %a%== 8		start reboot.bat
if %a%== 9		start sound.bat
if %a%== 10		start cat_network.bat
if %a%== 11		start ql_sdk_api_test.bat
if %a%== 12		start cat_iccid.bat
if %a%== 13		start tailf_dislog.bat
if %a%== 14		start debug.bat
if %a%== 15		start cat_bdLog.bat
if %a%== 16		start start_log.sh.bat
if %a%== 17		start done_log.sh.bat
if %a%== 18		start grep_signa.bat
if %a%== 19		start grep_eu_ecall.bat
if %a%== 20		start grep_gnss.bat
if %a%== 21		start grep_monitor.bat
if %a%== 22		start grep_logread.bat


pause
goto menu

:monitor
start info.bat
start ps.bat
start ccmni.bat
goto menu