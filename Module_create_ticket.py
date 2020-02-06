import time
import unittest

from selenium import webdriver

from locators import locators


class NDPdLoginTest(unittest.TestCase):

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
        self.driver.find_element_by_id(locators.login_id).send_keys(locators.pba_login)
        self.driver.find_element_by_id(locators.pwd_id).send_keys(locators.NDPd_pwd)
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id(locators.login_button_id).click()
        time.sleep(5)

    def test_B_NDPd_Menu(self):
        print("inside the Menu")
        self.driver.find_element_by_xpath(locators.window_xpath).click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath(locators.Module_xpath).click()
        # 3 dot action menu
        self.driver.find_element_by_xpath(locators.menu_xpath).click()
        self.driver.find_element_by_xpath(locators.create_ticket).click()
        self.driver.find_element_by_xpath(locators.ticket_category_xpath).click()
        self.driver.find_element_by_id(locators.ticket_id).click()
        self.driver.find_element_by_xpath(locators.ticket_sub_category_xpath).click()
        self.driver.find_element_by_id(locators.sub_ticket_id).click()

        # submit
        self.driver.find_element_by_xpath(locators.submit_xpath).click()
        self.driver.implicitly_wait(10)
        # create ticket
        # self.driver.find_element_by_xpath(locators.ticket_name_xpath).click()
        # self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath(locators.ticket_name_xpath).send_keys(locators.ticket_name_xpath_value)
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath(locators.ticket_description_xpath).send_keys(locators.ticket_description_xpath_value)
        self.driver.implicitly_wait(10)
        # dropdown severity
        self.driver.find_element_by_xpath(locators.ticket_severity_xpath).click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath(locators.ticket_severity_value_xpath).click()
        self.driver.implicitly_wait(10)
        # dropdown priority
        self.driver.find_element_by_xpath(locators.ticket_priority_xpath).click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath(locators.ticket_priority_value_xpath).click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath(locators.submit_ticket_xpath).click()

    @classmethod
    def tearDownClass(cls):
        print("inside teardownclass")
        cls.driver.close()
        print("NDPd Login test has been completed")


if __name__ == "__main__":
    unittest.main()
    # unittest.main(
    #     testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/pavv/PycharmProjects/first_project/Reports"))
