import time
import pyautogui
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


def test_my_iq(driver):
    wait = WebDriverWait(driver, 60)
    wait.until(ec.element_to_be_clickable((By.XPATH, "//p[@class='page-test-my-iq-text-button']"))).click()

    # Start Test
    wait = WebDriverWait(driver, 60)
    wait.until(ec.element_to_be_clickable((By.XPATH, "//button[normalize-space()='START TEST']"))).click()
    time.sleep(2)
    pyautogui.press("enter")

    # Selecting 1st option as Answer
    wait = WebDriverWait(driver, 60)
    wait.until(
        ec.element_to_be_clickable((By.XPATH, "//body/div[@id='root']/div[@class='App']/div[@class='container-fluid']"
                                              "/div[@class='row']/div[@class='attend_class_test_main_container"
                                              " container-fluid']/div[@class='attend-test-main']/div[@class='row']"
                                              "/div[@class='row']/div[@class='col-md-6']"
                                              "/div[@class='attend-test-options']/div[2]"))).click()
    time.sleep(1)
    # Mark for review
    driver.find_element(By.XPATH, "//button[normalize-space()='Mark for Review']").click()

    # Next button
    for _ in range(19):
        wait = WebDriverWait(driver, 60)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Next']"))).click()

    driver.find_element(By.XPATH, "//div[@class='attend-test-finishtest-btn']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//button[normalize-space()='Yes']").click()
    time.sleep(4)

    """ My IQ Test """
    # My IQ Test
    wait = WebDriverWait(driver, 60)
    wait.until(ec.element_to_be_clickable((By.XPATH, "//div[normalize-space()='My IQ Test']"))).click()
    time.sleep(2)

    # search
    driver.find_element(By.XPATH, "//input[@placeholder='Search by date, time taken, or score']").send_keys("2024-12-05")
    time.sleep(2)

    # Sorting Method
    driver.find_element(By.XPATH, "//div[@class='select-wrapper']//select").click()
    driver.find_element(By.XPATH, "//option[@value='test_date-desc']").click()
    time.sleep(4)

    # View Test
    driver.find_element(By.XPATH, "(//p[contains(text(),'View Test')])[1]").click()
    time.sleep(4)

    # Scroll down to see questions
    driver.find_element(By.XPATH, "//div[@class='questions-section']").click()
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'end')
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'home')
    time.sleep(1)

    # return to interviews
    driver.find_element(By.XPATH, "//a[@id='navigation-bar-2']").click()
    time.sleep(2)

    # home
    driver.find_element(By.XPATH, "(//a[normalize-space()='Home'])[1]").click()
    time.sleep(2)
