from Config.config import TestData
from Pages.signIn import SignIn
from Test.test_Base import BaseTest
from Pages.addCamera import AddCam

class TestAddCam(BaseTest):
    def test_addcam(self):
        self.addcam=AddCam(self.driver)
        self.addcam.addcam(TestData.NAME,TestData.DESC,TestData.LOCATION,TestData.STREAM_URL)