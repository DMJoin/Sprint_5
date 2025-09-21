from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import *

class TestLogin:

    def test_login(self, driver):
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Button.REGISTRATION_BUTTON))
        driver.find_element(*Button.REGISTRATION_BUTTON).click()
        driver.find_element(*AuthPage.EMAIL_INPUT).send_keys('test_user304@gmail.com')     
        driver.find_element(*AuthPage.PASSWORD_INPUT).send_keys('Qwerty456')
        driver.find_element(*Button.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(AuthPage.PROFILE_NAME))
        user_name = driver.find_element(*AuthPage.PROFILE_NAME)
        user_avatar = driver.find_element(*AuthPage.PROFILE_AVATAR)
        assert user_name.is_displayed()
        assert user_avatar.is_displayed()