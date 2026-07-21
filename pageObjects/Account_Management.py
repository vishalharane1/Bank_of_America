from selenium.webdriver.common.by import By

from utilites.Excel_ulitiies import Excel_Ulitiles_class


class Account_management_class:
    file_path=".\\TestData\\Bank_of_america_all_accounts.xlsx"
    sheetname="Sheet1"
    username_id="username"
    password_id="password"
    loginButton_id="loginButton"
    accountmangement_xpath="//a[normalize-space()='Account Management']"
    viewallaccount_xpath="//a[normalize-space()='View All Accounts']"
    max_len="//tbody/tr"




    def __init__(self,driver):
        self.driver=driver

    def enter_username(self,username):
        username_var=self.driver.find_element(By.ID,self.username_id)
        username_var.send_keys(username)

    def enter_password(self,password):
        password_var=self.driver.find_element(By.ID,self.password_id)
        password_var.send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.ID,self.loginButton_id).click()


    def click_accountmangement_button(self):
        self.driver.find_element(By.XPATH,self.accountmangement_xpath).click()

    def click_viewallaccount_button(self):
        self.driver.find_element(By.XPATH,self.viewallaccount_xpath).click()

    def table_data_insert(self):
        max_row=self.driver.find_elements(By.XPATH, self.max_len)
        for i in range(1, len(max_row)+1):
            accountid=self.driver.find_element(By.XPATH,f"//tbody/tr[{i}]/td[1]").text
            customerid=self.driver.find_element(By.XPATH,f"//tbody/tr[{i}]/td[2]").text

            accounttype=self.driver.find_element(By.XPATH,f"//tbody/tr[{i}]/td[3]").text

            balance=self.driver.find_element(By.XPATH,f"//tbody/tr[{i}]/td[4]").text
            Excel_Ulitiles_class.write_date_to_excel(self.file_path,self.sheetname,i+1,2,accountid)
            Excel_Ulitiles_class.write_date_to_excel(self.file_path,self.sheetname,i+1,3,customerid)
            Excel_Ulitiles_class.write_date_to_excel(self.file_path,self.sheetname,i+1,4,accounttype)
            Excel_Ulitiles_class.write_date_to_excel(self.file_path,self.sheetname,i+1,5,balance)





