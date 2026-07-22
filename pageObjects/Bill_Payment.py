from selenium.webdriver.common.by import By

from utilites.Excel_ulitiies import Excel_Ulitiles_class


class Bill_Payment_class:
    file_path=".\\TestData\\Bank_of_america_all_accounts.xlsx"
    file_path_2 = ".\\TestData\\ViewFundsTransfers.xlsx"
    sheetname="Sheet1"
    username_id="username"
    password_id="password"
    loginButton_id="loginButton"
    BillPayments_xpath="//a[normalize-space()='Bill Payments']"
    accountId="accountId"
    payeeName="payeeName"
    amount="amount"
    description="description"
    pay_button="//button[@type='submit']"
    validation_xpath="//div[@class='success-message']"




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


    def click_BillPayments_button(self):
        self.driver.find_element(By.XPATH,self.BillPayments_xpath).click()

    def enter_accountId(self,accountId):
        self.driver.find_element(By.ID,self.accountId).send_keys(accountId)

    def enter_payeeName(self,payeeName):
        self.driver.find_element(By.ID,self.payeeName).send_keys(payeeName)

    def enter_amount(self,amount):
        self.driver.find_element(By.ID,self.amount).send_keys(amount)

    def enter_description(self,description):
        self.driver.find_element(By.ID,self.description).send_keys(description)

    def click_pay_button(self):
        self.driver.find_element(By.XPATH,self.pay_button).click()


    def validation_text(self):
       return self.driver.find_element(By.XPATH,self.validation_xpath).text

