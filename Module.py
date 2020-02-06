from selenium import webdriver

driver = webdriver.Chrome("C:/Users/pavv/Desktop/exe_files/chromedriver.exe")
driver.get('http://nokiatest.siteforge.com/jsp/login.jsp#/login')
driver.maximize_window()
driver.find_element_by_id("j_username_onscreen").send_keys("pba_u")
driver.find_element_by_id("j_password_onscreen").send_keys("Nokia_123")
driver.find_element_by_id("Login_button").click()
driver.implicitly_wait(15)
# menu window
driver.find_element_by_xpath("/html/body/div[2]/div[2]/md-toolbar[1]/md-menu[1]/button").click()
driver.implicitly_wait(15)

# flag = driver.find_element_by_xpath(".//*[contains(@title, 'Testcases')]").click()
# driver.implicitly_wait(15)

element = driver.find_element_by_xpath(".//*[contains(@title, 'Testcases')]").click()
driver.implicitly_wait(15)

driver.find_element_by_xpath("(//button)[20]").click()
driver.implicitly_wait(20)
driver.find_element_by_xpath(".//*[contains(@id, 'input_106')]").send_keys("Demo")
driver.implicitly_wait(20)

#Type(dropdown)
driver.find_element_by_xpath("//*[contains(@role, 'combobox')]").click()
driver.implicitly_wait(40)
driver.find_element_by_xpath("/html/body/md-virtual-repeat-container/div/div[2]/ul/li[3]").click()
driver.implicitly_wait(20)

#Field Type(dropdown)
driver.implicitly_wait(15)
driver.find_element_by_id("select_option_124").click()
driver.find_element_by_id("select_108").click()
driver.implicitly_wait(15)
driver.find_element_by_xpath("(//button)[46]").click()
