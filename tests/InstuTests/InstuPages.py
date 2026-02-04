from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InstuPages:
    """InstuLearn sayfa elementleri"""
    
    driver = None
    
    # ====== LOCATOR'LAR ======
    courses_Button = (By.XPATH, "//a[.//span[normalize-space()='Courses']]")
    new_webinar_button = (By.XPATH, "(//*[@href='/panel/webinars/new'])[3]")
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        print("Page object oluşturuldu")
    
    # ====== METHOD'LAR ======

   
    def click_coursesButton(self):
        """Courses butonuna tıklar, önce üzerine gelir ve highlight eder."""
        # Elementi bul ve tıklanabilir olana kadar bekle
        courses_element = self.wait.until(EC.element_to_be_clickable(self.courses_Button))
        
        # Elementi görüntü alanına kaydır (daha sağlam olması için)
        #self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", courses_element)
        
        # Elementi highlight et (kırmızı çerçeve)
        #self.driver.execute_script("arguments[0].style.border='3px solid red'", courses_element)
        
        # Hover işlemi için ActionChains kullan
        #ActionChains(self.driver).move_to_element(courses_element).perform()
        
        # Butona tıkla
        courses_element.click()
        print("Courses butonuna tıklandı")   

    def go_to_login_page(self):
        """Login sayfasına gider"""
        login_link_xpath = '//a[@href="/login" and contains(@class, "text-dark-blue")]'
        login_link = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, login_link_xpath))
        )
        login_link.click()
        print("Login sayfasına gidildi")

    def click_new_webinar_button(self):
        """New Webinar butonuna tıklar, önce üzerine gelir ve highlight eder."""
        try:
            # Elementi bul ve tıklanabilir olana kadar bekle
            webinar_button_element = self.wait.until(EC.element_to_be_clickable(self.new_webinar_button))
            
            # Elementi görüntü alanına kaydır
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", webinar_button_element)
            
            # Elementi highlight et (kırmızı çerçeve)
            self.driver.execute_script("arguments[0].style.border='3px solid red'", webinar_button_element)
            
            # Hover işlemi için ActionChains kullan
            ActionChains(self.driver).move_to_element(webinar_button_element).perform()
            
            # Butona tıkla
            webinar_button_element.click()
            print("New Webinar butonuna tıklandı (standart metot ile).")
        except Exception as e:
            print(f"Standart tıklama başarısız oldu: {e}. JavaScript ile tıklama denenecek.")
            try:
                # JavaScript ile tıklamayı dene
                webinar_button_element = self.wait.until(EC.presence_of_element_located(self.new_webinar_button))
                self.driver.execute_script("arguments[0].click();", webinar_button_element)
                print("New Webinar butonuna tıklandı (JavaScript ile).")
            except Exception as e2:
                print(f"JavaScript ile tıklama da başarısız oldu: {e2}")
                raise