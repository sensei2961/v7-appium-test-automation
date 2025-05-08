import pytest
from appium.webdriver.common.appiumby import AppiumBy

def test_login(driver):
    username_field = driver.find_element(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTextField')
    password_field = driver.find_element(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSecureTextField[`value == "Password"`]')
    login_button = driver.find_element(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "Sign In"`]')

    username_field.clear()
    username_field.send_keys("maxxp02smoke")
    password_field.clear()
    password_field.send_keys("My123123")
    login_button.click()

    # Verify login success (replace with actual condition)
    success_element = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Tab Bar')
    assert success_element.is_displayed(), "Login failed or Dashboard not displayed"
