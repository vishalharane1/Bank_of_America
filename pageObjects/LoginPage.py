from selenium.webdriver.common.by import By


class Loginpage:
    username_id="username"
    password_id="password"
    loginButton_id="loginButton"
    logout_xpath="//a[normalize-space()='Logout']"
    Customer_Management_xpath = "//a[normalize-space()='Customer Management']"
    Create_Customer_xpath="//a[normalize-space()='Create Customer']"


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

    def click_logout_button(self):
        self.driver.find_element(By.XPATH,self.logout_xpath).click()

    ####starting customer management#######
    def click_Customer_Management(self):
        button_Customer_Management = self.driver.find_element(By.XPATH, self.Customer_Management_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", button_Customer_Management)
        button_Customer_Management.click()

    def click_Create_Customer(self):
        button_Create_Customer_= self.driver.find_element(By.XPATH, self.Create_Customer_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", button_Create_Customer_)
        button_Create_Customer_.click()



