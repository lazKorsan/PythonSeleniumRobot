from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import logging
import time
from InstuUtils import InstuLearnLoginMethod

driver = webdriver.Chrome()
driver.maximize_window()

# Navigate to the InstuLearn QA website
driver.get("https://qa.instulearn.com/")
logging.info("Navigated to InstuLearn QA website")

# Wait for the page to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

# Perform login using the method
InstuLearnLoginMethod(driver, "lazKorsan030220260417@gmail.com", "Query.2026")

# Add a small delay to observe the result
time.sleep(5)

# Close the browser
driver.quit()
