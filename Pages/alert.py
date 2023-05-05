import time
import pytest
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC

class Alert(object):

    def __init__(self,driver):
        self.driver = driver

    """SIGNUP NEXT PAGE"""
    def email_already_exist(self):
        alert = "Email already exists"
        
        try:   
          element_alert =  self.driver.find_element(By.CLASS_NAME, 'Toastify__toast-body') 
          element_otp =  self.driver.find_element(By.XPATH, "//h3[@class='text-center']")  
             
          alert2 = element_alert.get_attribute('textContent')
          
          if alert2 == alert:
              assert alert2 == alert
              pytest.fail(alert2)

        except NoSuchElementException:
            print()

    
    """VERIFY OTP"""
    def verify_otp(self):
        alert = "OTP Verified"
        
        try:   
          element_alert =  self.driver.find_element(By.CLASS_NAME, 'Toastify__toast-body')   
          alert2 = element_alert.get_attribute('textContent')
          
          if alert2 == alert:
              assert alert2 == alert
              
          elif alert2 != alert:
              pytest.fail(alert2)    

        except NoSuchElementException:
            print()
            

        ######################################################################################################
        ####################################### SIGN IN ######################################################
        
    def signin(self):
        alert = "Sign in successfully"
        
        try:   
         element_alert =  self.driver.find_element(By.CLASS_NAME, 'Toastify__toast-body')   
         alert2 = element_alert.get_attribute('textContent')
           
         if alert2 == alert:
               assert alert2 == alert
               
         elif alert2 != alert:
               pytest.fail(alert2)    
 
        except NoSuchElementException:
            print()

        ######################################################################################################
        ####################################### CREATE CAMERA #################################################
        
    def creatcam(self):
        alert = "Camera added successfully"
        
        try:   
         element_alert =  self.driver.find_element(By.CLASS_NAME, 'Toastify__toast-body')   
         alert2 = element_alert.get_attribute('textContent')
           
         if alert2 == alert:
               assert alert2 == alert
               print(alert)
               
         elif alert2 != alert:
               pytest.fail(alert2)    
 
        except NoSuchElementException:
            print()   
  
         
         

    