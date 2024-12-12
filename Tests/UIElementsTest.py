from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time

def test_sorting_functionality(driver,username):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()


    select = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
    select.select_by_value("lohi")

    prices = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
    prices = [float(price.text.replace("$", "")) for price in prices]

    return prices == sorted(prices)


def test_image_loading(driver,username):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    images = driver.find_elements(By.TAG_NAME, "img")
    all_images_loaded = all(img.get_attribute("src") for img in images)
    
    for backpack in images:
        if backpack.get_attribute("alt") == "Sauce Labs Backpack":
            return backpack.get_attribute("src") == "/static/media/sauce-backpack-1200x1500.0a0b85a3.jpg" and all_images_loaded

if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.maximize_window()
    if test_sorting_functionality(driver,"standard_user"):
        print("\033[92mTest Passed ✅\033[0m")
    else:
        print("\033[91mTest Failed ❌\033[0m")
    driver.quit()
    
    
    driver = webdriver.Chrome()
    driver.maximize_window()
    if test_image_loading(driver,"problem_user"):
        print("\033[92mTest Passed ✅\033[0m")
    else:
        print("\033[91mTest Failed ❌\033[0m")
