from selenium.webdriver.common.by import By

class Button:
    REGISTRATION_BUTTON = (By.XPATH, "//button[contains(text(), 'Вход и регистрация')]")
    NO_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(), 'Нет аккаунта')]")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(), 'Создать аккаунт')]")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выйти')]")
    CREATE_ADVERTISING_BUTTON = (By.XPATH, "//button[contains(text(), 'Разместить объявление')]")
    PUBLISH_ADVERTISING_BUTTON = (By.XPATH, "//button[contains(text(), 'Опубликовать')]")

class AuthPage:
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    PASSWORD_CONFIRM_INPUT = (By.NAME, "submitPassword")
    PROFILE_NAME = (By.XPATH, ".//h3[@class='profileText name']")
    PROFILE_AVATAR = (By.XPATH, ".//button[@class='circleSmall']")
    POPUP_NOT_AUTHORIZED = (By.CLASS_NAME, "popUp_shell__LuyqR")
    POPUP_NOT_AUTHORIZED_MESSAGE = (By.XPATH, "//h1[contains(text(), 'Чтобы разместить объявление, авторизуйтесь')]" )
    POPUP_AUTHORIZED_ERROR = (By.XPATH, "//span[@class = 'input_span__yWPqB' and text() = 'Ошибка']")
    POPUP_ERROR_FIELD = (By.CSS_SELECTOR, "div.input_inputError__fLUP9")
    
class Elements:
    CARD = (By.CLASS_NAME, 'card')
    MY_ADVERTISING = (By.XPATH, "//h2[contains(text(), 'Куплю лопату')]")

class CreateAdvertising:
    PRODUCT_NAME = (By.XPATH, '//input[@class = "input_inputStandart__JweLZ spanGlobal" and @placeholder = "Название"]')
    PRODUCT_DESCRIPTION = (By.XPATH, '//textarea[@class = "textarea_inputStandart__IoNxq spanGlobal"]')
    PRODUCT_COST = (By.XPATH, '//input[@class = "input_inputStandart__JweLZ spanGlobal" and @placeholder = "Стоимость"]')
    DROPDOWN_CATEGORY = (By.XPATH, "(//button[@class='dropDownMenu_arrowDown__pfGL1 dropDownMenu_noDefault__wSKsP'])[1]")
    DROPDOWN_CITY = (By.XPATH, "(//button[@class='dropDownMenu_arrowDown__pfGL1 dropDownMenu_noDefault__wSKsP'])[2]")
    SELECTED_CATEGORY = (By.XPATH, '//span[@class = "undefined dropDownMenu_textColor__Nyo8k" and text() = "Садоводство"]')
    SELECTED_CITY = (By.XPATH, '//span[@class = "undefined dropDownMenu_textColor__Nyo8k" and text() = "Москва"]')