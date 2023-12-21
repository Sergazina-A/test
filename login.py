from selenium.webdriver.support import expected_conditions as EC
import time


def perform_login(driver, wait, locators):
    wait.until(EC.element_to_be_clickable(locators['login/registration'])).click()
    wait.until(EC.element_to_be_clickable(locators['login_text_editor2'])).click()
    wait.until(EC.element_to_be_clickable(locators['login_text_editor2'])).send_keys("7774186025")
    driver.execute_script('mobile: performEditorAction', {'action': 'search'})
    wait.until(EC.element_to_be_clickable(locators['pass_text_editor'])).click()
    wait.until(EC.element_to_be_clickable(locators['pass_text_editor'])).send_keys("test12345")
    # driver.execute_script('mobile: performEditorAction', {'action': 'search'})
    wait.until(EC.element_to_be_clickable(locators['login_button'])).click()
    time.sleep(2)