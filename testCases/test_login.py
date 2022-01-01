import pytest
from selenium import webdriver
from pageObjects.LoginPage import loginPage
from testCases.confitest import setup
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_homepageTitle(self,setup):

        self.logger.info("***************Test_001_Login*******")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        actual_title = self.driver.title
        self.driver.close()
        if actual_title == "Your store. Login":
            assert True
            self.logger.info("***************Home page Title Passed *******")
        else:
            assert False
            self.logger.info("***************Home page Title Failed *******")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        self.lp = loginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassWord(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        print(("after login Title"+act_title))
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")
            assert False
            self.driver.close()
