from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import testData
import InstuUtils

# Driver oluştur
driver = webdriver.Chrome()
driver.maximize_window()
print("Driver oluşturuldu.")

try:
    # 1. Siteye git
    driver.get(testData.login_url)
    print("Siteye gidildi:", testData.login_url)
    
    # 2. Sayfanın yüklenmesini bekle
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )
    
    # 3. Login ol (Metot kullanarak)
    InstuUtils.InstuLearnLoginMethod(driver, testData.mail, testData.password)
    print("Login işlemi tamamlandı.")
    
      # buradaki adım step4nin başına dahil edilmeyecek. 
    driver.get("https://qa.instulearn.com/panel/webinars/3647/step/6")
    
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )
    
   # step6 baslangıc 
   
   # newFAQbUTTON
    nwFAQButton_Xpath = '//button[@id="webinarAddFAQ"]'
    nwFAQButton = driver.find_element(By.XPATH, nwFAQButton_Xpath)
    driver.execute_script("arguments[0].style.border='3px solid red'", nwFAQButton) 
    nwFAQButton.click()
    time.sleep(1)
    
    # titleBox
    titleBox_Xpath = '//input[@name="ajax[new][title]"]'
    titleBox = driver.find_element(By.XPATH, titleBox_Xpath)
    driver.execute_script("arguments[0].style.border='3px solid green'", titleBox)  
    titleBox.send_keys("Ogretmenler ile gorusme sıklıgı")
    time.sleep(1)
     
    # answerBox
    answerBox_Xpath = '//textarea[@name="ajax[new][answer]"]'
    answerBox = driver.find_element(By.XPATH, answerBox_Xpath)
    driver.execute_script("arguments[0].style.border='3px solid blue'", answerBox)  
    answerBox.send_keys("Ogrencilerimiz 2 haftada 1 15 dk zoom gorusmesi yapabilirler")
    time.sleep(1)
    
    # saveButton
    saveButton_Xpath = '//button[@class="js-save-faq btn btn-sm btn-primary"]'
    saveButton = driver.find_element(By.XPATH, saveButton_Xpath)
    driver.execute_script("arguments[0].style.border='3px solid yellow'", saveButton)  
    saveButton.click()
    time.sleep(1)
    
    # nextStepButton
    nextStepButton_Xpath = '//button[@id="getNextStep"]'
    nextStepButton = driver.find_element(By.XPATH, nextStepButton_Xpath)
    driver.execute_script("arguments[0].style.border='3px solid orange'", nextStepButton)  
    nextStepButton.click()
    time.sleep(1)
    
    
   
    
except Exception as e:
    print(f"Bir hata oluştu: {e}")
finally:   
    time.sleep(5)
    driver.quit()
    print("Tarayıcı kapatıldı.")