import time
import unittest
from selenium import webdriver
from locators import locators


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

    def test_B_NDPd_Menu_TC(self):
        print("inside the Menu")
        self.driver.find_element_by_xpath(locators.window_xpath).click()
        self.driver.implicitly_wait(10)

        # to select SMPT from Menu bar

        flag = self.driver.find_element_by_xpath(locators.SMPT_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", flag)
        self.driver.implicitly_wait(30)
        flag.click()

        self.driver.find_element_by_xpath(locators.SMPT_plus_button_xpath).click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath(locators.SMP_name_xpath).send_keys("SMPT_automation15")
        time.sleep(3)

        self.driver.find_element_by_xpath(locators.SMP_site_type_xpath).click()
        time.sleep(3)

        self.driver.find_element_by_xpath(locators.SMP_site_type_xpath_value).click()
        time.sleep(3)

        # Handling check_box
        self.driver.find_element_by_xpath(locators.SMPT_Select_Module_Template_xpath).click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath(locators.SMPT_Module_Template_xpath).click()
        self.driver.find_element_by_xpath(locators.Click_on_full_window_xpath).click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath(locators.SMPT_portfolio_xpath).click()
        self.driver.implicitly_wait(15)
        self.driver.find_element_by_xpath(locators.SMPT_portfolio_xpath_value).click()
        time.sleep(4)
        self.driver.find_element_by_xpath(locators.SMPT_save_xpath).click()
        time.sleep(5)

        # Inside the Manage Modules
        self.driver.find_element_by_xpath(locators.Module_name_click_xpath).click()
        self.driver.find_element_by_xpath(locators.weightage_xpath).send_keys(100)
        time.sleep(3)
        self.driver.find_element_by_xpath(locators.stage_xpath).click()
        time.sleep(3)
        print("before stage value")
        self.driver.find_element_by_xpath(locators.stage_xpath_value).click()
        print("after stage value")
        time.sleep(3)
        self.driver.find_element_by_xpath(locators.Module_weight_save_xpath).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(locators.SMPT_publish_xpath).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(locators.SMPT_publish_yes_xpath).click()

    # @classmethod
    # def tearDownClass(cls):
    #     print("inside teardownclass")
    #     cls.driver.close()
    #     print("NDPd Login test has been completed")


if __name__ == "__main__":
    unittest.main()
    # unittest.main(
    #     testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/pavv/PycharmProjects/first_project/Reports"))
