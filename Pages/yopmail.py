import time
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from Config.config import TestData
from selenium.webdriver.common.keys import Keys
from Pages.locatorsPage import Locators


class YopmailPage(BasePage):
    
    """constructor"""
    def __init__(self,driver):
        self.driver=driver

    """SIGNUP METHOD"""

    def Yopmail_signup(self,email):
        """ RUNNING SCRIPT TO THE NEW WINDOW"""
        self.driver.execute_script("window.open()")

        """ ASSIGNING INDEX 1 TO YOPMAIL WINDOW"""
        self.driver.switch_to.window(self.driver.window_handles[1])    
        self.driver.get(TestData.YOPMAIL_URL)
        time.sleep(2)
        self.mail_field = self.is_visible(Locators.YOP_EMAIL_FIELD)
        self.mail_field.send_keys(Keys.CONTROL, "a")
        self.mail_field.send_keys(Keys.BACKSPACE)
        #self.mail_field.send_keys(self,email)
        self.do_send_keys(Locators.YOP_EMAIL_FIELD,TestData.EMAIL)
        self.do_click(Locators.YOP_SEND_BTN)
        time.sleep(5)
        self.driver.switch_to.frame(self.is_visible(Locators.YOP_FRAME))

        try:
            SIGNUP_LINK_CLICK = self.is_visible(Locators.CONTINUE_LINK)
        
            if SIGNUP_LINK_CLICK.is_displayed():
                SIGNUP_LINK_CLICK.click()
                print(self.driver.title)
      
        except:
            SIGNUP_LINK_VERIFY = self.is_visible(Locators.VERIFY_LINK)

            if SIGNUP_LINK_VERIFY.is_displayed():
                SIGNUP_LINK_VERIFY.click()
                print(self.driver.title)

            else:  
                print("NO LINK AND BUTTON FOUND")  
              
        time.sleep(2)