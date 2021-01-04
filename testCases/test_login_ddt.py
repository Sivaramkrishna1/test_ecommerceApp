import pytest
from selenium import webdriver
from pageObjects.LogInPage import LoginPage
from utilities.readProperties import ReadConfig as rc
from utilities.customLogger import LogGen
from utilities import XLUtils
import time

class Test_002_DDT_Login:
    baseurl=rc.getApplicationUrl()
    path='.//TestData/DataDrive.xlsx'
    logger=LogGen.logGeneration()

    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info('********* Test_002_DDT_Login *******')
        self.logger.info('********* Verifying Login Test *******')
        self.driver=setup
        self.driver.get(self.baseurl)

        self.lp=LoginPage(self.driver)

        self.rows=XLUtils.getRowCount(self.path,'Sheet1')
        print('number of Rows:',self.rows)

        status_list=[]

        for r in range(2,self.rows+1):
            self.user=XLUtils.readData(self.path,'Sheet1',r,1)
            self.password=XLUtils.readData(self.path,'Sheet1',r,2)
            self.exp=XLUtils.readData(self.path,'Sheet1',r,3)

            self.lp.setUserName(self.user)
            self.lp.setUserPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title=self.driver.title
            exp_title='Dashboard / nopCommerce administration'

            if act_title == exp_title:
                if self.exp == 'test passed':
                    self.logger.info('*********  passed  ********')
                    self.lp.clickLogout()
                    status_list.append('pass')
                elif self.exp == 'test fail':
                    self.logger.info('*******  failed ********')
                    self.lp.clickLogout()
                    status_list.append('fail')

            elif act_title != exp_title:
                if self.exp == 'test passed':
                    self.logger.info('******* failed ********')
                    status_list.append('fail')
                elif self.exp == 'test fail':
                    self.logger.info('******  pass  ******')
                    status_list.append('pass')

        if 'fail' not in status_list:
            self.logger.info('############## login DDT test pass ############')
            self.driver.close()
            assert True
        else:
            self.logger.info('############ login DDT test fail ############')
            self.driver.close()
            assert False

        self.logger.info('------------- end of login DDT test  ----------')
        self.logger.info('------------- Complete login DDT test  ----------')