from Config.config import TestData
from Pages.signIn import SignIn
from Test.test_Base import BaseTest

class TestSignIn(BaseTest):
    def test_signin(self):
        self.signupPage=SignIn(self.driver)
        self.signupPage.signIn(TestData.EMAIL,TestData.PASSWORD)