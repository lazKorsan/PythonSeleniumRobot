*** Settings ***
Library    SeleniumLibrary
Library    String
Library    DateTime

*** Variables ***
${URL}                  https://qa.loyalfriendcare.com/en
${BROWSER}              chrome
${USER_NAME}            lazKorsan
${PASSWORD}             Query.2026
${SIGN_IN_XPATH}        (//*[@class="btn_add"])[2]
${NAME_INPUT}           //input[@id="name"]
${EMAIL_INPUT}          //input[@id="email"]
${PASS_INPUT}           //input[@id="password"]
${CONFIRM_PASS_INPUT}   //input[@id="password-confirm"]
${SIGN_UP_BTN}          //button[@class="btn btn-primary btn-cons m-t-10"]
${DASHBOARD_USER}       //a[@class='btn_add']

*** Test Cases ***
Dynamic Registration And Username Verification Test
    [Setup]    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window

    # 1. Kayıt Sayfasına Git
    Wait Until Element Is Visible    ${SIGN_IN_XPATH}    10s
    Click Element    ${SIGN_IN_XPATH}
    Sleep    2s

    # 2. Kullanıcı Adını Yaz
    Input Text    ${NAME_INPUT}    ${USER_NAME}

    # 3. Dinamik Email Üret (Python'daki time.time() mantığı)
    ${timestamp}=    Evaluate    int(time.time())    modules=time
    ${DYNAMIC_EMAIL}=    Set Variable    ${USER_NAME}${timestamp}@gmail.com
    Log To Console    \nÜretilen Email: ${DYNAMIC_EMAIL}
    
    Input Text    ${EMAIL_INPUT}    ${DYNAMIC_EMAIL}
    Sleep    1s

    # 4. Şifreleri Doldur
    Input Text    ${PASS_INPUT}    ${PASSWORD}
    Input Text    ${CONFIRM_PASS_INPUT}    ${PASSWORD}
    Sleep    1s

    # 5. Kayıt Ol Butonuna Tıkla
    Click Element    ${SIGN_UP_BTN}
    
    # Sayfanın yüklenmesi için bekle
    Wait Until Element Is Visible    ${DASHBOARD_USER}    15s

    # 6. Kullanıcı İsmini Doğrula ve Şiiri Oku
    ${raw_text}=    Get Text    ${DASHBOARD_USER}
    ${gercek_isim}=    Strip String    ${raw_text}

    Log To Console    \n--- İKON AYIKLAMA KISMI ---
    Log To Console    Aranan kahraman: ${USER_NAME}
    Log To Console    Bulunan cengaver: ${gercek_isim}

    Run Keyword If    '${gercek_isim}' == '${USER_NAME}'    Basarili Siiri
    ...    ELSE    Basarisiz Siiri

    # Teknik Doğrulama
    Should Be Equal As Strings    ${gercek_isim}    ${USER_NAME}

    [Teardown]    Close Browser

*** Keywords ***
Basarili Siiri
    Log To Console    \nAyarlar çarkı döndü, isim doğru takıldı,
    Log To Console    Testin meşalesi, gururla yakıldı! ✅

Basarisiz Siiri
    Log To Console    \nEyvah! Çarklar karıştı, isimler uymadı,
    Log To Console    Sistem bu hatayı, asla duymadı... ❌