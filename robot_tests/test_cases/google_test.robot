*** Settings ***
Documentation     Google ana sayfasını açmak için basit bir test.
Library           SeleniumLibrary

*** Test Cases ***
Google Ana Sayfasi Basligini Dogrula
    [Documentation]    Google ana sayfasını açar ve başlığın doğru olduğunu doğrular.
    Open Browser    https://www.google.com    chrome
    Maximize Browser Window
    sleep  12s
    Title Should Be    Google
    Close Browser

*** Keywords ***
# Bu alana daha sonra kendi özel anahtar kelimelerinizi ekleyebilirsiniz. 
# robot robot_tests/test_cases/google_test.robot
