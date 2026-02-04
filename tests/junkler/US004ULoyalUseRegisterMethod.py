from selenium import webdriver
import utils  # utils.py dosyasını içe aktar

# 1. Tarayıcıyı Başlat
driver = webdriver.Chrome()
driver.maximize_window()

# 2. Kayıt Metodunu Çağır
# Not: Email'i metodun içinde kendisi ürettiği için buraya yazmıyoruz
basari_durumu = utils.LoyalFriendRegisterMethod(
    driver, 
    "lazKorsan", 
    "Query.2026", 
    "Query.2026"
)

# 3. Sonuca göre bir işlem yap
if basari_durumu:
    print("Test Geçti!")
else:
    print("Test Kaldı!")

# driver.quit()