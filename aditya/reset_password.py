import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

# Resetting password for student profile
def reset_password(driver, reset):
    if reset == "y":
        driver.find_element(By.XPATH, "//*[name()='path' and contains(@d,'M13 3a9 9 ')]").click()

        # Current Password
        wait = WebDriverWait(driver, 30)
        element1 = (wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "label[for='password-id']"))))
        actions = ActionChains(driver)
        actions.move_to_element(element1).click().send_keys("Aditya@1234").perform()
        time.sleep(2)

        # eye icon of current password
        driver.find_element(By.CSS_SELECTOR, "#reset-password-eye-icon-0").click()

        # New Password
        wait = WebDriverWait(driver, 30)
        wait.until(ec.presence_of_element_located((By.XPATH, "//input[@id='new-password-id']"))).send_keys(
            "Aditya@12345")
        # eye icon of current password
        driver.find_element(By.CSS_SELECTOR, "#reset-password-eye-icon-1").click()

        # Confirm Paasword
        wait = WebDriverWait(driver, 30)
        wait.until(ec.presence_of_element_located((By.XPATH, "//input[@id='cfm-password-id']"))).send_keys(
            "Aditya@12345")
        # eye icon of current password
        driver.find_element(By.CSS_SELECTOR, "#reset-password-eye-icon-2").click()
        time.sleep(1)

        # Update Password
        wait = WebDriverWait(driver, 60)
        wait.until(ec.presence_of_element_located((By.XPATH, "//button[@id='reset-password-submit']"))).click()
        time.sleep(20)

        """ Sign In Again"""
        driver.get("https://master.d3rqcznoic140q.amplifyapp.com/")
        time.sleep(1)
        # sign in button
        driver.find_element(By.XPATH, "//button[@class='home_get_started_button']").click()
        time.sleep(2)
        # email id
        driver.find_element(By.XPATH, "//input[@id='email-id']").send_keys("test333@test.com")
        time.sleep(2)
        # password
        driver.find_element(By.XPATH, "//input[@id='password-id']").send_keys("Aditya@12345")
        # submit button
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        # My Profile
        wait = WebDriverWait(driver, 30)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//div[@id='myprofile']//img[@class='Entity-Box-Img']"))).click()
        time.sleep(2)



