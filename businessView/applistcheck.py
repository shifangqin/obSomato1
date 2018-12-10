from common.desired_caps import desired_caps
from common.common_func import Common

class CheckAppList(Common):
 '''
the goal scenario:
1. check the app list and its' version
2. check the APPs under each tab

 '''


if __name__ == '__main__':
    driver = desired_caps()
    csv_file = '../data_input/app_list.csv'