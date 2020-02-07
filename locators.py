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


    # locators with respect to Testcase creation in Testcase Tab

    #Handling scrollbar to select TC
    TC_xpath = ".//*[contains(@title, 'Testcases')]"
    plus_button_xpath = "(//button)[20]"
    TC_name_xpath = ".//*[contains(@ng-model, 'ctrl.testcase')]"
    TC_Type_xpath = "//*[contains(@role, 'combobox')]"
    TC_Type_xpath_value = "/html/body/md-virtual-repeat-container/div/div[2]/ul/li[3]"
    TC_Field_Type_xpath = ".//*[contains(@ng-model, 'ctrl.filedTypeModel')]"
    TC_Field_Type_xpath_value = ".//*[contains(@value, 'TEXT_AREA')]"
    TC_submit_xpath = "//*[contains(@type, 'submit()')]"

    # Handling scroll bar to select SMPT
    SMPT_xpath = ".//*[contains(@title, 'SMP Templates')]"
    SMPT_plus_button_xpath = "(//button)[21]"
    SMP_name_xpath = ".//*[contains(@name, 'name')]"
    SMP_site_type_xpath = ".//*[contains(@name, 'siteType')]"
    SMP_site_type_xpath_value = "(.//*[contains(@value, 'Radio')])[2]"
    #handling check box
    SMPT_Select_Module_Template_xpath = ".//*[contains(@aria-label, 'Module Template(s)')]"
    # SMPT_Module_Template_xpath = ".//*[contains(@placeholder, 'Search Module Template')]"
    SMPT_Module_Template_xpath = ".//*[contains(@value, '2318')]"
    Click_on_full_window_xpath = "//md-backdrop"

    SMPT_portfolio_xpath = ".//*[contains(@aria-label, 'Portfolio')]"
    SMPT_portfolio_xpath_value = "/html/body/div[7]/md-select-menu/md-content/md-option[2]/div"
    #SMPT_portfolio_xpath_value = ".//*[contains(@id, 'select_option_246')]"
    SMPT_save_xpath = "(//button)[19]"
    Module_name_click_xpath = "(.//*[contains(@class, 'ng-binding')])[46]"
    weightage_xpath = ".//*[contains(@name, 'weightage')]"
    stage_xpath = ".//*[contains(@id, 'select_894')]"
    stage_xpath_value = ".//*[contains(@id, 'select_option_919')]"
    Module_weight_save_xpath = "(.//*[contains(@type, 'button')])[23]"
    SMPT_publish_xpath = "(.//*[contains(@type, 'button')])[16]"