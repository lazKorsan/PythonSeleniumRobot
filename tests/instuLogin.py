from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import logging
import time

driver = webdriver.Chrome();
driver.maximize_window();

# Navigate to the InstuLearn QA website
driver.get("https://qa.instulearn.com/")
logging.info("Navigated to InstuLearn QA website")

# sayfanın yüklenmesini beklele
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

# loginButton  tıkla
loginButton_Xpath = '//a[@href="/login" and contains(@class, "text-dark-blue")]'
loginButton = driver.find_element(By.XPATH,loginButton_Xpath)
loginButton.click()
logging.info("Clicked on login button")

# sayfanın yüklenmesini beklele
time.sleep(2) 

# emailBox'a email adresini gir
emailBox_ID = 'email'
emailBox = driver.find_element(By.ID, emailBox_ID)
emailBox.send_keys("lazKorsan030220260417@gmail.com")
logging.info("Entered email address")

# passwordBox'a şifreyi gir
passwordBox_ID = 'password'
passwordBox = driver.find_element(By.ID, passwordBox_ID)
passwordBox.send_keys("Query.2026")
logging.info("Entered password")

# loginSubmitButton tıkla  
loginSubmitButton_Class = '//button[@class="btn btn-primary btn-block mt-20"]'
loginSubmitButton = driver.find_element(By.XPATH, loginSubmitButton_Class)
loginSubmitButton.click()
logging.info("Clicked on login submit button")









