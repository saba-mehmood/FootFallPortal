from time import sleep, time
from Pages.BasePage import BasePage
from Config.config import TestData
from Pages.locatorsPage import Locators
from Pages.alert import Alert


class SignIn(BasePage):


    """CONSTRUCTOR"""
    def __init__(self, driver):

        """INHERIT BASE CLASS"""
        super().__init__(driver)
    
    """CREATING PAGE ACTIONS"""
    def signIn(self,email,password):
        self.driver.get(TestData.SIGNIN_URL)
        self.driver.window_handles[0]
        sleep(3)

        self.do_send_keys(Locators.SIGIN_EMAIL,email)
        self.do_send_keys(Locators.SIGIN_PASSWORD,password)
        self.do_click(Locators.SIGNUP_BUTTON)
        sleep(3)

        """HANDLING OTP VERIfY"""
        self.a = Alert(self.driver)
        self.a.signin()

        sleep(4)


        