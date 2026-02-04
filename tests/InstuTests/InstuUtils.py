from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import logging
import time
import InstuPages

def InstuLearnLoginMethod(driver, email, password):
    # Giriş linkine tıkla
    

    # sayfanın yüklenmesini bekle
    time.sleep(2)

    # emailBox'a email adresini gir
    emailBox_ID = 'email'
    emailBox = driver.find_element(By.ID, emailBox_ID)
    emailBox.send_keys(email)
    logging.info("Entered email address")

    # passwordBox'a şifreyi gir
    passwordBox_ID = 'password'
    passwordBox = driver.find_element(By.ID, passwordBox_ID)
    passwordBox.send_keys(password)
    logging.info("Entered password")

    # loginSubmitButton tıkla
    loginSubmitButton_Class = '//button[@class="btn btn-primary btn-block mt-20"]'
    loginSubmitButton = driver.find_element(By.XPATH, loginSubmitButton_Class)
    loginSubmitButton.click()
    logging.info("Clicked on login submit button")
def InstuLearnRegisterMethod(driver, userName, password):
    """
    Kayıt olma metodudur. Mail adresi otomatik (benzersiz) üretilir.
    """
    try:
        driver.get("https://qa.instulearn.com/")
        time.sleep(2)

        # 1. Register sayfasına giden butona tıkla
        register_xpath = '//a[@href="/register" and contains(@class, "text-dark-blue")]'
        driver.find_element(By.XPATH, register_xpath).click()
        time.sleep(2)

        # 2. Instructor seçimi
        instructor_xpath = '(//*[@class="font-12 cursor-pointer px-15 py-10"])[2]'
        driver.find_element(By.XPATH, instructor_xpath).click()
        time.sleep(2)

        # 3. Kullanıcı Adı
        driver.find_element(By.ID, 'full_name').send_keys(userName)

        # 4. Dinamik Email Üretme (Hata almamak için her seferinde farklı mail üretir)
        dinamik_email = userName + str(int(time.time())) + "@gmail.com"
        driver.find_element(By.ID, 'email').send_keys(dinamik_email)

        # 5. Şifre ve Onay Şifre
        driver.find_element(By.ID, 'password').send_keys(password)
        driver.find_element(By.ID, 'password_confirmation').send_keys(password)
        time.sleep(1)

        # 6. Kayıt Butonu
        driver.find_element(By.XPATH, '//button[@type="submit" and contains(@class, "btn-primary")]').click()
        time.sleep(3)   # Sayfayı bekle

        # 7. Doğrulama (Verification)   
        try:
            # Kayıt sonrası login sayfasına yönlendirme kontrolü
            driver.find_element(By.XPATH, '//a[@href="/login" and contains(@class, "text-dark-blue")]')
            print("Kayıt BAŞARILI! ✅")
            return True
        except:
            print("Kayıt BAŞARISIZ! ❌")
            return False

    except Exception as e:
        print(f"Kayıt sırasında bir hata oluştu hocam: {e}")
        return False
    
# driver.quit() # Tarayıcıyı kapatmak istersen açabilirsin

def navigateToNewCoursePage(driver):
    """
    Navigates from the main panel to the new course/webinar creation page.
    """
    print("Navigating to new course page...")
    # 4. Page object oluştur
    instu_pages = InstuPages.InstuPages(driver)
    
    # 5. Courses butonuna tıkla (METHOD'u çağır!)
    instu_pages.click_coursesButton()
    
    # 6. Bekle ve kontrol et
    time.sleep(2)
    
    # 7. Panel sayfasına gidildiğini doğrula ve ardından 'New Webinar' butonuna tıkla
    panel_url = driver.current_url
    print(f"Mevcut URL: {panel_url}")
    
    # URL'in 'panel' içerdiğini kontrol et
    if "panel" in panel_url:
        print("✅ BAŞARILI: Panel sayfasına gidildi!")

        # 8. New Webinar butonuna tıkla (Page Object Model kullanarak)
        instu_pages.click_new_webinar_button()
        
        # 9. Yeni sayfanın yüklenmesini bekle ve URL'i kontrol et
        try:
            WebDriverWait(driver, 10).until(EC.url_contains("webinars/new"))
            new_page_url = driver.current_url
            print(f"Yeni Sayfa URL: {new_page_url}")
            print("✅ BAŞARILI: New Webinar sayfasına başarıyla gidildi!")
        except:
            print("❌ HATA: New Webinar sayfasına gidilemedi veya URL 'webinars/new' içermiyor.")

    else:
        print("❌ HATA: Panel sayfasına gidilemedi! (URL 'panel' içermiyor)")
        
        
def step1(driver):
    #import time
    #from selenium.webdriver.common.by import By
    #from selenium.webdriver.support.ui import WebDriverWait
    #from selenium.webdriver.support import expected_conditions as EC

    try:
        # Course type dropdown tıkla
        COURSTTPE_XPATH = '//select[@class="custom-select "]'
        courseTypeButton = driver.find_element(By.XPATH, COURSTTPE_XPATH)
        driver.execute_script("arguments[0].style.border='3px solid red'", courseTypeButton)
        courseTypeButton.click()
        print("Course type dropdown tıklandı.")

        SECOND_OPTION_XPATH = '//select[@class="custom-select "]/option[2]'
        secondOption = driver.find_element(By.XPATH, SECOND_OPTION_XPATH)

        # Dropdown menüde İkinci seçeneğe highlight ekle
        driver.execute_script("arguments[0].style.backgroundColor = 'yellow'", secondOption)

        # İkinci seçeneğe tıkla
        secondOption.click()
        print("İkinci seçenek seçildi.")

        # Title box bul ve başlık gir
        TITLEBOX_XPATH = '(//input[@class="form-control "])[1]'
        titleBox = driver.find_element(By.XPATH, TITLEBOX_XPATH)
        driver.execute_script("arguments[0].style.border='3px solid blue'", titleBox)
        titleBox.send_keys("mathematics")
        print("Yeni kurs başlığı mathematics girildi.")

        # CEO Description Box
        CEODESCRIPTION_XPATH = '//input[@name="seo_description"]'
        ceoDescriptionBox = driver.find_element(By.XPATH, CEODESCRIPTION_XPATH)
        driver.execute_script("arguments[0].style.border='3px solid green'", ceoDescriptionBox)
        ceoDescriptionBox.send_keys("This is a mathematics course.")
        print("CEO Description box dolduruldu.")

        # Thumbnail Box
        THUMBNAIL_XPATH = '//input[@id="thumbnail"]'
        thumbNailBox = driver.find_element(By.XPATH, THUMBNAIL_XPATH)
        driver.execute_script("arguments[0].style.border='3px solid orange'", thumbNailBox)
        thumbNailBox.send_keys("/store/2014/math1.jpg")
        print("Thumbnail yüklendi.")

        # Cover Image Box
        COVERIMAGE_XPATH = '//input[@id="cover_image"]'
        coverImageBox = driver.find_element(By.XPATH, COVERIMAGE_XPATH)
        driver.execute_script("arguments[0].style.border='3px solid purple'", coverImageBox)
        coverImageBox.send_keys("/store/2014/3d_difdenk.png")
        print("Cover image yüklendi.")

        # Edit Note area
        NOTE_EDITABLE_XPATH = '//*[@class="note-editable card-block"]'
        noteEditableArea = driver.find_element(By.XPATH, NOTE_EDITABLE_XPATH)
        driver.execute_script("arguments[0].style.border='3px solid pink'", noteEditableArea)
        noteEditableArea.click()
        noteEditableArea.send_keys("Kurs başlangıç tarihi ayın 24 dünde olacak")
        print("Kurs başlangıç tarihi 2nci ayın 24'e ayarlandı")

        # Next step button
        NEXT_STEP_BUTTON_XPATH = '//button[@id="getNextStep"]'
        nextStepButton = driver.find_element(By.XPATH, NEXT_STEP_BUTTON_XPATH)
        driver.execute_script("arguments[0].style.border='3px solid cyan'", nextStepButton)
        nextStepButton.click()
        print("Next step butonuna tıklandı.")

        # Sayfanın yüklenmesini bekle
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

        # Yeni sayfanın URL'sini al ve konsola yazdır
        currentUrl = driver.current_url
        print("Yeni sayfanın URL'i:", currentUrl)

        # Webinar ID'yi consola yazdır
        webinar_id = currentUrl.split('/')[5]  # URL yapısına göre 5. indeks
        print("Webinar ID:", webinar_id)

        # Webinar ID'sini bir değişkende sakla
        saved_webinar_id = webinar_id
        print(f"Kayıtlı Webinar ID: {saved_webinar_id}")

    except Exception as e:
        print("Hata:", e)
    finally:
        time.sleep(5)
        