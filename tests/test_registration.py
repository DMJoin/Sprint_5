from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import *

class TestRegistration:

    def test_succes_registration_user(self, driver, generate_email):
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Button.REGISTRATION_BUTTON))
        driver.find_element(*Button.REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Button.NO_ACCOUNT_BUTTON))
        driver.find_element(*Button.NO_ACCOUNT_BUTTON).click() 
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(AuthPage.EMAIL_INPUT))
        driver.find_element(*AuthPage.EMAIL_INPUT).send_keys(generate_email)
        driver.find_element(*AuthPage.PASSWORD_INPUT).send_keys('qwerty123')
        driver.find_element(*AuthPage.PASSWORD_CONFIRM_INPUT).send_keys('qwerty123')
        driver.find_element(*Button.CREATE_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(AuthPage.PROFILE_NAME))
        user_name = driver.find_element(*AuthPage.PROFILE_NAME)
        user_avatar = driver.find_element(*AuthPage.PROFILE_AVATAR)
        assert user_name.is_displayed()
        assert user_avatar.is_displayed() 

    def test_registration_existing_user(self, driver):
       WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Button.REGISTRATION_BUTTON))
       driver.find_element(*Button.REGISTRATION_BUTTON).click()
       WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Button.NO_ACCOUNT_BUTTON))
       driver.find_element(*Button.NO_ACCOUNT_BUTTON).click() 
       WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(AuthPage.EMAIL_INPUT))
       driver.find_element(*AuthPage.EMAIL_INPUT).send_keys('test_user304@gmail.com')
       driver.find_element(*AuthPage.PASSWORD_INPUT).send_keys('Qwerty456')
       driver.find_element(*AuthPage.PASSWORD_CONFIRM_INPUT).send_keys('Qwerty456')
       driver.find_element(*Button.CREATE_ACCOUNT_BUTTON).click()
       WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(AuthPage.POPUP_ERROR_FIELD))
       popup_registration_user = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(AuthPage.POPUP_AUTHORIZED_ERROR))
       assert popup_registration_user.text == "Ошибка" 

    def test_wrong_registration_user(self, driver, wrong_generate_email):
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Button.REGISTRATION_BUTTON))
        driver.find_element(*Button.REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Button.NO_ACCOUNT_BUTTON))
        driver.find_element(*Button.NO_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(AuthPage.EMAIL_INPUT))
        driver.find_element(*AuthPage.EMAIL_INPUT).send_keys(wrong_generate_email)
        driver.find_element(*AuthPage.PASSWORD_INPUT).send_keys('Qwerty456')
        driver.find_element(*AuthPage.PASSWORD_CONFIRM_INPUT).send_keys('Qwerty456')
        driver.find_element(*Button.CREATE_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(AuthPage.POPUP_ERROR_FIELD))
        popup_registration_user = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(AuthPage.POPUP_AUTHORIZED_ERROR))
        assert popup_registration_user.text == "Ошибка"



  

