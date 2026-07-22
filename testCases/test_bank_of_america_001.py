import time

import pytest
from faker import Faker

from pageObjects.Account_Management import Account_management_class
from pageObjects.Bill_Payment import Bill_Payment_class
from pageObjects.CustomerSupport import CustomerSupport_class
from pageObjects.Customer_Management import Customer_Management
from pageObjects.LoginPage import Loginpage
from pageObjects.SingUpPage import createuser_class
from pageObjects.Transaction_History import TransactionHistory_class
from pageObjects.View_Funds_Transfers import View_funds_tranfers_class
from utilites.Excel_ulitiies import Excel_Ulitiles_class
from utilites.Logger import Log_genarator_class
from utilites.Readconfig import Read_config_class


@pytest.mark.usefixtures("browser_setup")
class Test_BankApplication:
    driver=None
    log=Log_genarator_class.loggon_method()

    bank_url=Read_config_class.get_bankapp_url()
    usersingup_url=Read_config_class.get_usersingup_url()
    login_url=Read_config_class.get_loginpage_url()
    excel_path=r"C:\Users\visha\Desktop\PyProject\Bank_Application_Bank_of_America\TestData\Faker_Data.xlsx"
    sheetname="Sheet1"
    filepath_ddt=r"C:\Users\visha\Desktop\PyProject\Bank_Application_Bank_of_America\TestData\TestData_For_DDT.xlsx"
    file_path_create_user=r"C:\Users\visha\Desktop\PyProject\Bank_Application_Bank_of_America\TestData\Pune_Users_Test_Data.xlsx"
    sheetname_create_user="Pune Users"
    def test_VerifyURLAndTitle_001(self):
        self.log.info("-----Start VerifyURLAndTitle Test Case 1------")
        self.driver.get(self.bank_url)
        self.log.info(f"URL---->{self.bank_url}")
        self.log.info(f"TITLE---->{self.driver.title}")
        assert self.driver.title=="Bank Application"

    def test_Singup_or_createuser_002(self):
        max_row=Excel_Ulitiles_class.get_max_row_from_excel(self.excel_path,self.sheetname)
        self.log.info(f"-----max row--->{max_row}------")
        self.log.info("-----Start VerifyURLAndTitle Test Case 1------")
        for i in range(2,max_row+1):
            fake = Faker("en_IN")
            self.username = fake.user_name()
            Excel_Ulitiles_class.write_date_to_excel(self.excel_path,self.sheetname,i,2,self.username)
            self.password = fake.password(length=10,
            special_chars=True,
            digits=True,
            upper_case=True,
            lower_case=True)
            #Excel_Ulitiles_class.write_date_to_excel(self.excel_path, self.sheetname, i + 1, 3, self.password)
            Excel_Ulitiles_class.write_date_to_excel(self.excel_path, self.sheetname, i , 3, "QaTest#2026")

            self.email = fake.email()
            Excel_Ulitiles_class.write_date_to_excel(self.excel_path, self.sheetname, i , 4, self.email)
            self.phone = fake.phone_number()
            Excel_Ulitiles_class.write_date_to_excel(self.excel_path, self.sheetname, i , 5, self.phone)
            self.log.info("-----Start test_Singup_or_createuser_002 Test Case 2------")
            self.log.info(f"URL---->{self.usersingup_url}")
            self.driver.get(self.usersingup_url)
            self.singup_obj = createuser_class(self.driver)
            self.singup_obj.enter_username(self.username)
            self.log.info(f"username---->{self.username}")
            #self.singup_obj.enter_password(self.password)
            self.singup_obj.enter_password("P@ssw0rd123")
            self.log.info(f"password---->P@ssw0rd123")
            self.singup_obj.enter_email(self.email)
            self.log.info(f"email---->{self.email}")
            self.singup_obj.enter_phone(self.phone)
            self.log.info(f"phone---->{self.phone}")

            self.singup_obj.click_crete_user()
            actual_result=self.singup_obj.message_for_print()
            Excel_Ulitiles_class.write_date_to_excel(self.excel_path, self.sheetname, i , 6, actual_result)
            expected_result=Excel_Ulitiles_class.read_data_from_excel(self.excel_path, self.sheetname, i,7)
            if expected_result==actual_result:
                Excel_Ulitiles_class.write_date_to_excel(self.excel_path, self.sheetname, i, 8, "Pass")
            else:
                Excel_Ulitiles_class.write_date_to_excel(self.excel_path, self.sheetname, i, 8, "Fail")

            self.singup_obj.click_singupbutton()
    print("-----Test cases Ended  test_Singup_or_createuser_002 -------")

    def test_loginpage_ddt_003(self):
        max_row=Excel_Ulitiles_class.get_max_row_from_excel(self.filepath_ddt,sheetname=self.sheetname)
        self.log.info(f"-----max row--->{max_row}------")
        self.log.info("-----Start loginpage_ddt Test Case 1------")
        for i in range(2,max_row+1):
            username=Excel_Ulitiles_class.read_data_from_excel(self.filepath_ddt,self.sheetname,i,2)
            password=Excel_Ulitiles_class.read_data_from_excel(self.filepath_ddt,self.sheetname,i,3)
            expected_result=Excel_Ulitiles_class.read_data_from_excel(self.filepath_ddt,self.sheetname,i,4)
            self.driver.get(self.login_url)
            self.log.info(f"URL---->{self.login_url}")
            self.login=Loginpage(self.driver)
            self.login.enter_username(username)
            self.login.enter_password(password)
            self.login.click_login_button()
            self.log.info(f"bank_app_login_page Title-->{self.driver.title}")
            try:
                assert self.driver.title=="Dashboard"
                Excel_Ulitiles_class.write_date_to_excel(self.filepath_ddt, self.sheetname, i, 5, "Pass")
                self.login.click_logout_button()

            except:
                Excel_Ulitiles_class.write_date_to_excel(self.filepath_ddt,self.sheetname,i,5,"Fail")
            actual_result=Excel_Ulitiles_class.read_data_from_excel(self.filepath_ddt,self.sheetname,i,5)
            if actual_result==expected_result:
                Excel_Ulitiles_class.write_date_to_excel(self.filepath_ddt,self.sheetname,i,6,"Test cases Pass")
            else:
                Excel_Ulitiles_class.write_date_to_excel(self.filepath_ddt,self.sheetname,i,6,"Test cases Fail")


    def test_customer_management_004(self):
        self.log.info(f"------Starting  customer_management 004 test case------------")
        username=Excel_Ulitiles_class.read_data_from_excel(self.filepath_ddt,self.sheetname,2,2)
        password = Excel_Ulitiles_class.read_data_from_excel(self.filepath_ddt, self.sheetname, 2, 3)
        self.driver.get(self.login_url)
        self.log.info(f"URL---->{self.login_url}")
        self.customer_management = Customer_Management(self.driver)
        self.log.info(f"username-->{username}")
        self.customer_management.enter_username(username)
        self.log.info(f"password-->{password}")
        self.customer_management.enter_password(password)
        self.customer_management.click_login_button()
        self.log.info(f"bank_app_login_page Title-->{self.driver.title}")
        self.customer_management.click_Customer_Management()
        self.log.info(f"bank_app_login_page Title-->{self.driver.title}")
        assert self.driver.title=="Customer Management"
        self.customer_management.click_Create_Customer()
        self.log.info(f"bank_app_login_page Title-->{self.driver.title}")
        assert self.driver.title == "Create Customer"
        max_row=Excel_Ulitiles_class.get_max_row_from_excel(self.file_path_create_user,self.sheetname_create_user)
        self.log.info(f"max rows--->{max_row}")
        for i in range(2,max_row+1):
            userid=Excel_Ulitiles_class.read_data_from_excel(self.file_path_create_user,self.sheetname_create_user,i,1)
            firstname=Excel_Ulitiles_class.read_data_from_excel(self.file_path_create_user,self.sheetname_create_user,i,2)
            lastName=Excel_Ulitiles_class.read_data_from_excel(self.file_path_create_user,self.sheetname_create_user,i,3)
            dateOfBirth=Excel_Ulitiles_class.read_data_from_excel(self.file_path_create_user,self.sheetname_create_user,i,4)
            address=Excel_Ulitiles_class.read_data_from_excel(self.file_path_create_user,self.sheetname_create_user,i,5)
            city=Excel_Ulitiles_class.read_data_from_excel(self.file_path_create_user,self.sheetname_create_user,i,6)
            state=Excel_Ulitiles_class.read_data_from_excel(self.file_path_create_user,self.sheetname_create_user,i,7)
            zipCode=Excel_Ulitiles_class.read_data_from_excel(self.file_path_create_user,self.sheetname_create_user,i,8)
            self.customer_management.enter_userid(userid)
            self.customer_management.enter_firstName(firstname)
            self.customer_management.enter_lastName(lastName)
            self.customer_management.enter_dateOfBirth(dateOfBirth)
            self.customer_management.enter_address(address)
            self.customer_management.enter_city(city)
            self.customer_management.enter_state(state)
            self.customer_management.enter_zipCode(zipCode)
            self.customer_management.click_createCustomerBtn()
            self.customer_management.click_Create_Customer()

    def test_account_mangement_005(self):
        self.log.info(f"\n------Starting  account_mangement 005 test case------------")
        username=Read_config_class.get_username()
        password=Read_config_class.get_password()
        self.driver.get(self.login_url)
        self.log.info(f"URL---->{self.login_url}")
        self.account_obj=Account_management_class(self.driver)
        self.account_obj.enter_username(username)
        self.account_obj.enter_password(password)
        self.account_obj.click_login_button()
        self.account_obj.click_accountmangement_button()
        self.account_obj.click_viewallaccount_button()
        self.account_obj.table_data_insert()

    def test_view_fund_transfers_006(self):
        self.log.info(f"\n------Starting  test_view_fund_transfers test case------------")
        username = Read_config_class.get_username()
        password = Read_config_class.get_password()
        self.driver.get(self.login_url)
        self.log.info(f"URL---->{self.login_url}")
        self.v_f_t = View_funds_tranfers_class(self.driver)
        self.v_f_t.enter_username(username)
        self.v_f_t.enter_password(password)
        self.v_f_t.click_login_button()
        self.v_f_t.click_accountmangement_button()
        self.v_f_t.click_viewallaccount_button()
        self.v_f_t.table_data_insert()

    def test_bill_payment_007(self):
        self.log.info(f"\n------Starting  test_view_fund_transfers test case------------")
        username = Read_config_class.get_username()
        password = Read_config_class.get_password()
        self.driver.get(self.login_url)
        self.log.info(f"URL---->{self.login_url}")
        self.billp = Bill_Payment_class(self.driver)
        self.billp.enter_username(username)
        self.billp.enter_password(password)
        self.billp.click_login_button()
        self.billp.click_BillPayments_button()
        self.billp.enter_accountId(1)
        self.billp.enter_payeeName("Sachin mahrtr")
        self.billp.enter_amount(3000)
        self.billp.enter_description("Electricity bill")
        self.billp.click_pay_button()
        self.log.info(f"\n------{self.billp.validation_text()}------------")
        assert self.billp.validation_text()=="Bill payment created successfully"

    def test_transaction_history_008(self):
        self.log.info(f"\n------Starting  test_transaction_history_008 test case------------")
        username = Read_config_class.get_username()
        password = Read_config_class.get_password()
        self.driver.get(self.login_url)
        self.log.info(f"URL---->{self.login_url}")
        self.log.info(f"TITLE---->{self.driver.title}")

        self.billp = TransactionHistory_class(self.driver)
        self.transaction = TransactionHistory_class(self.driver)
        self.transaction.enter_username(username)
        self.transaction.enter_password(password)
        self.transaction.click_login_button()
        self.log.info(f"TITLE---->{self.driver.title}")
        assert self.driver.title in [ "Dashboard",'Login']
        self.transaction.click_TransactionHistory_button()
        assert self.driver.title == "Transaction History"
        self.transaction.enter_accountId(1)
        self.transaction.submit_button()
        self.transaction.table_data_insert()

    def test_customer_support_009(self):
        self.log.info(f"\n------Starting  test_transaction_history_008 test case------------")
        username = Read_config_class.get_username()
        password = Read_config_class.get_password()
        self.driver.get(self.login_url)
        self.log.info(f"URL---->{self.login_url}")
        self.log.info(f"TITLE---->{self.driver.title}")
        self.CustomerSupport = CustomerSupport_class(self.driver)
        self.CustomerSupport.enter_username(username)
        self.CustomerSupport.enter_password(password)
        self.CustomerSupport.click_login_button()
        self.log.info(f"TITLE---->{self.driver.title}")
        assert self.driver.title in [ "Dashboard",'Login']
        self.CustomerSupport.click_Customer_support()
        assert self.driver.title=="Customer Support"
        for i in range(1,6):
            fake=Faker()
            name=fake.name()
            email=fake.email()
            phone_no = fake.numerify("##########")
            issue = fake.random_element(elements=[
                "Unable to login to my account",
                "Payment transaction failed",
                "Unable to reset my password",
                "Customer account is not accessible",
                "Website is loading very slowly"
            ])
            self.CustomerSupport.enter_name(name)
            self.CustomerSupport.enter_email(email)
            self.CustomerSupport.enter_phone(phone_no)
            self.CustomerSupport.enter_issue(issue)
            self.CustomerSupport.click_sumit()
            assert self.CustomerSupport.validation_text()=="Support request submitted successfully!"
        self.CustomerSupport.click_logout_button()




























