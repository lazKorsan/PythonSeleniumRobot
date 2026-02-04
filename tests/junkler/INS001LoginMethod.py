

import InstuUtils



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from utils.config import LoginData  # Import the LoginData class from the config module
import time

import InstuUtils  # Import the InstuUtils module for the login method



from utils.config import LoginData

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://qa.instulearn.com/")
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

InstuUtils.InstuLearnLoginMethod(driver, LoginData.EMAIL, LoginData.PASSWORD)


time.sleep(15)  # Wait for a while to observe the result
