@title pull_log

@set a=log_%date:~5,2%%date:~8,2%_%time:~0,2%%time:~3,2%
md %a%

adb shell "logread > /tmp/syslog.log"
adb pull /tmp/syslog.log  %a%/syslog.log
adb pull /sdcard/log  %a%

@pause