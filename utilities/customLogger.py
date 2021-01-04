import logging

class LogGen:

    @staticmethod
    def logGeneration():

        logger=logging.getLogger()
        handler=logging.FileHandler('.\\LogFiles\\auto1.log')
        formatter=logging.Formatter('%(asctime)s: %(levelname)s: %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
        return logger
