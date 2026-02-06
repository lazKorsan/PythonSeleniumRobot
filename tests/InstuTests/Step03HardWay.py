from collections.abc import KeysView
from winreg import KEY_ENUMERATE_SUB_KEYS
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
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
    
   
   
    # buradaki adım step5in başına dahil edilmeyecek. 
    driver.get("https://qa.instulearn.com/panel/webinars/3637/step/5")
    
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )
    
    
    
    
    # ******step5baslangic*new prerequest  **
    
    # newPrequestButton 
    NEW_PREREQUEST_BUTTON_XPATH = '//button[@id="webinarAddPrerequisites"]'
    newPrequestButton = driver.find_element(By.XPATH, NEW_PREREQUEST_BUTTON_XPATH)
    driver.execute_script("arguments[0].style.border='3px solid green'", newPrequestButton)     
    newPrequestButton.click()
    print("newPrequestButton tıklandı.  ")
    
    # selectPreRequest 
    
    SELECT_PREREQUEST_Xpath = driver.find_element(By.XPATH,'//*[@class="select2-selection__placeholder"]')
    driver.execute_script("arguments[0].style.border='3px solid red'", SELECT_PREREQUEST_Xpath) 
    SELECT_PREREQUEST_Xpath.click()
    
    # selectTypeBox
    selectTypeBox_X_path = '/html/body/span/span/span[1]/input'
    selectTypeBox = driver.find_element(By.XPATH, selectTypeBox_X_path)
    driver.execute_script("arguments[0].style.border='3px solid blue'", selectTypeBox)     
    selectTypeBox.send_keys("SDET")    
    #selectTypeBox.send_keys(Keys.ENTER)  
    location = selectTypeBox.location
    x = location['x']
    y = location['y'] + 30  # 30 piksel aşağı

   # Fareyi tıklanacak konuma hareket ettir
    actions = ActionChains(driver)
    actions.move_by_offset(x, y).click().perform()

    print("30 piksel aşağıya tıklandı.")  
    print("selectTypeBox dolduruldu.")
    
    
    
    
    # saveButton
    saveButton_Xpath = '//button[@class="js-save-prerequisite btn btn-sm btn-primary"]'
    saveButton = driver.find_element(By.XPATH, saveButton_Xpath)
    driver.execute_script("arguments[0].style.border='3px solid orange'", saveButton)     
    saveButton.click()  
    print("yeni istekler eklendi")
    
    
    
    
    
    
    
    
    

    
    
    

    

    
    
    
    
    
    
    
    
finally:
    time.sleep(5)
    driver.quit()
    print("Tarayıcı kapatıldı.")