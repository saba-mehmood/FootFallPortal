
from time import sleep, time
from Pages.BasePage import BasePage
from Config.config import TestData
from Pages.locatorsPage import Locators
from Pages.alert import Alert


class SignUp(BasePage):


    """CONSTRUCTOR"""
    def __init__(self, driver):

        """INHERIT BASE CLASS"""
        super().__init__(driver)
    
    """CREATING PAGE ACTIONS"""
    def signup(self,email,f_name,l_name,password,confirm_pass):
        self.driver.get(TestData.FootFall_URL)
        self.driver.window_handles[0]
        sleep(3)
        self.do_send_keys(Locators.EMAIL,email)
        self.do_send_keys(Locators.FIRST_NAME,f_name)
        self.do_send_keys(Locators.LAST_NAME,l_name)
        self.do_send_keys(Locators.PASSWORD,password)
        self.do_send_keys(Locators.CONFIRM_PASS,confirm_pass)
        self.do_click(Locators.SIGNUP_BUTTON)
        sleep(2)
        
        """HANDLING EMAIL ALREADY EXIST"""
        self.a = Alert(self.driver)
        self.a.email_already_exist()

        sleep(5)


        """OTP WINDOW"""
        self.do_send_keys(Locators.OTP_FIELD,'1234')
        self.do_click(Locators.VERIFY_OTP)

        sleep(3)


        """HANDLING OTP VERIfY"""
        self.a = Alert(self.driver)
        self.a.verify_otp()

      
        


