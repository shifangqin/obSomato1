from selenium.webdriver.support.ui import WebDriverWait
from common.desired_caps import driver
# from capability import appium_cap

def getGameNamefromRetainPg():
    # confirm it is on home page, and then sen "return" key
    WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath('//*[@text="益智教育"]'))
    driver.keyevent('4')  # send "return" key
    #driver.implicitly_wait(5)

    # confirm the retain-page appears, and then get the name string of the games
    WebDriverWait(driver, 20).until(lambda x: x.find_element_by_id("com.orbbec.gdgamecenter:id/cancel_exit_btn"))
    nameStri1 = driver.find_element_by_id('com.orbbec.gdgamecenter:id/one_name').text + driver.find_element_by_id(
        'com.orbbec.gdgamecenter:id/two_name').text + driver.find_element_by_id(
        'com.orbbec.gdgamecenter:id/three_name').text + driver.find_element_by_id(
        'com.orbbec.gdgamecenter:id/four_name').text
    print(nameStri1)
    driver.find_element_by_id('com.orbbec.gdgamecenter:id/cancel_exit_btn').click()
    return nameStri1


nameStri1 = getGameNamefromRetainPg()

nameStri2 = getGameNamefromRetainPg()


if nameStri1 == nameStri2:
    print("(灬ꈍ ꈍ灬)随机机制判定为失败！！")
    pass
else:
    print("(*￣︶￣)随机机制判定为成功！！")