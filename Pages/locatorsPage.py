from selenium.webdriver.common.by import By

class Locators:

    ####################################################################################################
    ##################################### SIGN UP LOCATORS #############################################
    
    EMAIL = (By.XPATH,"//input[@id='email']")
    FIRST_NAME = (By.XPATH,"//input[@id='firstName']")
    LAST_NAME = (By.XPATH,"//input[@id='lastName']")
    PASSWORD = (By.XPATH, "//input[@id='password']")
    CONFIRM_PASS = (By.XPATH,"//input[@id='confirmPassword']")
    SIGNUP_BUTTON = (By.XPATH,"//button[@type='submit']")
    
    ###################################################################################################
    ##################################### OTP WINDOW ##################################################
    
    OTP_FIELD = (By.XPATH,"//input[@placeholder='Enter OTP here...']")
    VERIFY_OTP = (By.XPATH,"//button[normalize-space()='Verify OTP']")
    
    ##################################################################################################
    ##################################### YOPMAIL ####################################################

    YOP_EMAIL_FIELD = (By.XPATH,"//input[@id='login']")
    YOP_SEND_BTN = (By.XPATH,"//i[@class='material-icons-outlined f36']")
    YOP_FRAME = (By.ID,"By.ID,'ifmail'")

    ##################################################################################################
    ##################################### SIGN IN ####################################################

    SIGIN_EMAIL = (By.XPATH,"//input[@id='email']")
    SIGIN_PASSWORD = (By.XPATH,"//input[@id='password']")
    SIGIN_BUTTON = (By.XPATH,"//button[@type='submit']")

    ##################################################################################################
    ##################################### ADD CAMERA #################################################

    ADD_CAM = (By.XPATH,"//button[@type='button']")
    CAM_NAME = (By.XPATH,"//input[@placeholder='Enter camera name']")
    DESC = (By.XPATH,"//input[@placeholder='Enter camera description']")
    LOCATION = (By.XPATH,"//input[@placeholder='Enter camera location']")
    STREAM_URL = (By.XPATH,"//input[@placeholder='Enter stream URL']")
    CREAT_BUTTON = (By.XPATH,"//button[normalize-space()='Create']")

    
