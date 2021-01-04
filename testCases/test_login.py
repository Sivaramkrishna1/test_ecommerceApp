import pytest
from selenium import webdriver
from pageObjects.LogInPage import LoginPage
from utilities.readProperties import ReadConfig as rc
from utilities.customLogger import LogGen

class Test_001_Login:
    baseurl=rc.getApplicationUrl()
    username=rc.getUseremail()
    password=rc.getPassword()
    logger=LogGen.logGeneration()

    @pytest.mark.regression
    def test_homePageTitle(self,setup):
        self.logger.info('********** Test_001_Login **********')
        self.logger.info('********** Verifying homepage Title **********')
        self.driver=setup
        self.driver.get(self.baseurl)
        act_title=self.driver.title
        if act_title == 'Your store. Login':
            assert True
            self.driver.close()
            self.logger.info('*********** homepage title test is passed *******')
        else:
            self.driver.save_screenshot('.\\Screenshots\\'+'test_homePageTitle.png')#(.\\-------\\) is current directory
            self.driver.close()
            self.logger.error('********* homepage title test is failed *************')
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info('********* Test_001_Login *******')
        self.logger.info('********* Verifying Login Test *******')
        self.driver=setup
        self.driver.get(self.baseurl)
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setUserPassword(self.password)
        self.lp.clickLogin()
        act_title=self.driver.title

        if act_title == 'Dashboard / nopCommerce administration':
            assert True
            self.driver.close()
            self.logger.info('********* Login test is passed *********')
        else:
            self.driver.save_screenshot('.\\Screenshots\\'+'test_login.png')
            self.driver.close()
            self.logger.error('********* Login test is failed ********')
            assert False