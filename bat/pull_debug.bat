@title pull_debug

@set a=debug_%date:~5,2%%date:~8,2%_%time:~0,2%%time:~3,2%
md %a%

adb pull /mnt/sdcard/logreadtmp.log %a%/logreadtmp.log
adb pull /mnt/sdcard/dmesgtmp.log %a%/dmesgtmp.log
adb pull /mnt/sdcard/mtklog %a%
adb pull /var/log/audio_dump %a%
adb pull /sdcard/log %a%

@cmd