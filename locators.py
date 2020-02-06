from selenium import webdriver


class locators:
    # login Details
    login_page_url = "C:/Users/pavv/Desktop/exe_files/chromedriver.exe"
    site_url = "https://nokiatest.siteforge.com/jsp/login.jsp#/login"
    login_id = "j_username_onscreen"
    pwd_id = "j_password_onscreen"
    login_button_id = "Login_button"
    pba_login = "pba_u"
    NDPd_pwd = "Nokia_123"

    # Menu Window
    window_xpath = "/html/body/div[2]/div[2]/md-toolbar[1]/md-menu[1]/button"
    Module_xpath = ".//*[contains(@title, 'Modules')]"

    # for 3 dot menu from actions
    menu_xpath = ".//*[contains(@aria-label, 'Actions')]"
    create_ticket = "/html/body/div[6]/md-menu-content/ticket-dir-common/md-menu-item/button/span"
    # to handle dropdown
    ticket_category_xpath = ".//*[contains(@aria-label, 'Select Ticket Category')]"
    ticket_id = "select_option_296"

    ticket_sub_category_xpath = ".//*[contains(@aria-label, 'Select Ticket Sub Category')]"
    sub_ticket_id = "select_option_307"

    # for submit button in Module
    submit_xpath = "/html/body/div[7]/md-dialog/form/md-dialog-content/div/div[2]/button[2]"


    # creating ticket
    ticket_name_xpath = ".//*[contains(@id, 'name')]"
    ticket_name_xpath_value = "Demo ticket"
    ticket_description_xpath = ".//*[contains(@ng-model, 'ticket.description')]"
    ticket_description_xpath_value = "Demo"

    # drodown severity in ticket creation
    ticket_severity_xpath = ".//*[contains(@ng-model, 'ticket.severity')]"
    ticket_severity_value_xpath = ".//*[contains(@value, 'BA Creatical')]"

    # dropdown Priority in ticket creation
    ticket_priority_xpath = ".//*[contains(@ng-model, 'ticket.priority')]"
    ticket_priority_value_xpath = ".//*[contains(@value, 'High priority')]"

    submit_ticket_xpath = ".//*[contains(@id, 'submitticket')]"
