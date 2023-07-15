@title manual_call
 
start start_log.sh.bat
adb shell " touch /home/root/_manual "
adb shell " tail -f /sdcard/log/bdlog/bdLog "

@cmd