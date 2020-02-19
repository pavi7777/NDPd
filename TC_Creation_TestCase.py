import time
import unittest
from selenium import webdriver
from Properties import Locators


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
        self.driver.get(Locators.site_url)
        self.driver.find_element_by_id(Locators.login_id).send_keys(Locators.pba_login)
        self.driver.find_element_by_id(Locators.pwd_id).send_keys(Locators.NDPd_pwd)
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id(Locators.login_button_id).click()
        time.sleep(5)

    def test_B_NDPd_Menu_TC(self):
        print("inside the Menu")
        self.driver.find_element_by_xpath(Locators.window_xpath).click()
        self.driver.implicitly_wait(10)

        # To select Testcase from Menu window
        flag = self.driver.find_element_by_xpath(Locators.TC_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", flag)
        self.driver.implicitly_wait(30)
        flag.click()

        self.driver.find_element_by_xpath(Locators.plus_button_xpath).click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath(Locators.TC_name_xpath).send_keys("Demo_automation")
        self.driver.implicitly_wait(20)

        # Type(dropdown)
        self.driver.find_element_by_xpath(Locators.TC_Type_xpath).click()
        self.driver.implicitly_wait(40)
        self.driver.find_element_by_xpath(Locators.TC_Type_xpath_value).click()
        self.driver.implicitly_wait(20)

        # Field Type(dropdown)
        self.driver.implicitly_wait(15)
        self.driver.find_element_by_xpath(Locators.TC_Field_Type_xpath).click()
        self.driver.find_element_by_xpath(Locators.TC_Field_Type_xpath_value).click()
        self.driver.implicitly_wait(15)
        self.driver.find_element_by_xpath(Locators.TC_submit_xpath).click()

    @classmethod
    def tearDownClass(cls):
        print("inside teardownclass")
        cls.driver.close()
        print("NDPd Login test has been completed")


if __name__ == "__main__":
    unittest.main()
