from common.desired_caps import desired_caps
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from common.common_func import CommonFunc
from time import sleep


class RetainPageView(CommonFunc):
    # driver=desired_caps()

    exitBtn = (By.ID, 'com.orbbec.gdgamecenter:id/cancel_exit_btn')
    game_content = (By.ID, 'com.orbbec.gdgamecenter:id/centent_layout')
    game_names = (By.CLASS_NAME, 'android.widget.TextView')


    def get_game_name_from_retainPg(self):
        name_list=[]
        self.driver.keyevent('4')
        WebDriverWait(self.driver, 10).until(lambda x:x.find_element(*self.exitBtn))

        """
        get the name list of the random recommended games
        """
        game_content=self.find_element(*self.game_content)
        game_names =game_content.find_elements(*self.game_names)

        for name in game_names:
            name_list.append(name.text)
        self.find_element(*self.exitBtn).click()
        sleep(10)
        return name_list

    def compare_nameList(self):
        list1=self.get_game_name_from_retainPg()

        list2=self.get_game_name_from_retainPg()
        if list1 == list2:
            return False
        else:
            return True

if __name__ == '__main__':
    driver=desired_caps()
    retainPge=RetainPageView(driver)
    result=retainPge.compare_nameList()
    print(result)