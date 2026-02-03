from selenium import webdriver
import utils  # Az önce oluşturduğumuz dosyayı içe aktarıyoruz

# Tarayıcıyı hazırla
driver = webdriver.Chrome()
driver.get("https://qa.loyalfriendcare.com/en")

# İŞTE O MEŞHUR ÇAĞIRMA ANI:
utils.LoyalFriendLoginMethod(
    driver, 
    "lazKorsan20220262058@gmail.com", 
    "Query.2026", 
    "lazKorsan"
)

# Test bittikten sonra başka işler yapabilirsin...
print("Metot başarıyla çağrıldı ve çalıştı.")
# driver.quit()