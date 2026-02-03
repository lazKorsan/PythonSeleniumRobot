from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import logging
import time

def InstuLearnLoginMethod(driver, email, password):
    # Giriş linkine tıkla
    login_link_xpath = '//a[@href="/login" and contains(@class, "text-dark-blue")]'
    driver.find_element(By.XPATH, login_link_xpath).click()
    time.sleep(2)

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