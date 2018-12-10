from appium import webdriver
import yaml
import logging
import logging.config
import os
from time import sleep

"""
define the logs' format
"""
CON_LOG = '../config/log.conf'
logging.config.fileConfig(CON_LOG)
logging=logging.getLogger()

def get_base_dir():
    return os.path.dirname(os.path.dirname(__file__))   # __file__: get base_dir of the current file

def desired_caps():
    file = open('../config/capability.yaml', 'r')
    data = yaml.load(file)

    desired_caps = {}

    desired_caps['platformName'] = data['platformName']
    desired_caps['platformVersion'] = data['platformVersion']
    desired_caps['deviceName'] = data['deviceName']

    desired_caps['app'] = os.path.join(get_base_dir(), 'app', data['appName'])
    desired_caps['appPackage'] = data['appPackage']
    desired_caps['appActivity']= data ['appActivity']
    desired_caps['noReset'] = data['noReset']
    # desired_caps['unicodeKeyboard'] = data['unicodeKeyboard']
    # desired_caps['resetKeyboard'] = data ['resetKeyboard']

    logging.info('=======start app desiredc-cpas=======')
    driver=webdriver.Remote('http://'+str(data['ip'])+':'+str(data['port'])+'/wd/hub',desired_caps)
    driver.implicitly_wait(10)
    # sleep(10)
    return driver

if __name__ == '__main__':
    desired_caps()
