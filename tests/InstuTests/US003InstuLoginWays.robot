
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import logging
import time
from InstuUtils import InstuLearnLoginMethod

driver = webdriver.Chrome()
driver.maximize_window()





driver.get("https://qa.instulearn.com/")