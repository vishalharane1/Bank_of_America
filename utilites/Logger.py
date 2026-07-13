import logging

class Log_genarator_class:

    @staticmethod
    def loggon_method():
        log_file=logging.FileHandler(".\\Logs\\bank_application.log")
        log_formate=logging.Formatter("%(asctime)s : %(levelname)s : %(funcName)s : %(lineno)d : %(message)s")
        log_file.setFormatter(log_formate)
        logger=logging.getLogger()
        logger.addHandler(log_file)
        logger.setLevel(logging.INFO)
        return logger
