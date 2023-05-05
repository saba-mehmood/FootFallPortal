from time import sleep, time
from Pages.BasePage import BasePage
from Config.config import TestData
from Pages.locatorsPage import Locators
from Pages.alert import Alert
from Pages.signIn import SignIn


class AddCam(BasePage):


    """CONSTRUCTOR"""
    def __init__(self, driver):

        """INHERIT BASE CLASS"""
        super().__init__(driver)
    
    
    def addcam(self,name,desc,location,stream):

        """ CALLING LOGIN PAGE """
        login = SignIn(self.driver)
        login.signIn(TestData.EMAIL,TestData.PASSWORD)
        sleep(3)

        """ ADD CAMERA """
        self.do_click(Locators.ADD_CAM)
        self.do_send_keys(Locators.CAM_NAME,name)
        self.do_send_keys(Locators.DESC,desc)
        self.do_send_keys(Locators.LOCATION,location)
        self.do_send_keys(Locators.STREAM_URL,stream)
        self.do_click(Locators.CREAT_BUTTON)
        sleep(2)

        """ HANDLING ADD CAMERA """
        self.a = Alert(self.driver)
        self.a.creatcam()
        sleep(2)
        

        

