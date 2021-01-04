from selenium import webdriver
import pytest

@pytest.fixture( )
def setup(browser):
    if browser == 'chrome':
        driver=webdriver.Chrome()
        print('-----launching Chrome browser------')
    elif browser == 'firefox':
        driver=webdriver.Firefox()
        print('-----launching FireFox browser------')
    elif browser == 'ie':
        driver=webdriver.Ie()
    else:
        driver=webdriver.Chrome()
    return driver

def pytest_addoption(parser):           #this will get the value from CLI/hooks (cmd)
    parser.addoption('--browser')      #here addoption is a  buit-in method


@pytest.fixture()
def browser(request):                     #this will return the browser value to setup method
    return request.config.getoption('--browser')

################### pytest HTML Reports #################
#it is hook for adding Environment info to HTML Reports

def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commmerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester Name'] = 'SRK'

#it is hook for deleting/modify Environmentninfo to HTML Reports
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME',None)
    metadata.pop('Plugins',None)