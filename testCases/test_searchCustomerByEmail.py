from pageObjects.LogInPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from selenium import webdriver
import pytest
import time

class Test_004_SearchCustomerByEmail:

    baseurl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.logGeneration()  # Logger

    @pytest.mark.regression
    def test_searchCustomerByEmail(self,setup):
        self.logger.info('******** test_004-searchCustomer ********')
        self.driver=setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()

        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setUserPassword(self.password)
        self.lp.clickLogin()
        self.logger.info('******* login sucesssfulll **********')

        self.addcust=AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()

        self.logger.info('******** searching customer by emailid **********')

        searchcust=SearchCustomer(self.driver)
        searchcust.setEmail('victoria_victoria@nopCommerce.com')
        searchcust.clickSearch()
        time.sleep(3)
        status=searchcust.searchCustomerByEmail('victoria_victoria@nopCommerce.com')
        assert True==status
        self.logger.info('****** test searchcustomer is finished **********')
        self.driver.close()
