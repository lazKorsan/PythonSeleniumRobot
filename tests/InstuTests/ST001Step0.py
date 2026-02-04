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
    
    # 4. Yeni kurs oluşturma sayfasına git (Metot kullanarak)
    InstuUtils.navigateToNewCoursePage(driver)
    print("Yeni kurs oluşturma akışı tamamlandı.")
    
    # **********step1 baslangic****************
    
    # course type dropdown tıkla
    COURSTTPE_XPATH = '//select[@class="custom-select "]'    
    courseTypeButton = driver.find_element(By.XPATH, COURSTTPE_XPATH)    
    driver.execute_script("arguments[0].style.border='3px solid red'", courseTypeButton)  
    courseTypeButton.click()
    print("Course type dropdown tıklandı.")
    
    SECOND_OPTION_XPATH = '//select[@class="custom-select "]/option[2]'  
    secondOption = driver.find_element(By.XPATH, SECOND_OPTION_XPATH)

   # dropdownmenude İkinci seçeneğe highlight ekle
    driver.execute_script("arguments[0].style.backgroundColor = 'yellow'", secondOption)

   # İkinci seçeneğe tıkla
    secondOption.click()
    print("İkinci seçenek seçildi.")
    
    # title box bul ve başlık gir
    TITLEBOX_XPATH = '(//input[@class="form-control "])[1]'
    titleBox = driver.find_element(By.XPATH, TITLEBOX_XPATH)
    driver.execute_script("arguments[0].style.border='3px solid blue'", titleBox)    
    titleBox.send_keys("mathematics")
    print("Yeni kurs başlığı mathematics girildi.")
    
    #CEO DescriptionbBox 
    CEODESCRIPTION_XPATH = '//input[@name="seo_description"]'
    ceoDescriptionBox = driver.find_element(By.XPATH, CEODESCRIPTION_XPATH)
    driver.execute_script("arguments[0].style.border='3px solid green'", ceoDescriptionBox)    
    ceoDescriptionBox.send_keys("This is a mathematics course.")
    print("CEO Description box dolduruldu.")
    
    # thumbnail Box 
    THUMBNAIL_XPATH = '//input[@id="thumbnail"]'
    thumbNailBox = driver.find_element(By.XPATH, THUMBNAIL_XPATH)
    driver.execute_script("arguments[0].style.border='3px solid orange'", thumbNailBox)    
    thumbNailBox.send_keys("/store/2014/math1.jpg")  
    print("Thumbnail yüklendi.")
    
    # jpx box
    COVERIMAGE_XPATH = '//input[@id="cover_image"]'
    coverImageBox = driver.find_element(By.XPATH, COVERIMAGE_XPATH)
    driver.execute_script("arguments[0].style.border='3px solid purple'", coverImageBox)    
    coverImageBox.send_keys("/store/2014/3d_difdenk.png")  
    print("Cover image yüklendi.")
    
    # editNote area 
    NOTE_EDİBTALE_XPATH = '//*[@class="note-editable card-block"]'
    noteEditableArea = driver.find_element(By.XPATH, NOTE_EDİBTALE_XPATH)
    driver.execute_script("arguments[0].style.border='3px solid pink'", noteEditableArea) 
    noteEditableArea.click()   
    noteEditableArea.send_keys("Kurs başlangıç tarihi ayın 24 dunde olacak")
    print("Kurs başlangıç tarihi 2nci ayın 24'e ayarlandı")
    
    # next stepButton
    NEXT_STEP_BUTTON_XPATH = '//button[@id="getNextStep"]'
    nextStepButton = driver.find_element(By.XPATH, NEXT_STEP_BUTTON_XPATH)
    driver.execute_script("arguments[0].style.border='3px solid cyan'", nextStepButton) 
    nextStepButton.click()
    print("Next step butonuna tıklandı.")
    
    # sayfanın yuklenmesini bekle
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )
    
    # yeni sayfanın url ini al ve konsola yazdır
    currentUrl = driver.current_url
    print("Yeni sayfanın URL'i:", currentUrl)
    
    # webinar id consola yazdır 
    webinar_id = currentUrl.split('/')[5]  # URL yapısına göre 5. indeks
    
    print("Webinar ID:", webinar_id)
    
    # Webinar ID'sini bir değişkende sakla
    saved_webinar_id = webinar_id
    
    # Daha sonra bu değişkeni kullanabilirsiniz
    print(f"Kayıtlı Webinar ID: {saved_webinar_id}")
    
    # ***********step1 tamamlandı*****************
    
    
finally:   
    time.sleep(5)
    driver.quit()
    print("Tarayıcı kapatıldı.")
