import configparser


config=configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class Read_config_class:

    @staticmethod
    def get_bankapp_url():
        return config.get("URL","bank_url")

    @staticmethod
    def get_usersingup_url():
        return config.get("URL","usersingup_url")

    @staticmethod
    def get_loginpage_url():
        return config.get("URL","loginpage_url")

    @staticmethod
    def get_username():
        return config.get("login info","username")

    @staticmethod
    def get_password():
        return config.get("login info","password")

