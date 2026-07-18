from selenium.webdriver.common.by import By


class Customer_Management:
    username_id="username"
    password_id="password"
    loginButton_id="loginButton"
    logout_xpath="//a[normalize-space()='Logout']"
    Customer_Management_xpath = "//a[normalize-space()='Customer Management']"
    Create_Customer_xpath="//a[normalize-space()='Create Customer']"
    userid_id="userId"
    firstName_id="firstName"
    lastName_id="lastName"
    dateOfBirth_id="dateOfBirth"
    address_id="address"
    city_id="city"
    state_id="state"
    zipCode_id="zipCode"
    createCustomerBtn_id="//button[@id='createCustomerBtn']"


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

    def enter_userid(self, userid):
        userid_var = self.driver.find_element(By.ID, self.userid_id)
        userid_var.send_keys(userid)

    def enter_firstName(self,firstName):
        firstName_var=self.driver.find_element(By.ID,self.firstName_id)
        firstName_var.send_keys(firstName)


    def enter_lastName(self,lastName):
        lastName_var=self.driver.find_element(By.ID,self.lastName_id)
        lastName_var.send_keys(lastName)

    def enter_dateOfBirth(self,dateOfBirth):
        dateOfBirth_var=self.driver.find_element(By.ID,self.dateOfBirth_id)
        dateOfBirth_var.send_keys(dateOfBirth)

    def enter_address(self, address):
        address_var = self.driver.find_element(By.ID, self.address_id)
        address_var.send_keys(address)

    def enter_city(self,city):
        city_var=self.driver.find_element(By.ID,self.city_id)
        city_var.send_keys(city)

    def enter_state(self,state):
        state_var=self.driver.find_element(By.ID,self.state_id)
        state_var.send_keys(state)

    def enter_zipCode(self,zipCode):
        zipCode_var=self.driver.find_element(By.ID,self.zipCode_id)
        zipCode_var.send_keys(zipCode)

    def click_createCustomerBtn(self):
        createCustomerBtn_var = self.driver.find_element(By.XPATH, self.createCustomerBtn_id)
        self.driver.execute_script("arguments[0].scrollIntoView();", createCustomerBtn_var)

        createCustomerBtn_var.click()
