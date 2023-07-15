@title sound
@mode con: cols=100 lines=10

@set /p a= sound (0~65535) : 
adb shell " amixer -c0 cset name="ADDA_DL_GAIN" %a% "

@pause