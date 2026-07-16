from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class createuser_class:
    username_xpath="//input[@id='username']"
    password_xpath="//input[@id='password']"
    email_xpath="//input[@id='email']"
    phone_xpath="//input[@id='phone']"
    click_crete_user_btn_xpath="//button[@id='createUserButton']"
    successMessage="successMessage"
    singup_button="//a[@id='signUpLink']"

    def __init__(self,driver):
        self.driver=driver

    def enter_username(self,username):
        username_1=self.driver.find_element(By.XPATH,self.username_xpath)
        username_1.send_keys(username)

    def enter_password(self, password):
        password_1 = self.driver.find_element(By.XPATH, self.password_xpath)
        password_1.send_keys(password)

    def enter_email(self,email):
        email_1=self.driver.find_element(By.XPATH,self.email_xpath)
        email_1.send_keys(email)

    def enter_phone(self,phone):
        phone_1=self.driver.find_element(By.XPATH,self.phone_xpath)
        phone_1.send_keys(phone)

    def click_crete_user(self):
        button=self.driver.find_element(By.XPATH,self.click_crete_user_btn_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();",button)
        button.click()

    def message_for_print(self):
        try:
            # message = self.driver.find_element(By.ID, self.successMessage)
            message=WebDriverWait(self.driver,15).until(expected_conditions.visibility_of_element_located((By.ID,self.successMessage)))
            return message.text

        except:
            return "User not create fail"

    def click_singupbutton(self):
        try:
            singup_button=WebDriverWait(self.driver,15).until(expected_conditions.visibility_of_element_located((By.XPATH,self.singup_button)))

            # singup_button = self.driver.find_element(By.XPATH, self.singup_button)
            # self.driver.execute_script("arguments[0].scrollIntoView();", singup_button)
            singup_button.click()
        except:
            return "Failed test case"

