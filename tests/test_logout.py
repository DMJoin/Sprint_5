from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import *

class TestLogout:

    def test_logout(self, driver):
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Button.REGISTRATION_BUTTON))
        driver.find_element(*Button.REGISTRATION_BUTTON).click()
        driver.find_element(*AuthPage.EMAIL_INPUT).send_keys('test_user303@gmail.com')    
        driver.find_element(*AuthPage.PASSWORD_INPUT).send_keys('Qwerty456')
        driver.find_element(*Button.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(AuthPage.PROFILE_NAME))
        driver.find_element(*Button.LOGOUT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Button.REGISTRATION_BUTTON))
        # Проверить: произошёл переход на главную страницу, 
        user_name = driver.find_elements(*AuthPage.PROFILE_NAME)
        user_avatar = driver.find_elements(*AuthPage.PROFILE_AVATAR)
        login_button = driver.find_element(*Button.REGISTRATION_BUTTON)
        assert len(user_name) == 0
        assert len(user_avatar) == 0
        assert login_button.is_displayed()