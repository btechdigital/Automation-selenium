from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# Set up options
options = Options()
options.add_experimental_option("detach", True)  # Corrected syntax here

service = Service('chromedriver.exe') 

driver = webdriver.Chrome(service=service, options=options)

driver.get('https://practicetestautomation.com/practice/')

success_url = "https://practicetestautomation.com/logged-in-successfully/"


#click Login Url
driver.find_element(By.LINK_TEXT, 'Test Login Page').click()

#send keys
driver.find_element(By.NAME,"username").send_keys('student')
driver.find_element(By.NAME, "password").send_keys('Password123')
submit_btn = driver.find_element(By.ID, "submit").click()

try:
    error_message = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'error'))
        ).text
    print("Error message displayed:", error_message)
    # assert " Invalid Credentials " in error_message
except:
    driver.get(success_url)


finally:
    driver.find_element(By.CLASS_NAME, 'wp-block-button').click()
    print("Log Out Successfully")
    time.sleep(25)  
    driver.quit()




