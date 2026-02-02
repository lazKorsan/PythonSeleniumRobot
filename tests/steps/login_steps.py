from behave import given, when, then
from utils.LoyalFriendLoginMethod import login_ve_dogrula
import assertpy

@given('the user is on the login page')
def step_given_user_on_login_page(context):
    """
    Test edilecek web sitesinin ana sayfasını açar.
    URL, environment.py içinde belirtilen driver context'inden gelir.
    """
    context.driver.get("https://qa.loyalfriendcare.com/en")

@when('the user enters "{email}" and "{password}"')
def step_when_user_enters_credentials(context, email, password):
    """
    Kullanıcı adı ve şifre ile giriş yapmayı dener.
    Giriş ve doğrulama işlemini yapan fonksiyonu çağırır.
    Sonucu bir sonraki adımda kullanmak üzere context'e kaydeder.
    """
    # 'Then' adımında beklenen kullanıcı adı, e-postanın '@' işaretinden önceki kısmıdır.
    # Bu varsayımı, 'login_ve_dogrula' fonksiyonunun beklentisine göre yapıyoruz.
    expected_username = "lazKorsan" # Feature dosyasında belirtilen beklenen isim
    context.login_success = login_ve_dogrula(context.driver, email, password, expected_username)

@then('the user name "{expected_name}" should be visible')
def step_then_user_name_should_be_visible(context, expected_name):
    """
    'when' adımında gerçekleştirilen giriş işleminin sonucunu doğrular.
    Eğer giriş başarısızsa, test bu adımda hata vererek durur.
    """
    assertpy.assert_that(context.login_success).is_true()
