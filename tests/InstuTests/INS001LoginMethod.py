

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

import InstuUtils 
import testData


driver = webdriver.Chrome()
driver.maximize_window()

# Navigate to the login page directly
driver.get("https://qa.instulearn.com/login")
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

# Perform login using the method from InstuUtils
InstuUtils.InstuLearnLoginMethod(driver, testData.mail, testData.password)



time.sleep(15)  # Wait for a while to observe the result
