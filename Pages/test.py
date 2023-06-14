from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create an instance of the webdriver
driver = webdriver.Chrome()

# Navigate to the login page
driver.get('https://testuser.yallagrub.com')

# Find the username and password input fields and enter your credentials
username_input = driver.find_element(By.ID, 'username')
password_input = driver.find_element(By.ID, 'password')

username_input.send_keys('your_username')
password_input.send_keys('your_password')

# Submit the login form
login_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
login_button.click()

# Wait for the login process to complete (you can modify the timeout value as needed)
wait = WebDriverWait(driver, 10)
wait.until(EC.url_to_be('https://example.com/dashboard'))

# Perform actions on the logged-in page
# ...

# Close the browser
driver.quit()
