from pageObjects.LogInPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from selenium import webdriver
import pytest
import time

class Test_005_searchCustomerByName:
    baseurl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.logGeneration()  # Logger

    @pytest.mark.regression
    def test_searchCustomerByName(self,setup):
        self.logger.info('******* Test_005_searchcustomerByName ******')
        self.driver=setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()

        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setUserPassword(self.password)
        self.lp.clickLogin()
        self.logger.info('*********** login sucessfull *********')

        self.addcust=AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()

        self.logger.info('******** searching by Name *********')

        searchName=SearchCustomer(self.driver)
        searchName.setFirstName('Victoria')
        searchName.setLastName('Terces')
        searchName.clickSearch()
        time.sleep(3)
        status=searchName.searchCustomerByName('Victoria Terces')
        assert True == status
        self.logger.info('********* test_005_searchCustomerByNameis fnished *********')
        self.driver.close()