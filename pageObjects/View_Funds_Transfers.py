from selenium.webdriver.common.by import By

from utilites.Excel_ulitiies import Excel_Ulitiles_class


class View_funds_tranfers_class:
    file_path=".\\TestData\\Bank_of_america_all_accounts.xlsx"
    file_path_2 = ".\\TestData\\ViewFundsTransfers.xlsx"
    sheetname="Sheet1"
    username_id="username"
    password_id="password"
    loginButton_id="loginButton"
    FundsTransferManagement_xpath="//a[normalize-space()='Funds Transfer Management']"
    viewallaccount_xpath="//a[normalize-space()='View All Fund Transfers']"
    max_len="//tbody/tr"
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


    def click_accountmangement_button(self):
        self.driver.find_element(By.XPATH,self.FundsTransferManagement_xpath).click()

    def click_viewallaccount_button(self):
        self.driver.find_element(By.XPATH,self.viewallaccount_xpath).click()

    def table_data_insert(self):
        max_row=self.driver.find_elements(By.XPATH, self.max_len)
        for i in range(1, len(max_row)+1):
            TransferID=self.driver.find_element(By.XPATH,f"//tbody/tr[{i}]/td[1]").text
            FromAccountID=self.driver.find_element(By.XPATH,f"//tbody/tr[{i}]/td[2]").text

            ToAccountID=self.driver.find_element(By.XPATH,f"//tbody/tr[{i}]/td[3]").text
            TransferDate=self.driver.find_element(By.XPATH,f"//tbody/tr[{i}]/td[4]").text
            Description=self.driver.find_element(By.XPATH,f"//tbody/tr[{i}]/td[5]").text




            Excel_Ulitiles_class.write_date_to_excel(self.file_path_2,self.sheetname,i,2,TransferID)
            Excel_Ulitiles_class.write_date_to_excel(self.file_path_2,self.sheetname,i,3,FromAccountID)
            Excel_Ulitiles_class.write_date_to_excel(self.file_path_2,self.sheetname,i,4,ToAccountID)
            Excel_Ulitiles_class.write_date_to_excel(self.file_path_2,self.sheetname,i,5,TransferDate)
            Excel_Ulitiles_class.write_date_to_excel(self.file_path_2,self.sheetname,i,6,Description)

            self.j+=1
            button=self.driver.find_element(By.XPATH, f"//a[normalize-space()='{str(self.j)}']")
            self.driver.execute_script("arguments[0].scrollIntoView();",button)
            button.click()
            if str(self.j)=="6":
                break
            else:
                pass










