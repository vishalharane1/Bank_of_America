from selenium.webdriver.common.by import By


class CustomerSupport_class:
    username_id="username"
    password_id="password"
    loginButton_id="loginButton"
    logout_xpath="a[href='/logout']"
    Customer_support_xpath = "//a[normalize-space()='Customer Support']"
    name="name"
    email="email"
    phone="phone"
    issue="issue"
    submit_xpath="//button[@type='submit']"


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




    def click_Customer_support(self):
        button_Customer_Management = self.driver.find_element(By.XPATH, self.Customer_support_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", button_Customer_Management)
        button_Customer_Management.click()

    def enter_name(self,name):
        username_var=self.driver.find_element(By.ID,self.name)
        self.driver.execute_script("arguments[0].scrollIntoView();", username_var)

        username_var.send_keys(name)

    def enter_email(self,email):
        password_var=self.driver.find_element(By.ID,self.email)
        self.driver.execute_script("arguments[0].scrollIntoView();", password_var)

        password_var.send_keys(email)

    def enter_phone(self,phone):
        phone_1=self.driver.find_element(By.ID,self.phone)
        self.driver.execute_script("arguments[0].scrollIntoView();", phone_1)
        phone_1.send_keys(phone)

    def enter_issue(self,issue):
        password_var=self.driver.find_element(By.ID,self.issue)
        self.driver.execute_script("arguments[0].scrollIntoView();", password_var)

        password_var.send_keys(issue)

    def click_sumit(self):
        button_submit= self.driver.find_element(By.XPATH, self.submit_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", button_submit)
        button_submit.click()





    def validation_text(self):
        return self.driver.find_element(By.XPATH,"//div[@class='success-message']").text

    def click_logout_button(self):
        logout=self.driver.find_element(By.CSS_SELECTOR,self.logout_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", logout)
        logout.click()



