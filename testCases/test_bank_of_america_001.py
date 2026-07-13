import pytest

from utilites.Logger import Log_genarator_class
from utilites.Readconfig import Read_config_class


@pytest.mark.usefixtures("browser_setup")
class Test_BankApplication:
    driver=None
    log=Log_genarator_class.loggon_method()

    bank_url=Read_config_class.get_bankapp_url()

    def test_VerifyURLAndTitle_001(self):
        self.log.info("-----Start VerifyURLAndTitle Test Case 1------")
        self.driver.get(self.bank_url)
        self.log.info(f"URL---->{self.bank_url}")
        self.log.info(f"TITLE---->{self.driver.title}")
        assert self.driver.title=="Bank Application"
