@title pull_bdLog

@set a=bdLog_%date:~5,2%%date:~8,2%_%time:~0,2%%time:~3,2%
md %a%

adb pull /sdcard/log/bdlog/bdLog %a%

@cmd