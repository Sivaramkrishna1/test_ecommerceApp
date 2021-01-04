import pytest
from selenium import webdriver
from pageObjects.LogInPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
import string
import random

class Test_003_AddCustomer:
    baseurl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.logGeneration()   #Logger

    @pytest.mark.sanity
    def test_addCustomer(self,setup):
        self.logger.info('********** Test_003_AddCustomer *********')
        self.driver=setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setUserPassword(self.password)
        self.lp.clickLogin()
        self.logger.info('*********** Login succesfull *********')

        self.addcust=AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()
        self.addcust.clickOnAddnew()

        self.logger.info('********* provinding customer details *********')

        self.email = random_generator() + '@gmail.com'
        self.addcust.setEmail(self.email)
        self.addcust.setPassword('test123')
        self.addcust.setNewsletter('Test store 2')
        self.addcust.setCustomerRoles('Guests')
        self.addcust.setManagerOfVendor('Vendor 2')
        self.addcust.setGender('Male')
        self.addcust.setFirstName('Siva')
        self.addcust.setLastName('Ram')
        self.addcust.setDob('7/05/1992')
        self.addcust.setCompanyName('busyQA')
        self.addcust.setAdminContent('this is for testing.............')
        self.addcust.clickOnSave()

        self.logger.info('********** saving customer info ********')

        self.logger.info('****** add customer validation started ********')

        self.msg=self.driver.find_element_by_tag_name('body').text
        print(self.msg)
        if 'The new customer has been added successfully.' in self.msg:
            assert True == True
            self.logger.info('********* add customer test passed *******')
        else:
            self.driver.save_screenshot('.\\Screenshots\\'+ 'test_addCustomer-scr.png')
            self.logger.error('******* add customer test failed *******')
            assert True == False
        self.driver.close()
        self.logger.info('****** Ending AddCustomer_test ***********')

def random_generator(size=8,char=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(char) for x in range(size))

