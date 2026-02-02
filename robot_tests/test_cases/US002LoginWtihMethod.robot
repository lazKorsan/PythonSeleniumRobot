*** Settings ***
Library     SeleniumLibrary
# Resource dosyasını kütüphane gibi içe aktarıyoruz
Resource    loginMethod.resource

*** Variables ***
${URL}         https://qa.loyalfriendcare.com/en
${BROWSER}     chrome

*** Test Cases ***
Scenario 1: Valid Login Test
    [Setup]    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window

    # İŞTE O MEŞHUR ÇAĞIRMA ANI:
    # Metoda ihtiyacı olan 3 bilgiyi (arguments) gönderiyoruz.
    Loyal Friend Login Method    lazKorsan20220262058@gmail.com    Query.2026    lazKorsan

    [Teardown]    Close Browser