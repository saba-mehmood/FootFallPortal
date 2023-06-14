from selenium.webdriver.support.ui import Select
from time import sleep, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta


# Create an instance of the webdriver
driver = webdriver.Chrome()
driver.maximize_window()

# Navigate to the login page
driver.get('https://testuser.yallagrub.com')

driver.find_element(By.XPATH,"//body/div[@id='root']/div[contains(@class,'pl-4 pt-4')]/div[contains(@class,'')]/ul[contains(@class,'react-multi-carousel-track')]/li[4]/div[1]/div[1]/div[1]").click()
sleep(2)
driver.find_element(By.XPATH,"//div[normalize-space()='Unleavened bread stuffed with potato & vegetables. Served with special afghani chutni & pickle']").click()
sleep(2)
driver.find_element(By.XPATH,"//div[@class='flex justify-between items-center menu-quantity-items']//div[3]//*[name()='svg']").click()
sleep(2)
driver.find_element(By.XPATH,"//input[@id='cc661aec-15b5-4071-9d97-ec94cb18211e']").click()
sleep(2)
driver.find_element(By.XPATH,"//button[@class='flex w-full bg-pink text-white py-3 px-4 rounded justify-between']").click()
driver.find_element(By.XPATH,"//div[normalize-space()='Shinwari BBQ']").click()
sleep(2)
start_plan=driver.find_element(By.XPATH,'//*[@id="root"]/div[2]/div[2]/div[3]/div/div[2]/div[2]/div[2]/button')
start_plan.click()
driver.find_element(By.XPATH,"//div[contains(@class,'text-xs')]")
print("done")

# Calculate tomorrow's date

tomorrow = datetime.now() + timedelta(days=1)
tomorrow_date = tomorrow.strftime("%Y-%m-%d")
enter = driver.find_element(By.XPATH,"//div[@class='text-xs']")
enter.clear()
enter.click()
enter.send_keys(tomorrow_date)

sleep(3)


# Close the browser
driver.quit()
