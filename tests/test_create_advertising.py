from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import *


class TestCreateAdvertising:

    def test_create_advertising_not_authorized(self, driver):
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Button.REGISTRATION_BUTTON))
        driver.find_element(*Button.CREATE_ADVERTISING_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(AuthPage.POPUP_NOT_AUTHORIZED))
        popup_unautorized = driver.find_element(*AuthPage.POPUP_NOT_AUTHORIZED_MESSAGE)
        assert popup_unautorized.text == "Чтобы разместить объявление, авторизуйтесь" 

    def test_create_advertising_authorized(self, driver):
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Button.REGISTRATION_BUTTON))
        driver.find_element(*Button.REGISTRATION_BUTTON).click()
        driver.find_element(*AuthPage.EMAIL_INPUT).send_keys('test_user304@gmail.com')     
        driver.find_element(*AuthPage.PASSWORD_INPUT).send_keys('Qwerty456')
        driver.find_element(*Button.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(AuthPage.PROFILE_NAME))
        driver.find_element(*Button.CREATE_ADVERTISING_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(CreateAdvertising.PRODUCT_NAME))
        driver.find_element(*CreateAdvertising.PRODUCT_NAME).send_keys('Куплю лопату')
        driver.find_element(*CreateAdvertising.PRODUCT_DESCRIPTION).send_keys('Куплю лопату или только фотографию лопаты')
        driver.find_element(*CreateAdvertising.PRODUCT_COST).send_keys('1000')
        driver.find_element(*CreateAdvertising.DROPDOWN_CATEGORY).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(CreateAdvertising.SELECTED_CATEGORY))
        driver.find_element(*CreateAdvertising.SELECTED_CATEGORY).click()
        driver.find_element(*CreateAdvertising.DROPDOWN_CITY).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(CreateAdvertising.SELECTED_CITY))
        driver.find_element(*CreateAdvertising.SELECTED_CITY).click()
        driver.find_element(*Button.PUBLISH_ADVERTISING_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Elements.CARD))
        driver.find_element(*AuthPage.PROFILE_AVATAR).click()
        create_advertising = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Elements.MY_ADVERTISING))
        assert create_advertising.text == 'Куплю лопату'
        
