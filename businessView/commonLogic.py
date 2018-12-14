#coding:'UTF-8'
from common.desired_caps import desired_caps
from common.common_func import CommonFunc
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
# import pandas as pd
import os
import subprocess
import re


# import sys
# sys.setrecursionlimit(100000)
"""
the goal scenario:
1. check the app list and its' version
2. check the APPs under each tab
"""
#
class CommonLogicValidation(CommonFunc):
    # home page
    rec_root = (By.XPATH, '//*[@text="推荐"]')
    reco_sec_appRoot = (By.ID, 'com.orbbec.gdgamecenter:id/framelayout_img')
    # rec_root = (By.ID, 'com.orbbec.gdgamecenter:id/home_item_tw_content')

    #person center page
    personApp_manager_Btn = (By.ID, 'com.orbbec.gdgamecenter:id/person_center_app_manager')
    allUpdate_Btn = (By.ID, 'com.orbbec.gdgamecenter:id/all_update_btn')

    soft_view_pager = (By.ID, 'com.orbbec.gdgamecenter:id/soft_viewpager')
    soft_item_view=(By.ID,'com.orbbec.gdgamecenter:id/soft_item_view')
    soft_item_name = (By.ID, 'com.orbbec.gdgamecenter:id/soft_item_name')

    app_uninstall_btn = (By.ID, 'com.orbbec.gdgamecenter:id/soft_item_uninstall_fl')
    app_uninstall_confir_btn = (By.ID, 'com.orbbec.gdgamecenter:id/confir_btn')
    app_uninstall_cancel_btn = (By.ID, 'com.orbbec.gdgamecenter:id/cancel_btn')

    # install page
    install_Btn = (By.ID, 'com.orbbec.gdgamecenter:id/soft_down')
    app_nameTV = (By.ID, 'com.orbbec.gdgamecenter:id/soft_name')
    # ok_installBtn = (By.ID, 'com.android.packageinstaller:id/ok_button')
    # launch_installBtn=(By.ID,'com.android.packageinstaller:id/launch_button')
    # done_installBtn = (By.ID, 'com.android.packageinstaller:id/done_button')
    apps_all_GridV = (By.CLASS_NAME, 'android.widget.GridView')


    app_name = (By.ID, 'com.orbbec.gdgamecenter:id/soft_item_name')
    app_version = (By.ID, 'com.orbbec.gdgamecenter:id/soft_item_version')
    app_size = (By.ID, 'com.orbbec.gdgamecenter:id/soft_item_size')

    """
key events
    """
    def keyEvents_swipe_right(self,NumofActs):
        while NumofActs:
            self.driver.keyevent(22)
            NumofActs=NumofActs-1
        sleep(2)
    def keyEvents_swipe_left(self,NumofActs):
        while NumofActs:
            self.driver.keyevent(21)
        sleep(2)
    def keyEvents_confirm(self):
        self.driver.keyevent(66)
    def keyEvents_return(self,NumofActs):
        while NumofActs:
            self.driver.keyevent(4)
        sleep(2)
    def adbKeyEvent(keyname):
        adb='adb shell input keyevnet %s'%keyname
        os.system(adb)
    """
get to certain page
    """
    def confirm_on_homePge(self):

        try:
            self.find_element(*self.rec_root)
        except TimeoutException:
            print("=======what a pity, we aren't get to homepage!!=======")
        else:
            print('======well done,we are on homepage 推荐!!!!!=======')
    def swip_to_secondTab(self):
        self.confirm_on_homePge()
        self.keyEvents_swipe_right(2)

        tab_name = (By.XPATH, '//*[@text="益智教育"]')
        try:
            self.find_element(*tab_name)
        except TimeoutException:
            print("=======what a pity, we aren't get to 益智教育 tab!!=======")
        else:
            print('======well done,we are on the second tab 益智教育!!!!!=======')
    def swip_to_thirdTab(self):
        self.confirm_on_homePge()
        self.keyEvents_swipe_right(3)

        tab_name = (By.XPATH, '//*[@text="健康互动"]')
        try:
            self.find_element(*tab_name)
        except TimeoutException:
            print("=======what a pity, we aren't get to 健康互动 tab!!=======")
        else:
            print('======well done,we are on the third  tab 健康互动!!!!!=======')
    def swip_to_fourthTab(self):
        self.confirm_on_homePge()
        self.keyEvents_swipe_right(4)

        tab_name = (By.XPATH, '//*[@text="休闲娱乐"]')
        try:
            self.find_element(*tab_name)
        except TimeoutException:
            print("=======what a pity, we aren't get to 休闲娱乐 tab!!=======")
        else:
            print('======well done,we are on fourth tab闲休娱乐!!!!!=======')
    def go_person_center(self):
        self.confirm_on_homePge()
        self.keyEvents_swipe_right(5)


        try:
            self.find_element(*self.personApp_manager_Btn)
        except TimeoutException:
            print("=======what a pity, we aren't get to 个人中心 tab!!=======")
        else:
            print('======well done,we are on 个人中心 tab!!!!!=======')
    def go_to_app_managePage(self):
        self.go_person_center()

        self.find_element(*self.personApp_manager_Btn).click()
        sleep(5)

        try:
            self.find_element(*self.allUpdate_Btn)
        except NoSuchElementException:
            print("=======what a pity, we aren't get to 应用管理 页!!=======")
        else:
            print('======well done,we are on 应用管理 页!!!!!=======')
    """
apps installation 
    """
    def install_certain_app(self):
        self.confirm_on_homePge()

        self.find_element(*self.reco_sec_appRoot).click()
        self.keyEvents_confirm()
        sleep(3)

        try:
            app_installBtn=self.find_element(*self.install_Btn)
        except NoSuchElementException:
            print("此应用已下载")
        else:

            app_installBtn.click()
            print("请注意，有个盒子可能需要手动点击下载")
    def uninstall_certain_app(self,appname):
        self.go_to_app_managePage()
        app_soft_viewPge=self.find_element(*self.soft_view_pager)
        app_soft_views=app_soft_viewPge.find_elements(*self.soft_item_view)
        for views in app_soft_views :
            name=views.find_element(*self.soft_item_name).text
            uninstall_btn=views.find_element(self.app_uninstall_btn)
            if appname==name():
                uninstall_btn.click()
                print("请留意，有可能需要你的点击")
            break
    def uninstall_all_app(self):
        self.go_to_app_managePage()
        app_soft_viewPge=self.find_element(*self.soft_view_pager)
        app_uninstall_btns=app_soft_viewPge.find_elements(*self.app_uninstall_btn)
        for app in app_uninstall_btns:
            try:
                app_uninstall_Btn = self.find_element(*self.app_uninstall_btn)
            except NoSuchElementException:
                print("没有找到卸载按钮")
            else:
                app_uninstall_Btn.click()
                sleep(3)
                try:
                    app_uninstall_Btn = self.find_element(*self.app_uninstall_confir_btn)
                except NoSuchElementException:
                    print("卸载二次弹窗没有找到")
                else:
                    app_uninstall_Btn.click()
                    print("请留意，有可能需要你的点击")


    """
person Center 
    """
    def get_app_input_set_from_CSVfile(self):
        app_input_set=set()

        csv_file = '../data_input/sichuanAppList.csv'
        rowNum_pointer = self.get_csv_data(csv_file, 1)
        rowNum=1

        while not rowNum_pointer==None:
            app_pointer = tuple(rowNum_pointer)
            app_input_set.add(app_pointer)
            # print(app_input_Set, "O(∩_∩)")
            rowNum+=1
            rowNum_pointer = self.get_csv_data(csv_file, rowNum)
        return app_input_set
    def get_app_info_from_personCenterPge(self):
        self.go_to_app_managePage()



        apps_all_GV = self.find_element(*self.apps_all_GridV)
        app_soft_IV = apps_all_GV.find_elements(*self.soft_item_view)

        app_pge_set = set()
        app_sizeDic={}
        for gameParent in app_soft_IV:
            name = gameParent.find_element(*self.app_name).text
            version = gameParent.find_element(*self.app_version).text
            versionStr = 'v' + version[3:]
            size = gameParent.find_element(*self.app_size).text
            app_sizeDic[name]=size
            app_tuple = (name, versionStr)
            app_pge_set.add(app_tuple)
        return app_pge_set,app_sizeDic
    def check_appList_meet_req(self, app_input_set, app_pge_set):

        if app_input_set.difference(app_pge_set)==set():
            print("没有缺少应用")
        else:
            print("缺少如下应用：",app_input_set.difference(app_pge_set))

        if app_pge_set.difference(app_input_set)==set():
            print("没有多出应用:")
        else:
            print("多出如下应用：",app_pge_set.difference(app_input_set))
    """
retain page
    """
    def get_game_name_from_retainPg(self):

        exitBtn = (By.ID, 'com.orbbec.gdgamecenter:id/cancel_exit_btn')
        game_content = (By.ID, 'com.orbbec.gdgamecenter:id/centent_layout')
        game_names = (By.CLASS_NAME, 'android.widget.TextView')

        name_list = []

        # confirm it is on home page, and then send "return" key

        self.confirm_on_homePge()
        self.keyEvents_return(1)

        """
        get the name list of the random recommended games
        """
        game_content = self.find_element(*game_content)
        game_names = game_content.find_elements(*game_names)

        for name in game_names:
            name_list.append(name.text)
        self.find_element(*exitBtn).click()
        sleep(10)
        return name_list

    def inject_certain_size(self,reqsize):
        command1 = 'adb shell df'
        bsNum = 1024
        p = subprocess.Popen(command1, stdout=subprocess.PIPE, shell=True)
        out = p.communicate()[0]
        size, userd, freesize = re.findall(r'/data\s+(\d+\.\d+)G\s+(\d+\.\d+)G\s+(\d+\.\d+)G', str(out))[0]

        countNum = freesize - int(reqsize / bsNum) + 1
        command2='dd if=/dev/zero of=test.zip bs=%s count=%s'%(bsNum,countNum)
        os.system(command2)


if __name__ == '__main__':
    csv_file = '../data_input/sichuanAppList.csv'
    driver=desired_caps()
    commonfuc=CommonFunc(driver)
    Intial=CommonLogicValidation(driver)





    """
    check retain page app appear in random
    """
    # list1 = intialPara.get_game_name_from_retainPg()
    #
    # list2 = intialPara.get_game_name_from_retainPg()
    # if list1 == list2:
    #     print("不是随机刷新")
    # else:
    #     print("随机刷新")