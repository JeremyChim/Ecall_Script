from tkinter import Tk,Button,Text,StringVar
import os
from time import sleep
from datetime import datetime
from PIL import Image, ImageTk

root = Tk()
root.title("The Great Wall   author:Mavis")
# root.geometry("760x350")
root.configure(bg='#FFF0F5')
root.resizable(False,False)

popen = os.popen

#打开指定的图片文件，缩放至指定尺寸
def get_image(filename,width, height):
    im = Image.open(filename).resize((width,height))
    return ImageTk.PhotoImage(im)

def devices():
    out = popen('adb devices').read()
    text.insert('end', "\nadb设备：\n" + out)

def update_phoneNum():
    popen('adb shell "echo 17279719730 > /home/root/_phoneNum"')
    sleep(0.5)
    out = popen('adb shell "grep "testEcallNum" /sdcard/log/bdlog/bdLog"').read()
    out = out[-13:]
    text.insert('end',"\n测试号码："+out)

def manualcall():
    # set phone_action: manEcall active
    # set phone_action: autoEcall active
    popen('adb shell "touch /home/root/_manual"')
    sleep(5)

    # for i in range(10, 0, -1):
    #     print("\r手动ecall拨打中{}秒！".format(i),end="",flush=True)
    #     sleep(1)

    out = popen('adb shell "grep "phone_action" /sdcard/log/bdlog/bdLog"').read()
    out = out[-17:]
    text.insert('end',"\nset phone_action:"+out)

def autocall():
    popen('adb shell "touch /home/root/_auto"')
    sleep(5)
    # for i in range(10, 0, -1):
    #     print("\r自动ecall拨打中{}秒！".format(i),end="",flush=True)
    #     sleep(1)
    out = popen('adb shell "grep "phone_action" /sdcard/log/bdlog/bdLog"').read()
    out = out[-18:]
    text.insert('end', "\nset phone_action:" + out)

def w_zhuwang():
    out = popen('adb shell "echo "1    4    1   4" > /proc/sys/kernel/printk && ifconfig"').read()
    keyword1 = 'ccmni0'
    keyword2 = 'ccmni1'
    if keyword1 in out and keyword2 in out:
        text.insert('end', "\n注网成功\n")
    else:
        text.insert('end', "\n注网失败\n")
        text.insert('end',out)

def zhuwang():
    out = popen('adb push E:/72k222\oversea  /gwmdata/config').read()
    out1 = popen('adb push E:/72k222\domestic  /gwmdata/config').read()
    out2 = popen('adb shell "reboot -f"').read()
    text.insert('insert', "\nout\n")
    text.insert('insert', "\nout1\n")
    text.insert('insert', "\nout3\n")
    for i in range(30, 0, -1):
        print("\r重启中{}秒！".format(i),end="",flush=True)
        sleep(1)
    w_zhuwang()

def cat_ver():
    out = popen('adb shell "cat /gwmapp/config/version.json"').read()
    text.insert('end', "\n版本信息：\n")
    text.insert('end', out)

def sound():
    out = popen('adb shell "amixer -c0 cset name="ADDA_DL_GAIN" 3000"').read()
    out = out[-6:]
    text.insert('end',"\n调节喇叭音量（HZ）："+out)

def spearker_test():
    popen('adb shell "touch /home/_openS && aplay /sdcard/1KHZ.wav"')

def cat_iccid():
    cmd = 'adb shell "ql_sdk_api_test"'
    popen('start cmd.exe /K %s' %cmd )
    text.insert('end', '\n查询iccid请依次输入4,0,2,1\n')

def cat_network():
    cmd = 'adb shell "ql_sdk_api_test"'
    popen('start cmd.exe /K %s' %cmd)
    text.insert('end', '\n查询网络信号请依次输入6,0,7,1\n')

def cat_network1():
    cmd = 'adb shell "ql_sdk_api_test"'
    popen('start cmd.exe /K %s' %cmd)
    text.insert('end', '\n查询信号强度请依次输入6,0,9,1\n')

def Airplane_mode():
    cmd = 'adb shell "ql_sdk_api_test"'
    popen('start cmd.exe /K %s' %cmd)
    text.insert('end', '\n切换飞行模式请依次输入11,0,15,1\n')

def Full_func():
    cmd = 'adb shell "ql_sdk_api_test"'
    popen('start cmd.exe /K %s' % cmd)
    text.insert('end', '\n切换全功能模式请依次输入11,0,14,1\n')

def reboot():
    popen('adb shell "reboot -f"')
    text.insert('end', '\n重启中。。。\n')

def bdLog():
    cmd = 'adb shell "tail -f /sdcard/log/bdlog/bdLog"'
    popen('start cmd.exe /K %s' % cmd)

def pull_log():
    now_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = 'logs_' + now_time
    os.mkdir(path)
    popen('adb shell "logread > /tmp/syslog.log"')
    popen('adb pull /tmp/syslog.log %s ' % path)
    popen('adb pull /sdcard/log %s ' % path)
    text.insert('end', '\n导出系统日志syslog.log&&/sdcard/log\n')

def ping_baidu():
    keyword = "0 packets received, 100% packet loss"
    ip = 'www.baidu.com'
    a = 0
    b = 0
    count = 0
    while count < 200:
        # return1=os.system('ping -n 1 -w 1 %s'%ip) #每个ip ping1次，等待时间为1s，os.system返回命令执行状态，0表示执行成功
        result = popen('adb shell ping -w 10 %s' % ip).read()
        print(result)
        if keyword in result:
            a += 1
            print('ping www.baidu.com fail:{}次\n'.format(a),end="",flush=True)
        else:
            b += 1
            print('ping www.baidu.com pass:{}次\n'.format(b),end="",flush=True)
        count += 1
    text.insert('end', 'ping www.baidu.com fail:' + str(a) + '次\n')
    text.insert('end', 'ping www.baidu.com pass:' + str(b) + '次\n')

def ping_nad():
    keyword = "0 received, 100% packet loss"
    ip = '192.168.125.1'
    a = 0
    b = 0
    count = 0
    while count < 50:
        # return1=os.system('ping -n 1 -w 1 %s'%ip) #每个ip ping1次，等待时间为1s，os.system返回命令执行状态，0表示执行成功
        result = popen('adb shell ping -w 5 %s' % ip).read()
        print(result)
        if keyword in result:
            a += 1
            print('ping 192.168.125.1 fail:{}次\n'.format(a),end="",flush=True)
        else:
            b += 1
            print('ping 192.168.125.1 pass:{}次\n'.format(b),end="",flush=True)
        count += 1
    text.insert('end', '\nping 192.168.125.1 fail:' + str(a) + '次\n')
    text.insert('end', '\nping 192.168.125.1 pass:' + str(b) + '次\n')

def exit():
    root.destroy()

texts = ['adb_devices','修改号码','手动ecall','自动ecall','是否注网','注网重启','查询版本','查询iccid',
         '调节声音','测试喇叭','网络信号','信号强度','飞行模式','全功能模式','TBOX重启','打开bdLog','导出log',
         'ping baidu','ping NAD','退出']
funs = [devices,update_phoneNum,manualcall,autocall,w_zhuwang,zhuwang,cat_ver,cat_iccid,sound,
        spearker_test,cat_network,cat_network1,Airplane_mode,Full_func,reboot,bdLog,pull_log,ping_baidu,ping_nad,
        exit]
len = len(texts)
count = 6
flag = int(len/count)+2
# text_img = get_image('flower.png',200,200)
for i in range(len):
    row = i%count
    col = int(i/count)+1
    button = Button(root,text=texts[i],height=2,width=10,command=funs[i],bg='#FFC0C8').grid(row=row,column=col,padx=2,pady=2)

#bg='#FFC0C8'

text = Text(root,bg='#FFC0C8')
text.grid(row=0,rowspan=6,column=flag,columnspan=len+2,padx=5,pady=5)

root.mainloop()