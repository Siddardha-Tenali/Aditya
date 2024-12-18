import time
from pynput.keyboard import Controller, Key
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

""" Inactive users"""
def inactive_users(driver):
    wait = WebDriverWait(driver, 20)
    wait.until(ec.presence_of_element_located((By.XPATH, "//h2[normalize-space()='Inactive Users']"))).click()
    time.sleep(1)

    '''department wise inactive users'''
    # # iQuadra
    # driver.find_element(By.XPATH, "//span[normalize-space()='iQuadra']").click()

    # Computer Science and Engineering
    driver.find_element(By.XPATH, "//span[normalize-space()='Computer Science and Engineering']").click()
    time.sleep(2)

    # # Electronics and Communication Engineering
    # driver.find_element(By.XPATH, "//span[normalize-space()='Electronics and Communication Engineering']").click()
    #
    # # Electrical and Electronics Engineering
    # driver.find_element(By.XPATH, "//span[normalize-space()='Electrical and Electronics Engineering']").click()

    # Petroleum Technology
    driver.find_element(By.XPATH, "//span[normalize-space()='Petroleum Technology']").click()
    time.sleep(1)

    # Mechanical Engineering
    driver.find_element(By.XPATH, "//span[normalize-space()='Mechanical Engineering']").click()
    time.sleep(1)

    # # Artificial Intelligence & Machine Learning
    # driver.find_element(By.XPATH, "//span[normalize-space()='Artificial Intelligence & Machine Learning']").click()
    #
    # # Civil Engineering
    # driver.find_element(By.XPATH, "//span[normalize-space()='Civil Engineering']").click()

    # Downloading All Inactive User Data
    wait = WebDriverWait(driver, 10)
    wait.until(ec.element_to_be_clickable((By.XPATH, "//div[@class='department-wise-download-button']"))).click()
    time.sleep(5)

    # search bar in inactive users
    wait = WebDriverWait(driver, 10)
    wait.until(ec.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search...']"))).send_keys('student_1')
    time.sleep(1)
    keyboard = Controller()
    keyboard.press(Key.page_down)
    time.sleep(1)

    # Dashboard
    wait = WebDriverWait(driver, 30)
    wait.until(ec.invisibility_of_element_located((By.CSS_SELECTOR, ".loader")))
    wait = WebDriverWait(driver, 30)
    wait.until(ec.visibility_of_element_located((By.ID, "navigation-bar-1")))
    wait.until(ec.element_to_be_clickable((By.ID, "navigation-bar-1"))).click()
    time.sleep(4)
