import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL( ):
        baseURL = config.get('common info','baseURL')
        return baseURL
    @staticmethod
    def getUseremail():
        username = config.get('common info','username')
        return username
    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password