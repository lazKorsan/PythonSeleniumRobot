import sys
import os

print(f"DEBUG: sys.path BEFORE modification: {sys.path}")
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
print(f"DEBUG: Project root to be added: {project_root}")
# Add the project root to the system path to allow importing modules from 'utils'
sys.path.append(project_root)
print(f"DEBUG: sys.path AFTER modification: {sys.path}")

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC                               
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

import InstuUtils 
from utils.config import LoginData

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://qa.instulearn.com/")
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))



InstuUtils.InstuLearnLoginMethod(driver,LoginData.EMAIL,LoginData.PASSWORD)


time.sleep(15)  # Wait for a while to observe the result
