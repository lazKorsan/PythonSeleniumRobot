from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

def LoyalFriendLoginMethod(driver, email, sifre, beklenen_isim):
    try:
        # Giriş linkine tıkla
        login_link_xpath = '//*[@id="top_menu"]/li[1]/a'
        driver.find_element(By.XPATH, login_link_xpath).click()
        time.sleep(2)

        # Bilgileri doldur
        actions = ActionChains(driver)
        actions.send_keys(email) \
               .send_keys(Keys.TAB) \
               .send_keys(sifre) \
               .send_keys(Keys.ENTER) \
               .perform()
        
        time.sleep(3)

        # Doğrulama
        xpath_kullanici = "//a[@class='btn_add']"
        gercek_isim = driver.find_element(By.XPATH, xpath_kullanici).text.strip()

        print(f"\nBeklenen: {beklenen_isim} / Gelen: {gercek_isim}")
        
        if gercek_isim == beklenen_isim:
            print("Giriş Başarılı! ✅")
            return True
        else:
            print("Giriş Başarısız! ❌")
            return False
            
    except Exception as e:
        print(f"Hata: {e}")
        return False
    
    
def LoyalFriendRegisterMethod(driver, userName, password, comfirmPassword):
    """
    Kayıt olma metodudur. Mail adresi otomatik (benzersiz) üretilir.
    """
    try:
        driver.get("https://qa.loyalfriendcare.com/en")
        time.sleep(2)

        # 1. Sign In / Register sayfasına giden butona tıkla
        # Not: Genelde [2] gibi indexler risklidir ama mevcut yapına sadık kaldım
        signInButton1 = driver.find_element(By.XPATH, '(//*[@class="btn_add"])[2]')
        signInButton1.click()
        time.sleep(2)

        # 2. Kullanıcı Adı
        driver.find_element(By.XPATH, '//input[@id="name"]').send_keys(userName)

        # 3. Dinamik Email Üretme (Hata almamak için her seferinde farklı mail üretir)
        # Parametre olarak mail almana gerek yok, burada üretiyoruz
        dinamik_email = userName + str(int(time.time())) + "@gmail.com"
        driver.find_element(By.XPATH, '//input[@id="email"]').send_keys(dinamik_email)
        print(f"Kaydedilen Email: {dinamik_email}")

        # 4. Şifreler
        driver.find_element(By.XPATH, '//input[@id="password"]').send_keys(password)
        driver.find_element(By.XPATH, '//input[@id="password-confirm"]').send_keys(comfirmPassword)
        time.sleep(1)

        # 5. Kayıt Butonu
        signUpButton = driver.find_element(By.XPATH, '//button[@class="btn btn-primary btn-cons m-t-10"]')
        signUpButton.click()
        time.sleep(3)

        # 6. Doğrulama (Verification)
        # Buradaki püf noktası: expectedUserName parametre olarak gelen userName olmalı
        xpath_isim_yeri = "//a[@class='btn_add']"
        element = driver.find_element(By.XPATH, xpath_isim_yeri)
        gercek_isim = element.text.strip()

        print("\n--- KAYIT TEST SONUCU ---")
        print(f"Beklenen (Parametre): {userName}")
        print(f"Gelen (Sitedeki): {gercek_isim}")

        if gercek_isim == userName:
            print("Kayıt başarılı, kullanıcı adı doğru görünüyor! ✅")
            return True
        else:
            print("Kayıt yapıldı ama kullanıcı adı eşleşmiyor! ❌")
            return False

    except Exception as e:
        print(f"Kayıt sırasında bir hata oluştu hocam: {e}")
        return False
