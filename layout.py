import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from os import popen
from time import sleep
from datetime import datetime
import os

class TabDemo(QTabWidget):
    def __init__(self, parent=None):
        super(TabDemo, self).__init__(parent)
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.addTab(self.tab1, "Tab 1")
        self.addTab(self.tab2, "Tab 2")
        self.addTab(self.tab3, "Tab 3")
        self.tab1UI()
        self.tab2UI()
        self.tab3UI()
        self.setWindowTitle("The Great Wall    author:Mavis")

    def tab1UI(self):
        layout = QFormLayout()

        self.text1 = QLabel('testEcallNum')
        self.edit1 = QLineEdit('17279719730',self)
        self.btn1 = QPushButton('update')
        self.btn1.clicked.connect(self.btn1Clicked)
        # layout.addWidget(self.text1,1,1)
        # layout.addWidget(self.edit1,1,2)
        # layout.addWidget(self.btn1,1,3)
        en = QHBoxLayout()
        en.addWidget(self.text1)
        en.addWidget(self.edit1)
        en.addWidget(self.btn1)
        layout.addRow(en)

        self.text2 = QLabel('volume')
        self.edit2 = QLineEdit()
        self.btn2 = QPushButton('update')
        self.btn2.clicked.connect(self.btn2Clicked)
        # layout.addWidget(self.text2, 2, 1)
        # layout.addWidget(self.edit2, 2, 2)
        # layout.addWidget(self.btn2, 2, 3)
        vl = QHBoxLayout()
        vl.addWidget(self.text2)
        vl.addWidget(self.edit2)
        vl.addWidget(self.btn2)
        layout.addRow(vl)

        # btns = ['speaker','manualEcall','autoEcall','bdLog']

        self.btn3 = QPushButton('speaker')
        self.btn3.clicked.connect(self.btn3Clicked)
        # layout.addWidget(self.btn3, 3, 1)

        self.btn4 = QPushButton('manualEcall')
        self.btn4.clicked.connect(self.btn4Clicked)
        # layout.addWidget(self.btn4, 4, 1)

        self.btn5 = QPushButton('autoEcall')
        self.btn5.clicked.connect(self.btn5Clicked)
        # layout.addWidget(self.btn5, 5, 1)

        self.btn6 = QPushButton('bdLog')
        self.btn6.clicked.connect(self.btn6Clicked)
        # layout.addWidget(self.btn6, 6, 1)

        btns = QHBoxLayout()
        btns.addWidget(self.btn3)
        btns.addWidget(self.btn4)
        btns.addWidget(self.btn5)
        btns.addWidget(self.btn6)
        layout.addRow(btns)

        self.btn7 = QPushButton('touch asn')

        btns1 = QHBoxLayout()
        btns1.addWidget(self.btn7)
        layout.addRow(btns1)

        self.te = QTextEdit()
        layout.addRow(self.te)

        self.setTabText(0, "ECALL")
        self.tab1.setLayout(layout)

    def btn1Clicked(self):
        val = self.edit1.text()
        popen('adb shell "echo %s > /home/root/_phoneNum"' % val)
        self.te.setText(f'update phoneNum:{val}')
        self.te.update()

    def btn2Clicked(self):
        val = self.edit2.text()
        popen('adb shell "amixer -c0 cset name="ADDA_DL_GAIN" %s"' % val)
        self.te.setText(f'Adjust the volume to {val}HZ')
        self.te.update()

    def btn3Clicked(self):
        popen('adb shell "touch /home/_openS && aplay /sdcard/1KHZ.wav"')

    def btn4Clicked(self):
        popen('adb shell "touch /home/root/_manual"')
        self.te.setText('touch manualEcall successed!')
        self.te.update()

    def btn5Clicked(self):
        popen('adb shell "touch /home/root/_auto"')
        self.te.setText('touch autoEcall successed!')
        self.te.update()

    def btn6Clicked(self):
        cmd = 'adb shell "tail -f /sdcard/log/bdlog/bdLog"'
        popen('start cmd.exe /K %s' % cmd)
        self.te.setText('open bdLog successed!')
        self.te.update()

    def btn7Clicked(self):
        popen('adb shell "touch /home/root/_asn"')
        self.te.setText('touch /home/root/_asn successed!')
        self.te.update()

    def tab2UI(self):
        layout = QFormLayout()

        self.fbtn1 = QPushButton('version')
        self.fbtn1.clicked.connect(self.fbtn1Clicked)
        self.fbtn2 = QPushButton('iccid')
        self.fbtn2.clicked.connect(self.fbtn2Clicked)
        self.fbtn3 = QPushButton('jannetwork')    #judge Annotation network
        self.fbtn3.clicked.connect(self.fbtn3Clicked)
        self.fbtn4 = QPushButton('annetwork')  # Annotation network
        self.fbtn4.clicked.connect(self.fbtn4Clicked)

        fbtns = QHBoxLayout()
        fbtns.addWidget(self.fbtn1)
        fbtns.addWidget(self.fbtn2)
        fbtns.addWidget(self.fbtn3)
        fbtns.addWidget(self.fbtn4)
        layout.addRow(fbtns)

        self.fbtn5 = QPushButton('net_sn')
        self.fbtn5.clicked.connect(self.fbtn5Clicked)
        self.fbtn6 = QPushButton('net_str')
        self.fbtn6.clicked.connect(self.fbtn6Clicked)
        self.fbtn7 = QPushButton('air_mode')
        self.fbtn7.clicked.connect(self.fbtn7Clicked)
        self.fbtn8 = QPushButton('fun_mode')
        self.fbtn8.clicked.connect(self.fbtn8Clicked)

        fbtns1 = QHBoxLayout()
        fbtns1.addWidget(self.fbtn5)
        fbtns1.addWidget(self.fbtn6)
        fbtns1.addWidget(self.fbtn7)
        fbtns1.addWidget(self.fbtn8)
        layout.addRow(fbtns1)

        self.ftext9 = QLabel('ping baidu')
        self.fedit9 = QLineEdit('Please enter the number of times',self)
        self.fbtn9 = QPushButton('confirm')
        self.fbtn9.clicked.connect(self.fbtn9Clicked)

        baidu = QHBoxLayout()
        baidu.addWidget(self.ftext9)
        baidu.addWidget(self.fedit9)
        baidu.addWidget(self.fbtn9)
        layout.addRow(baidu)

        self.ftext10 = QLabel('ping NAD')
        self.fedit10 = QLineEdit('Please enter the number of times',self)
        self.fbtn10 = QPushButton('confirm')
        self.fbtn10.clicked.connect(self.fbtn10Clicked)

        nad = QHBoxLayout()
        nad.addWidget(self.ftext10)
        nad.addWidget(self.fedit10)
        nad.addWidget(self.fbtn10)
        layout.addRow(nad)

        self.fte = QTextEdit()
        layout.addRow(self.fte)

        self.setTabText(1, "query")
        self.tab2.setLayout(layout)

    def fbtn1Clicked(self):
        out = popen('adb shell "cat /gwmapp/config/version.json"').read()
        self.fte.setText(out)
        self.fte.update()

    def fbtn2Clicked(self):
        cmd = 'adb shell "ql_sdk_api_test"'
        popen('start cmd.exe /K %s' % cmd)
        self.fte.setText('query iccid please input in sequence:4,0,2,1')
        self.fte.update()

    def fbtn3Clicked(self):
        out = popen('adb shell "echo "1    4    1   4" > /proc/sys/kernel/printk && ifconfig"').read()
        keyword1 = 'ccmni0'
        keyword2 = 'ccmni1'
        if keyword1 in out and keyword2 in out:
            self.fte.setText('registered on the internet succcess')
            self.fte.update()
        else:
            self.fte.setText('registered on the internet succcess' + out)
            self.fte.update()

    def fbtn4Clicked(self):
        popen('adb push E:\72k222\oversea  /gwmdata/config')
        popen('adb push E:\72k222\domestic  /gwmdata/config')
        popen('adb shell "reboot -f"').read()
        for i in range(30, 0, -1):
            self.fte.setText("\r rebooting{}秒！".format(i),end="",flush=True)
            self.fte.update()
            sleep(1)
        self.fbtn3Clicked()

    def fbtn5Clicked(self):
        cmd = 'adb shell "ql_sdk_api_test"'
        popen('start cmd.exe /K %s' % cmd)
        self.fte.setText('if you want to query network signal, please input in sequence:6,0,7,1')
        self.fte.update()

    def fbtn6Clicked(self):
        cmd = 'adb shell "ql_sdk_api_test"'
        popen('start cmd.exe /K %s' % cmd)
        self.fte.setText('if you want to query network strength please input in sequence:6,0,9,1')
        self.fte.update()

    def fbtn7Clicked(self):
        cmd = 'adb shell "ql_sdk_api_test"'
        popen('start cmd.exe /K %s' % cmd)
        self.fte.setText('if you want to switch to Airplane mode, please input in sequence:11,0,15,1')
        self.fte.update()

    def fbtn8Clicked(self):
        cmd = 'adb shell "ql_sdk_api_test"'
        popen('start cmd.exe /K %s' % cmd)
        self.fte.setText('if you want to switch to All_Function mode, please input in sequence:11,0,14,1')
        self.fte.update()

    def fbtn9Clicked(self):
        keyword = "0 packets received, 100% packet loss"
        ip = 'www.baidu.com'
        a = 0
        b = 0
        count = 0
        n = int(self.fedit9.text())
        while count < n:
            # return1=os.system('ping -n 1 -w 1 %s'%ip) #每个ip ping1次，等待时间为1s，os.system返回命令执行状态，0表示执行成功
            result = popen('adb shell ping -w 10 %s' % ip).read()
            print(result)
            if keyword in result:
                a += 1
                print('ping www.baidu.com fail:{}次\n'.format(a), end="", flush=True)
            else:
                b += 1
                print('ping www.baidu.com pass:{}次\n'.format(b), end="", flush=True)
            count += 1
        self.fte.setText('ping www.baidu.com fail:' + str(a) + 'times\n')
        self.fte.update()
        self.fte.append('ping www.baidu.com success:' + str(b) + 'times\n')
        self.fte.update()

    def fbtn10Clicked(self):
        keyword = "0 packets received, 100% packet loss"
        ip = '192.168.125.1'
        a = 0
        b = 0
        count = 0
        n = int(self.fedit10.text())
        while count < n:
            # return1=os.system('ping -n 1 -w 1 %s'%ip) #每个ip ping1次，等待时间为1s，os.system返回命令执行状态，0表示执行成功
            result = popen('adb shell ping -w 10 %s' % ip).read()
            # print(result)
            self.fte.setText('ping 192.168.125.1 {}times\n'.format(n))
            self.fte.update()
            if keyword in result:
                a += 1
                # print('ping 192.168.125.1 fail:{}次\n'.format(a), end="", flush=True)
                self.fte.append('ping 192.168.125.1 fail:{}times\n'.format(a))
                self.fte.update()
            else:
                b += 1
                # print('ping 192.168.125.1 pass:{}次\n'.format(b), end="", flush=True)
                self.fte.append('ping 192.168.125.1 success:{}times\n'.format(b))
                self.fte.update()
            count += 1

        # self.fte.append('ping 192.168.125.1 success:' + str(b) + 'times\n')
        # self.fte.update()

    def tab3UI(self):
        layout = QFormLayout()

        layout.addRow(QLabel('Please check the log to be exported'))

        bh = QHBoxLayout()

        self.qcbox1 = QCheckBox('/sdcard/log')
        self.qcbox1.stateChanged.connect(self.groove1)
        self.qcbox2 = QCheckBox('/mnt/sdcard/log')
        self.qcbox2.stateChanged.connect(self.groove2)
        self.qcbox3 = QCheckBox('/bdLog')
        self.qcbox3.stateChanged.connect(self.groove3)
        bh.addWidget(self.qcbox1)
        bh.addWidget(self.qcbox2)
        bh.addWidget(self.qcbox3)
        layout.addRow(bh)

        self.qbtn = QPushButton('confirm')
        self.qbtn.clicked.connect(self.qbtnClicked)
        layout.addRow(self.qbtn)

        self.setTabText(2, "pull log")
        self.tab3.setLayout(layout)
    cmds = []
    def groove1(self,state):
        if state == 2:
            cmd = 'adb pull /sdcard/log'
            self.cmds.append(cmd)
            # print(cmd)
    def groove2(self,state):
        if state == 2:
            cmd = 'adb pull /mnt/sdcard/log'
            self.cmds.append(cmd)
            # print(cmd)
    def groove3(self,state):
        if state == 2:
            cmd = 'adb pull /sdcard/log/bdlog/bdLog'
            self.cmds.append(cmd)
            # print(cmd)
    def qbtnClicked(self):
        now_time = datetime.now().strftime("%Y%m%d_%H%M%S")
        path = 'logs_' + now_time
        os.mkdir(path)
        keyword = 'pulled'
        k = 0
        for cmd in self.cmds:
            cmd = cmd + ' ' + path
            # print(cmd)
            out = popen('%s' % cmd ).read()
            if keyword in out:
                k += 1
        if k == len(self.cmds):
            print('pull logs success')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = TabDemo()
    demo.show()
    sys.exit(app.exec_())