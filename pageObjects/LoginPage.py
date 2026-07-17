from selenium.webdriver.common.by import By


class Loginpage:
    username_id="username"
    password_id="password"
    loginButton_id="loginButton"
    logout_xpath="//a[normalize-space()='Logout']"


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



