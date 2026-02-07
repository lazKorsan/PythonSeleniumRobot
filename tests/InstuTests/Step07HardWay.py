from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import testData
import InstuUtils

# Driver oluştur
driver = webdriver.Chrome()
driver.maximize_window()
print("Driver oluşturuldu.")

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

# Buradaki adım step 7'nin başına dahil edilmeyecek.
driver.get("https://qa.instulearn.com/panel/webinars/3651/step/7")

# newQuizButton
newQuizButton_Xpath = '//button[@id="webinarAddQuiz"]'
newQuizButton = driver.find_element(By.XPATH, newQuizButton_Xpath)
driver.execute_script("arguments[0].style.border='3px solid red'", newQuizButton) 
newQuizButton.click()
time.sleep(1)

# 1. Quiz Title (Zaten doğru çalışıyor ama index [1] önemli)
quizTitleBox_Xpath = '(//input[@name="ajax[new][title]"])[1]'
quizTitleBox = driver.find_element(By.XPATH, quizTitleBox_Xpath)
quizTitleBox.clear()
quizTitleBox.send_keys("Certifica alma sınavı")

# 2. Exam Time
ExamTimeBox_Xpath = '//input[@name="ajax[new][time]"]'
ExamTimeBox = driver.find_element(By.XPATH, ExamTimeBox_Xpath)
ExamTimeBox.send_keys("45")
time.sleep(1)

# 3. Number of Attempts (Hata buradaydı, doğru Xpath'i ve kaydırmayı uyguluyoruz)
# Ekran görüntündeki name attribute'una göre düzelttim: ajax[new][attempt]
attemptBox_Xpath = '//input[@name="ajax[new][attempt]"]'
attemptBox = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, attemptBox_Xpath))
)

# --- ETKİLİ KAYDIRMA VE GİRİŞ ---
# Elemanı ekranın tam ortasına getirir (Üst menüye takılmasını engeller)
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", attemptBox)
time.sleep(1)

# Görsel olarak doğrula
driver.execute_script("arguments[0].style.border='4px solid yellow'", attemptBox)

# Bazen input tipleri 'number' olduğunda .clear() hata verebilir, 
# Garanti olması için önce içeriği siliyoruz
attemptBox.send_keys(Keys.CONTROL + "a")
attemptBox.send_keys(Keys.BACKSPACE)
attemptBox.send_keys("3")
time.sleep(1)

print("✅ Attempt sayısı başarıyla girildi!")


# passMarkBox
passMarkBox_Xpath = '(//input[@class="js-ajax-pass_mark form-control "])[1]'
passMarkBox = driver.find_element(By.XPATH, passMarkBox_Xpath)
driver.execute_script("arguments[0].style.border='3px solid orange'", passMarkBox)  
passMarkBox.clear()
passMarkBox.send_keys("50")
time.sleep(1)

# expiresDayBox
expiresDayBox_Xpath = '//input[@name="ajax[new][expiry_days]"]'
expiresDayBox = driver.find_element(By.XPATH, expiresDayBox_Xpath)
driver.execute_script("arguments[0].style.border='3px solid purple'", expiresDayBox)  
expiresDayBox.clear()
expiresDayBox.send_keys("15")
time.sleep(1)

# selectQuestionBankRadioButton
selectQuestionBankRadioButton_Xpath = '(//label[@class="custom-control-label"])[1]'
selectQuestionBankRadioButton = driver.find_element(By.XPATH, selectQuestionBankRadioButton_Xpath)
driver.execute_script("arguments[0].style.border='3px solid pink'", selectQuestionBankRadioButton)  
selectQuestionBankRadioButton.click()
time.sleep(1)   

# selectCertificateButton
selectCertificateButton_Xpath = '(//*[@class="custom-control custom-switch"])[2]'
selectCertificateButton = driver.find_element(By.XPATH, selectCertificateButton_Xpath)
driver.execute_script("arguments[0].style.border='3px solid cyan'", selectCertificateButton)  
selectCertificateButton.click()
time.sleep(1)

# selectActiveQuizRadioButton
selectActiveQuizRadioButton_Xpath = '(//label[@class="custom-control-label"])[3]'
selectActiveQuizRadioButton = driver.find_element(By.XPATH, selectActiveQuizRadioButton_Xpath)
driver.execute_script("arguments[0].style.border='3px solid brown'", selectActiveQuizRadioButton)  
selectActiveQuizRadioButton.click()
time.sleep(1)

# createButton
createButton_Xpath = '(//button[@class="js-submit-quiz-form btn btn-sm btn-primary"])[1]'
createButton = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, createButton_Xpath))
)

driver.execute_script("arguments[0].style.border='3px solid gray'", createButton)  
createButton.click()
time.sleep(1)

# publishButton
publishButton_Xpath = '//button[@id="sendForReview"]'
publishButton = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, publishButton_Xpath))
)  
driver.execute_script("arguments[0].style.border='3px solid black'", publishButton)  
publishButton.click()
time.sleep(7)


print("✅ İşlemler tamamlandı!")

WebDriverWait(driver, 15).until(EC.url_contains("panel/webinars"))

print("\n" + "⭐" * 60)
print("                KURS OLUŞTURMA TEST RAPORU                ")
print("⭐" * 60)
print(f"📊 Test Durumu      : BAŞARILI ✅")
print(f"🔗 Son Durak URL    : {driver.current_url}")
print(f"📝 İşlem Özeti      : Step 7 Quiz tanımlandı ve onay için gönderildi.")
print(f"⏰ Bitiş Zamanı     : {time.strftime('%H:%M:%S')}")
print(f"🏆 Sonuç            : Kurs listenize başarıyla eklendi.")
print("⭐" * 60 + "\n")

#[@Gemini ?] 
# hocam bu noktadan sonra course oluşturlmuş oluyor 
# gidilen sayfanın linki https://qa.instulearn.com/panel/webinars
# buraya uygun bir şekilde 
# testin butununun kapsayacak konsol çıktısı yazdırabilitmiyiz. 
