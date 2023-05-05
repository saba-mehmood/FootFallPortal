import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

""" This class is parent of all the pages"""

"""It contains all the generic methods and utilities for all the pages"""


class BasePage:
    """constructor"""
    def __init__(self,driver):
        self.driver=driver
        
        
    """method for locating for click elements"""
    def doo_click(self,by_locator):
        WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(by_locator)).click()

    def do_click(self,by_locator):
        WebDriverWait(self.driver,30).until(EC.presence_of_element_located(by_locator)).click()


    """method for locating  elements for sending key"""  
    def do_send_keys(self,by_locator,text):
        WebDriverWait(self.driver,30).until(EC.presence_of_element_located(by_locator)).send_keys(text)

    """method for locating for  elements"""
    def is_visible(self,by_locator):
       element= WebDriverWait(self.driver,30).until(EC.presence_of_element_located(by_locator)) 
       return element 

    """method for locating for  elements"""
    def is_invisible(self,by_locator):
        __tracebackhide__ = True
        try:
         element= WebDriverWait(self.driver,70).until(EC.invisibility_of_element_located(by_locator)) 
         return element  
        except TimeoutException as ex:

            print("Loading time too much. " + str(ex))
            pytest.fail()