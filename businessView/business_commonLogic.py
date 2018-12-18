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
import sys
# sys.setrecursionlimit(100000)

"""
the roles
·   元素By定义在方法外，在方法内找寻以及调用
·   元素命名根据它的属性命名
·   元素By定义时，命名的最后一个单词的首字母小写，找寻元素是首字母大写，如：
·   id_soft_item_name&id_soft_item_Name
·
the goal scenario:
1. check the app list and its' version
2. check the APPs under each tab
"""
#
class CommonLogicValidation(CommonFunc):

    text_view=(By.CLASS_NAME,'android.widget.TextView')
    rec_root = (By.XPATH, '//*[@text="推荐"]')
    apps_all_GridV = (By.CLASS_NAME, 'android.widget.GridView')

    id_frame_layout_img = (By.ID, 'com.orbbec.gdgamecenter:id/framelayout_img')
    id_btn=(By.ID, 'com.orbbec.gdgamecenter:id/btn')
    id_soft_down = (By.ID, 'com.orbbec.gdgamecenter:id/soft_down') #install page download
    id_soft_name = (By.ID, 'com.orbbec.gdgamecenter:id/soft_name') #install page

    id_soft_view_pager = (By.ID, 'com.orbbec.gdgamecenter:id/soft_viewpager')
    id_soft_item_view=(By.ID, 'com.orbbec.gdgamecenter:id/soft_item_view')
    id_soft_item_name = (By.ID, 'com.orbbec.gdgamecenter:id/soft_item_name')
    id_soft_item_version = (By.ID, 'com.orbbec.gdgamecenter:id/soft_item_version') # app_manager_page
    id_soft_item_size = (By.ID, 'com.orbbec.gdgamecenter:id/soft_item_size') # app_manager_page

    id_soft_item_uninstall_fl = (By.ID, 'com.orbbec.gdgamecenter:id/soft_item_uninstall_fl')
    id_confir_btn = (By.ID, 'com.orbbec.gdgamecenter:id/confir_btn')
    id_cancel_btn = (By.ID, 'com.orbbec.gdgamecenter:id/cancel_btn')

    id_dialog_notices_root=(By.ID, 'com.orbbec.gdgamecenter:id/dialog_notices_root') # install spaceless
    id_cancel_exit_btn = (By.ID, 'com.orbbec.gdgamecenter:id/cancel_exit_btn') #retain page
    id_content_layout = (By.ID, 'com.orbbec.gdgamecenter:id/centent_layout') #retain page

    id_person_center_app_manager = (By.ID, 'com.orbbec.gdgamecenter:id/person_center_app_manager')
    id_all_update_btn = (By.ID, 'com.orbbec.gdgamecenter:id/all_update_btn')

    # rec_root = (By.ID, 'com.orbbec.gdgamecenter:id/home_item_tw_content')

    """
 go to certain page 
     """
    def confirm_on_homePge(self):

        try:
            self.find_element(*self.rec_root)
        except TimeoutException:
            print("=======what a pity, we aren't get to homepage!!=======")
        else:
            print('======well done,we are on homepage 推荐!!!!!=======')

    def go_to_2ndTab(self):
        self.confirm_on_homePge()
        self.KeyEvent(self.KEYCODE_DPAD_RIGHT, 2)

        tab_name = (By.XPATH, '//*[@text="益智教育"]')
        try:
            self.find_element(*tab_name)
        except TimeoutException:
            print("=======what a pity, we aren't get to 益智教育 tab!!=======")
        else:
            print('======well done,we are on the second tab 益智教育!!!!!=======')

    def go_to_3rdTab(self):
        self.confirm_on_homePge()
        self.KeyEvent(self.KEYCODE_DPAD_RIGHT, 3)

        tab_name = (By.XPATH, '//*[@text="健康互动"]')
        try:
            self.find_element(*tab_name)
        except TimeoutException:
            print("=======what a pity, we aren't get to 健康互动 tab!!=======")
        else:
            print('======well done,we are on the third  tab 健康互动!!!!!=======')

    def go_to_4thTab(self):
        self.confirm_on_homePge()
        self.KeyEvent(self.KEYCODE_DPAD_RIGHT, 4)

        tab_name = (By.XPATH, '//*[@text="休闲娱乐"]')
        try:
            self.find_element(*tab_name)
        except TimeoutException:
            print("=======what a pity, we aren't get to 休闲娱乐 tab!!=======")
        else:
            print('======well done,we are on fourth tab闲休娱乐!!!!!=======')

    def go_to_person_center(self):
        self.confirm_on_homePge()
        self.KeyEvent(self.KEYCODE_DPAD_RIGHT, 5)


        try:
            self.find_element(*self.id_person_center_app_manager)
        except TimeoutException:
            print("=======what a pity, we aren't get to 个人中心 tab!!=======")
        else:
            print('======well done,we are on 个人中心 tab!!!!!=======')

    def go_to_app_managePage(self):
        self.go_to_person_center()

        self.find_element(*self.id_person_center_app_manager).click()
        sleep(5)

        try:
            self.find_element(*self.id_all_update_btn)
        except NoSuchElementException:
            print("=======what a pity, we aren't get to 应用管理 页!!=======")
        else:
            print('======well done,we are on 应用管理 页!!!!!=======')

    """
apps installation 
    """
    def install_certain_app(self):
        self.confirm_on_homePge()

        self.find_element(*self.id_frame_layout_img).click()
        self.KeyEvent(self.KEYCODE_ENTER)
        sleep(3)

        try:
            app_installBtn=self.find_element(*self.id_soft_down)
        except NoSuchElementException:
            print("此应用已下载")
        else:

            app_installBtn.click()
            print("请注意，有个盒子可能需要手动点击下载")

    def uninstall_certain_app(self,appname):
        self.go_to_app_managePage()
        app_soft_viewPge=self.find_element(*self.id_soft_view_pager)
        app_soft_views=app_soft_viewPge.find_elements(*self.id_soft_item_view)
        for views in app_soft_views :
            name=views.find_element(*self.id_soft_item_name).text
            uninstall_btn=views.find_element(self.id_soft_item_uninstall_fl)
            if appname==name():
                uninstall_btn.click()
                print("请留意，有可能需要你的点击")
            break

    def uninstall_all_app(self):
        self.go_to_app_managePage()
        app_soft_viewPge=self.find_element(*self.id_soft_view_pager)
        app_uninstall_btns=app_soft_viewPge.find_elements(*self.id_soft_item_uninstall_fl)
        for app in app_uninstall_btns:
            try:
                app_uninstall_Btn = self.find_element(*self.id_soft_item_uninstall_fl)
            except NoSuchElementException:
                print("没有找到卸载按钮")
            else:
                app_uninstall_Btn.click()
                sleep(3)
                try:
                    app_uninstall_Btn = self.find_element(*self.id_confir_btn)
                except NoSuchElementException:
                    print("卸载二次弹窗没有找到")
                else:
                    app_uninstall_Btn.click()
                    print("请留意，有可能需要你的点击")

    def install_insufficient_notice(self):
        """

        """
        try:
            space_insufficient_notice_Root = self.find_element(*self.id_dialog_notices_root)
        except NoSuchElementException:
            print("=====oops! can't find notice dialog=======")
        else:
            space_insufficient_notice_TextView = space_insufficient_notice_Root.find_element(*self.text_view)
            notice_text=space_insufficient_notice_TextView[0].text # here are three text views

            if notice_text=='存储空间不足':
                print('well done RIGHT notice text:',notice_text)
            else:
                print("=====oops! illegal notice text=======")

            space_insufficient_notice_known_btn =space_insufficient_notice_Root.find_element(*self.id_btn)
            space_insufficient_notice_known_btn.click()


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
        app_soft_IV = apps_all_GV.find_elements(*self.id_soft_item_view)

        app_pge_set = set()
        app_sizeDic={}
        for gameParent in app_soft_IV:
            name = gameParent.find_element(*self.id_soft_item_name).text
            version = gameParent.find_element(*self.id_soft_item_version).text
            versionStr = 'v' + version[3:]
            size = gameParent.find_element(*self.id_soft_item_size).text
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

    def get_game_name_from_retainPg(self):
        name_list = []

        self.confirm_on_homePge()
        self.KeyEvent(self.KEYCODE_BACK)

        """
        get the name list of the random recommended games
        """
        game_content = self.find_element(*self.id_content_layout)
        game_names = game_content.find_elements(*self.id_soft_item_name)

        for name in game_names:
            name_list.append(name.text)
        self.find_element(*self.id_cancel_exit_btn).click()
        sleep(10)
        return name_list





if __name__ == '__main__':
    csv_file = '../data_input/sichuanAppList.csv'
    driver=desired_caps()

    Intial=CommonLogicValidation(driver)
    Intial.go_to_2ndTab()
    # Intial.go_to_3rdTab()
    # Intial.go_to_4thTab()
    # Intial.go_to_person_center()
    # Intial.go_to_app_managePage()