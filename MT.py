import time
import unittest
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement

from locators import locators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class NDPdLoginTest(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        print("inside setup class")
        cls.driver = webdriver.Chrome(executable_path="C:/Users/pavv/Desktop/exe_files/chromedriver"
                                                      ".exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_A_NDPd_PBA_login_validation(self):
        print("inside PBS_login_validation")
        self.driver.get(locators.site_url)
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id(locators.login_id).send_keys(locators.pba_login)
        self.driver.find_element_by_id(locators.pwd_id).send_keys(locators.NDPd_pwd)
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id(locators.login_button_id).click()
        time.sleep(5)

    def test_B_NDPd_Menu_Module_Template(self):
        self.driver.find_element_by_xpath(locators.window_xpath).click()
        self.driver.implicitly_wait(10)

        # to select Module_Template from Menu bar

        flag = self.driver.find_element_by_xpath(locators.Module_Template_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", flag)
        self.driver.implicitly_wait(30)
        flag.click()

        # to click on plus symbol
        self.driver.find_element_by_xpath(locators.Module_Template_plus_button_xpath).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(locators.Module_name_xpath).send_keys("Module_Template_automation75")
        time.sleep(3)
        self.driver.find_element_by_xpath(locators.Module_site_type_xpath).click()
        time.sleep(3)

        self.driver.find_element_by_xpath(locators.Module_site_type_xpath_value).click()
        time.sleep(3)

        # self.driver.find_element_by_xpath(locators.Module_Time_unit_xpath).click()
        # time.sleep(3)
        #
        # self.driver.find_element_by_xpath(locators.Module_Time_unit_value_xpath).click()
        # time.sleep(3)

        self.driver.find_element_by_xpath(locators.Module_save_basic_details_xpath).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(locators.Module_add_new_grp_xpath).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(locators.Module_grp_name).send_keys("Group1")
        time.sleep(3)
        self.driver.find_element_by_xpath(locators.Module_grp_weight_xpath).send_keys("100")
        time.sleep(5)

        ActionChains(self.driver).key_down(Keys.TAB).key_up(Keys.TAB).perform()
        ActionChains(self.driver).key_down(Keys.TAB).key_up(Keys.TAB).perform()
        ActionChains(self.driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
        time.sleep(5)
        self.driver.find_element_by_xpath(locators.MT_manage_task_and_MS).click()
        time.sleep(3)

        # Mouse over

        self.driver.find_element_by_xpath(locators.MT_grp_mouse_over_xpath).click()
        # ActionChains.move_to_element(search_grp).perform()
        self.driver.find_element_by_xpath(locators.MT_grp_plus_xpath).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(locators.MT_task_name_xpath).send_keys("task1")
        time.sleep(2)
        self.driver.find_element_by_xpath(locators.MT_task_weight_xpath).send_keys("100")
        time.sleep(2)
        self.driver.find_element_by_xpath(locators.MT_add_task_in_grp_xpath).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(locators.MT_task_xpath).click()
        self.driver.find_element_by_xpath(locators.MT_Task_start_date_xpath).send_keys("1")
        self.driver.find_element_by_xpath(locators.MT_Task_execution_time_xpath).send_keys("2")
        self.driver.find_element_by_xpath(locators.MT_Task_save_xpath).click()
        self.driver.find_element_by_xpath(locators.MT_deploy_xpath).click()


    # @classmethod
    # def tearDownClass(cls):
    #     print("inside teardownclass")
    #     cls.driver.close()
    #     print("NDPd Login test has been completed")


if __name__ == "__main__":
    unittest.main()
    # unittest.main(
    #     testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/pavv/PycharmProjects/first_project/Reports"))
