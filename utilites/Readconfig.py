import configparser


config=configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class Read_config_class:

    @staticmethod
    def get_bankapp_url():
        return config.get("URL","bank_url")
