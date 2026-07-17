import time

import pytest
from faker import Faker

from pageObjects.LoginPage import Loginpage
from pageObjects.SingUpPage import createuser_class
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
















