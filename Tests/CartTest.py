from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time

def test_checkout_button_with_empty_cart(driver,username):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    checkout_button = driver.find_element(By.ID, "checkout")
    is_enabled = checkout_button.is_enabled()

    return not is_enabled

def test_checkout_form(driver,username):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    driver.find_element(By.CSS_SELECTOR, "button[name*='add-to-cart']").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    driver.find_element(By.ID, "checkout").click()

    driver.find_element(By.ID, "first-name").send_keys("John")
    driver.find_element(By.ID, "postal-code").send_keys("12345")
    driver.find_element(By.ID, "continue").click()

    return not ("checkout-step-two.html" in driver.current_url)

if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.maximize_window()
    if test_checkout_button_with_empty_cart(driver,"standard_user"):
        print("\033[92mTest Passed ✅\033[0m")
    else:
        print("\033[91mTest Failed ❌\033[0m")
    driver.quit()
    
    driver = webdriver.Chrome()
    driver.maximize_window()
    if test_checkout_form(driver,"visual_user"):
        print("\033[92mTest Passed ✅\033[0m")
    else:
        print("\033[91mTest Failed ❌\033[0m")