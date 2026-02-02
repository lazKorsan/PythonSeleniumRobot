*** Settings ***
Library    SeleniumLibrary
Library    String

*** Variables ***
${URL}                  https://qa.loyalfriendcare.com/en
${BROWSER}              chrome
${EMAIL}                lazKorsan20220262058@gmail.com
${PASSWORD}             Query.2026
${EXPECTED_USER}        lazKorsan
${LOGIN_LINK_XPATH}     //*[@id="top_menu"]/li[1]/a
${USER_BUTTON_XPATH}    //a[@class='btn_add']

*** Test Cases ***
Loyal Friend Login Test With Poetry
    [Setup]    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    
    # 1. Giriş Sayfasına Git
    Wait Until Element Is Visible    ${LOGIN_LINK_XPATH}    10s
    Click Element    ${LOGIN_LINK_XPATH}
    Sleep    2s

    # 2. Email Yaz, TAB'a Bas, Şifre Yaz, ENTER'a Bas
    # Robot Framework'te Press Keys, ActionChains'in işini çok daha kolay yapar
    Press Keys    None    ${EMAIL}    TAB    ${PASSWORD}    ENTER
    Sleep    3s

    # 3. Kullanıcı İsmini Al ve Ayıkla
    Wait Until Element Is Visible    ${USER_BUTTON_XPATH}    10s
    ${raw_text}=    Get Text    ${USER_BUTTON_XPATH}
    
    # Python'daki strip() işlemi gibi metni temizle
    ${actual_name}=    Strip String    ${raw_text}
    
    # 4. Şiirsel Raporlama
    Log To Console    \n--- İKON AYIKLAMA VE TEST ŞİİRİ ---
    Log To Console    Yanında bir çark vardı, dönüyordu durmadan,
    Log To Console    İsmi aldık oradan, ikona hiç vurmadan.
    Log To Console    Aranan kahraman: ${EXPECTED_USER}
    Log To Console    Bulunan cengaver: ${actual_name}

    # 5. Doğrulama (Assertion)
    Run Keyword If    '${actual_name}' == '${EXPECTED_USER}'    Login Basarili Siiri
    ...    ELSE    Login Basarisiz Siiri

    # Testi teknik olarak doğrula (Fail if not equal)
    Should Be Equal As Strings    ${actual_name}    ${EXPECTED_USER}
    
    [Teardown]    Close Browser

*** Keywords ***
Login Basarili Siiri
    Log To Console    \nAyarlar çarkı döndü, isim doğru takıldı,
    Log To Console    Testin meşalesi, gururla yakıldı! ✅

Login Basarisiz Siiri
    Log To Console    \nEyvah! Çarklar karıştı, isimler uymadı,
    Log To Console    Sistem bu hatayı, asla duymadı... ❌