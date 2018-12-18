from baseView.baseView import BaseView
from selenium.webdriver.common.by import By
import logging
import csv
import time,os
import subprocess
import re
from time import sleep


class CommonFunc(BaseView):
    # 常用keyevent事件
    KEYCODE_HOME=3
    KEYCODE_MENU=82
    KEYCODE_BACK=4
    KEYCODE_POWER=26
    KEYCODE_DPAD_UP=19
    KEYCODE_DPAD_DOWN=20
    KEYCODE_DPAD_LEFT=21
    KEYCODE_DPAD_RIGHT=22

    def adbKeyEvent(self, Key_code, num_of_acts):
        while num_of_acts:
            adb ='adb shell input keyevent %s'%Key_code
            os.system(adb)
            num_of_acts-=1
        sleep(3)
    def getTime(self):
        self.now=time.strftime("%Y-%m-%d %H_%M_%S")
        return self.now

    def getScreenShot(self,module):
        time=self.getTime()
        image_file=os.path.dirname(os.path.dirname(__file__))+'/screenshots/%s_%s.png' %(module,time)

        logging.info('get %s screenshot' %module)
        self.driver.get_screenshot_as_file(image_file)

    def get_csv_data(self,csv_file,line):
        with open(csv_file,'r',encoding='utf-8-sig') as file:
            reader=csv.reader(file)
            for index,row in enumerate(reader,1):
                if index==line:
                    return row

    def get_excel_data(self,excel_file):
        logging.info('=====get_excel_data========')

    def get_data_freeSize(self):
        command = 'adb shell df'
        p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
        out = p.communicate()[0]
        size, userd, fsize = re.findall(r'/data\s+(\d+\.\d+)G\s+(\d+\.\d+)G\s+(\d+\.\d+)G', str(out))[0]

        return size, userd, fsize






