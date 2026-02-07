from behave import given, when, then
from selenium import webdriver
import time
import sys
import os

# Mevcut dosyanın (CreateCourseSteps.py) dizinini al
current_dir = os.path.dirname(os.path.abspath(__file__))
# Proje kök dizinini (Cucumber) al
project_root = os.path.dirname(current_dir)
# 'utils' klasörünün yolunu oluştur
utils_path = os.path.join(project_root, 'utils')
sys.path.append(utils_path)

import InstuUtils  
import testData     

@given('Kullanıcı tarayıcıyı açar')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()

@when('Kullanıcı siteye gider')
def step_impl(context):
    # Tablodan veriyi çekmek yerine testData'dan alıyoruz
    context.driver.get(testData.login_url) # [cite: 2]

@when('Kullanıcı giriş yapar')
def step_impl(context):
    InstuUtils.InstuLearnLoginMethod(context.driver, testData.mail, testData.password) # [cite: 3, 4, 5]

@when('Kullanıcı yeni kurs oluşturma sayfasına gider')
def step_impl(context):
    InstuUtils.navigateToNewCoursePage(context.driver) # [cite: 1]

@when('Kullanıcı temel bilgileri doldurur')
def step_impl(context):
    InstuUtils.step1(context.driver) # [cite: 1]

@when('Kullanıcı ek bilgileri doldurur')
def step_impl(context):
    # Feature dosyasındaki tablo verilerini kullanıyoruz
    row = context.table[0]
    InstuUtils.step2(
        context.driver, 
        capacity=row['Kapasite'], # 
        duration=row['Süre'],      # [cite: 8]
        tags=row['Etiketler'],     # [cite: 9]
        category_value=row['Kategori'] # [cite: 11]
    )

@when('Kullanıcı fiyatlandırma bilgilerini doldurur')
def step_impl(context):
    row = context.table[0]
    InstuUtils.step3(context.driver, access_days=row['Erişim Günleri'], price=row['Fiyat']) # [cite: 12, 13, 15]

@when('Kullanıcı yeni bölüm bilgilerini doldurur')
def step_impl(context):
    row = context.table[0]
    InstuUtils.step4(context.driver, title_text=row['Bölüm Başlığı']) # [cite: 16, 17]

@when('Kullanıcı ön koşul bilgilerini doldurur')
def step_impl(context):
    row = context.table[0]
    InstuUtils.step5(context.driver, search_text=row['Arama Metni']) # [cite: 18]

@when('Kullanıcı sıkça sorulan sorulara cevap verir')
def step_impl(context):
    row = context.table[0]
    # Daha önce yazdığımız step6 metodunu çağırıyoruz
    InstuUtils.step6(context.driver, faq_question=row['Soru'], faq_answer=row['Cevap']) # [cite: 19, 20, 22]

@when('Kullanıcı kurs sonunda yapılacak sınav hakkında bilgi verir')
def step_impl(context):
    row = context.table[0]
    # Yeni yazdığımız step7 metodunu çağırıyoruz
    InstuUtils.step7(
        context.driver, 
        quiz_title=row['Sınav Başlığı'], # [cite: 24]
        exam_time=row['Sınav Süresi'],   # [cite: 25]
        attempt_count=row['Deneme Sayısı'] # [cite: 26]
    )

@then('Kursun başarıyla oluşturulduğu doğrulanır')
def step_impl(context):
    assert "panel/webinars" in context.driver.current_url
    print("✅ BDD Testi Başarıyla Tamamlandı!")
    context.driver.quit()