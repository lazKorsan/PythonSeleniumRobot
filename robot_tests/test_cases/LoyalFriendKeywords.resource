*** Settings ***
Library    SeleniumLibrary
Library    String

*** Keywords ***
# --- GİRİŞ YAPMA METODU ---
Loyal Friend Login Method
    [Arguments]    ${email}    ${password}    ${expected_user}
    
    # Giriş linkine tıkla
    Wait Until Element Is Visible    //*[@id="top_menu"]/li[1]/a    10s
    Click Element    //*[@id="top_menu"]/li[1]/a
    Sleep    2s

    # Bilgileri doldur
    Press Keys    None    ${email}    TAB    ${password}    ENTER
    Sleep    3s

    # Kullanıcı ismini doğrula
    Verify User Name And Print Poetry    ${expected_user}

# --- KAYIT OLMA METODU (DİNAMİK) ---
Loyal Friend Register Method
    [Arguments]    ${user_name}    ${password}
    
    # Kayıt/Sign In sayfasına git (2. buton)
    Wait Until Element Is Visible    (//*[@class="btn_add"])[2]    10s
    Click Element    (//*[@class="btn_add"])[2]
    Sleep    2s

    # Kullanıcı Adı
    Input Text    //input[@id="name"]    ${user_name}

    # Dinamik Email Üret (Java/Python'daki time.time mantığı)
    ${timestamp}=    Evaluate    int(time.time())    modules=time
    ${dynamic_email}=    Set Variable    ${user_name}${timestamp}@gmail.com
    Input Text    //input[@id="email"]    ${dynamic_email}
    Log To Console    \nÜretilen Dinamik Email: ${dynamic_email}

    # Şifreler
    Input Text    //input[@id="password"]    ${password}
    Input Text    //input[@id="password-confirm"]    ${password}
    Sleep    1s

    # Kayıt Ol Butonu
    Click Element    //button[@class="btn btn-primary btn-cons m-t-10"]
    Sleep    3s

    # Kullanıcı ismini doğrula
    Verify User Name And Print Poetry    ${user_name}

# --- ORTAK DOĞRULAMA VE ŞİİR METODU ---
Verify User Name And Print Poetry
    [Arguments]    ${expected_name}
    
    Wait Until Element Is Visible    //a[@class='btn_add']    15s
    ${raw_text}=    Get Text    //a[@class='btn_add']
    ${actual_name}=    Strip String    ${raw_text}

    Log To Console    \n--- İKON AYIKLAMA VE TEST ŞİİRİ ---
    Log To Console    Aranan kahraman: ${expected_name}
    Log To Console    Bulunan cengaver: ${actual_name}

    IF    '${actual_name}' == '${expected_name}'
        Log To Console    Ayarlar çarkı döndü, isim doğru takıldı, ✅
        Log To Console    Testin meşalesi, gururla yakıldı!
    ELSE
        Log To Console    Eyvah! Çarklar karıştı, isimler uymadı, ❌
        Log To Console    Sistem bu hatayı, asla duymadı...
        Fail    Kullanıcı adı eşleşmedi! Beklenen: ${expected_name} Gelen: ${actual_name}
    END

    Should Be Equal As Strings    ${actual_name}    ${expected_name}