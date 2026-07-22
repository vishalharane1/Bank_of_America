from selenium.webdriver.common.by import By

from utilites.Excel_ulitiies import Excel_Ulitiles_class


class TransactionHistory_class:
    file_path=".\\TestData\\TransactionHistory_accountid_1.xlsx"

    sheetname="Sheet1"
    username_id="username"
    password_id="password"
    loginButton_id="loginButton"
    TransactionHistory_xpath="//a[normalize-space()='Transaction History']"
    accountId="accountId"
    submit="//button[@type='submit']"
    max_len = "//tbody/tr"
    j = 1





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


    def click_TransactionHistory_button(self):
        self.driver.find_element(By.XPATH,self.TransactionHistory_xpath).click()

    def enter_accountId(self,accountId):
        self.driver.find_element(By.ID,self.accountId).send_keys(accountId)

    def submit_button(self):
        button=self.driver.find_element(By.XPATH,self.submit)
        self.driver.execute_script("arguments[0].scrollIntoView();",button)
        button.click()



    def table_data_insert(self):

        max_row=self.driver.find_elements(By.XPATH, self.max_len)
        for i in range(2, len(max_row)+1):
            TransactionID=self.driver.find_element(By.XPATH,f"//tbody/tr[{i}]/td[1]").text
            AccountID=self.driver.find_element(By.XPATH,f"//tbody/tr[{i}]/td[2]").text

            Type=self.driver.find_element(By.XPATH,f"//tbody/tr[{i}]/td[3]").text
            Amount=self.driver.find_element(By.XPATH,f"//tbody/tr[{i}]/td[4]").text
            Date=self.driver.find_element(By.XPATH,f"//tbody/tr[{i}]/td[5]").text
            Description=self.driver.find_element(By.XPATH,f"//tbody/tr[{i}]/td[6]").text



            Excel_Ulitiles_class.write_date_to_excel(self.file_path,self.sheetname,i,1,i)
            Excel_Ulitiles_class.write_date_to_excel(self.file_path,self.sheetname,i,2,TransactionID)
            Excel_Ulitiles_class.write_date_to_excel(self.file_path,self.sheetname,i,3,AccountID)
            Excel_Ulitiles_class.write_date_to_excel(self.file_path,self.sheetname,i,4,Type)
            Excel_Ulitiles_class.write_date_to_excel(self.file_path,self.sheetname,i,5,Amount)
            Excel_Ulitiles_class.write_date_to_excel(self.file_path,self.sheetname,i,6,Date)
            Excel_Ulitiles_class.write_date_to_excel(self.file_path,self.sheetname,i,7,Description)








