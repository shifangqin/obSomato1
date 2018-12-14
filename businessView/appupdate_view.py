from common.desired_caps import desired_caps
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from common.common_func import CommonFunc
from time import sleep

import subprocess
import re

class AppUpdateView(CommonFunc):

    rec_root = (By.XPATH, '//*[@text="益智教育"]')

    def get_free_size(self):
        command = 'adb shell df'
        p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
        out = p.communicate()[0]
        size, used, free = re.findall(r'/data\s+(\d+\.\d+)\w\s+(\d+\.\d+)\w\s+(\d+\.\d+)\w', str(out))[0]
        return size, used, free

    def get_required_size(self):
        reqSize= 200
        return reqSize

    def get_inject_size(self):
        freeSize=float(self.get_free_size())*1024
        reqSize= self.get_required_size()
        injectSize= freeSize -reqSize+1
        return injectSize

    def judge_sapce_insufficent_messge(self):
