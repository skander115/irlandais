from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time


def login_test(username):
    try:
        # Setup
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")

        # Test Steps
        driver.find_element(By.ID, "user-name").send_keys(username)
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # Validation
        if "inventory.html" in driver.current_url:
            return True
        else:
            return False
    except Exception as e:
        return False
    finally:
        driver.quit()
        
def test_remove_from_cart(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    
    driver.find_element(By.ID, "login-button").click()
    driver.find_element(By.CSS_SELECTOR, "button[name*='add-to-cart-sauce-labs-backpack']").click()

    try:
        remove_button = driver.find_element(By.CSS_SELECTOR, "button[name*='remove-sauce-labs-backpack']")
        remove_button.click()
        time.sleep(1)
        removed = not driver.find_elements(By.CSS_SELECTOR, "button[name*='remove-sauce-labs-backpack']")
    except Exception:
        removed = False

    return removed

        
        
if __name__ == "__main__":
    usernames = ["standard_user", "locked_out_user", "problem_user", "performance_glitch_user", "invalid_user"]
    for username in usernames:
        if login_test(username):
            print(f"\033[92mTest Passed for {username} ✅\033[0m")
        else:
            print(f"\033[91mTest Failed for {username} ❌\033[0m")
    driver = webdriver.Chrome()
    driver.maximize_window()
    if test_remove_from_cart(driver):
        print("\033[92mTest Passed ✅\033[0m")
    else:
        print("\033[91mTest Failed ❌\033[0m")
