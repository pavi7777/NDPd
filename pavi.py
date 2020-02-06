from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome("C:/Users/pavv/Desktop/exe_files/chromedriver.exe")
driver.get('https://nokiatest.siteforge.com/jsp/login.jsp#/login')
driver.maximize_window()
driver.find_element_by_id("j_username_onscreen").send_keys("pba_u")
driver.find_element_by_id("j_password_onscreen").send_keys("Nokia_123")
driver.find_element_by_id("Login_button").click()
driver.implicitly_wait(15)
#menu window
driver.find_element_by_xpath("/html/body/div[2]/div[2]/md-toolbar[1]/md-menu[1]/button").click()
driver.implicitly_wait(15)
driver.find_element_by_xpath(".//*[contains(@title, 'Modules')]").click()
# driver.find_element_by_xpath("(//a)[7]").click()
driver.implicitly_wait(25)
# driver.find_element_by_xpath("(//button)[28]").click()

# for 3 dot menu for actions
driver.find_element_by_xpath(
    "/html/body/div[2]/div[2]/md-content/md-content/md-table-container/div/div/div[2]/div[2]/div/div[1]/div/div[4]/div[2]/div/div[1]/div/md-menu/button/md-icon").click()
driver.implicitly_wait(15)

# for create ticket from 3 dot action menu
driver.find_element_by_xpath("/html/body/div[6]/md-menu-content/ticket-dir-common/md-menu-item/button/span").click()
driver.implicitly_wait(15)
# driver.find_element_by_xpath(".//*[contains(@name, 'ticketCategory')]")
# driver.find_element_by_xpath("(//div)[1081]")
# driver.find_element_by_xpath("/html/body/div[6]/md-menu-content/md-menu-item[4]/button").click()

###########################Handling dropdown
# s1 = Select(driver.find_element_by_xpath(".//*[contains(@aria-label, 'Select Ticket Category')]").click())
# driver.implicitly_wait(15)
# s1.select_by_visible_text("E00 Integration")
# driver.find_element_by_xpath("/html/body/div[8]/md-select-menu/md-content/md-option[1]/div").submit()

driver.find_element_by_xpath(".//*[contains(@aria-label, 'Select Ticket Category')]").click()
driver.implicitly_wait(40)
driver.find_element_by_id("select_option_296").click()
# driver.find_element_by_xpath(".//*[contains(@id,'select_option_614')]").click()
driver.implicitly_wait(40)

driver.find_element_by_xpath(".//*[contains(@aria-label, 'Select Ticket Sub Category')]").click()
# driver.find_element_by_id("select_360").click()
driver.implicitly_wait(40)
# driver.find_element_by_xpath(".//*[contains(@id,'select_option_634')]").click()
driver.find_element_by_id("select_option_307").click()

# for submit button
driver.find_element_by_xpath("/html/body/div[7]/md-dialog/form/md-dialog-content/div/div[2]/button[2]").click()

driver.find_element_by_id("name").send_keys("demo_ticket")
driver.implicitly_wait(20)
driver.find_element_by_xpath(".//*[contains(@ng-model, 'ticket.description')]").send_keys("demo")

# severity
driver.find_element_by_xpath(".//*[contains(@ng-model, 'ticket.severity')]").click()
driver.implicitly_wait(40)
driver.find_element_by_xpath(".//*[contains(@value, 'BA Creatical')]").click()

# for priority (drop down)
driver.find_element_by_xpath(".//*[contains(@ng-model, 'ticket.priority')]").click()
driver.implicitly_wait(40)
driver.find_element_by_xpath(".//*[contains(@value, 'High priority')]").click()

# submit ticket
driver.find_element_by_xpath(".//*[contains(@id, 'submitticket')]").click()

# delete ticket in module
# for 3 dot menu for actions
# driver.find_element_by_xpath("/html/body/div[2]/div[2]/md-content/md-content/md-table-container/div/div/div[2]/div[2]/div/div[1]/div/div[4]/div[2]/div/div[1]/div/md-menu/button/md-icon").click()
# driver.implicitly_wait(15)

# for create ticket from 3 dot action menu
# driver.find_element_by_xpath(".//*[contains(@ng-click, 'openProjectDeleteWindow(125907)')]").click()
# driver.find_element_by_xpath("/html/body/div[7]/md-dialog/md-dialog-actions/button[2]").click()



