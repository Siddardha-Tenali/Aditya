import time
from pynput.keyboard import Controller, Key
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


'''  Active Users  '''
def active_user(driver):
    time.sleep(2)
    wait = WebDriverWait(driver, 30)  # Set an explicit wait time
    wait.until(ec.element_to_be_clickable((By.XPATH, "//h2[normalize-space()='Active Users']"))).click()

    # Downloading All Active User Data
    wait = WebDriverWait(driver, 30)  # Set an explicit wait time
    wait.until(ec.invisibility_of_element_located((By.CLASS_NAME, "loader")))
    wait.until(ec.element_to_be_clickable((By.XPATH, "//div[@class='department-wise-download-button']"))).click()

    # Department wise Users
    # Computer Science and Engineering
    wait = WebDriverWait(driver, 30)  # Set an explicit wait time
    wait.until(ec.invisibility_of_element_located((By.CLASS_NAME, "loader")))
    wait.until(ec.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Computer Science and Engineering']"))).click()

    # Petroleum Technology
    driver.find_element(By.XPATH, "//span[normalize-space()='Petroleum Technology']").click()
    time.sleep(1)

    # # Artificial Intelligence & Machine Learning
    # driver.find_element(By.XPATH, "((//div[@class='d-flex justify-content-between align-items-center'])[3])").click()
    #
    # # Civil Engineering
    # driver.find_element(By.XPATH, "((//div[@class='d-flex justify-content-between align-items-center'])[4])").click()
    #
    # # iQuadra
    # driver.find_element(By.XPATH, "((//div[@class='d-flex justify-content-between align-items-center'])[5])").click()
    #
    # # Electronics and Communication Engineering
    # driver.find_element(By.XPATH, "((//div[@class='d-flex justify-content-between align-items-center'])[6])").click()
    #
    # # Electrical and Electronics Engineering
    # driver.find_element(By.XPATH, "//span[normalize-space()='Electrical and Electronics Engineering']").click()

    # Mechanical Engineering
    driver.find_element(By.XPATH, "//span[normalize-space()='Mechanical Engineering']").click()
    time.sleep(1)

    # Computer Science and Engineering
    driver.find_element(By.XPATH,  "//span[normalize-space()='Computer Science and Engineering']").click()
    time.sleep(1)

    # Search bar
    wait = WebDriverWait(driver, 5)
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "input[type='search']"))).send_keys('indu')

    # view Interviews
    keyboard = Controller()
    keyboard.press(Key.page_down)
    time.sleep(5)
    wait = WebDriverWait(driver, 60)
    wait.until(ec.element_to_be_clickable((By.XPATH, "//tbody/tr[1]/td[6]/button[1]"))).click()
    time.sleep(10)

    # Download resume
    wait = WebDriverWait(driver, 30)
    wait.until(ec.element_to_be_clickable((By.XPATH, "(//div[contains(@class,'nbkr-interview-card-col-small')]"
                                                         "[normalize-space()='Download Resume'])[1]"))).click()
    time.sleep(2)
    # pyautogui.hotkey('alt', 'f4')
    driver.switch_to.window(driver.window_handles[0])

    #  View Self Introduction
    wait = WebDriverWait(driver, 10)
    wait.until(ec.element_to_be_clickable((By.XPATH, "//div[contains(@class,'nbkr-interview-card-col-small')]"
                                                        "[normalize-space()='View SelfIntroduction']"))).click()
    time.sleep(5)

    # View Technical Interview
    wait = WebDriverWait(driver, 10)
    wait.until(ec.element_to_be_clickable((By.XPATH, "//div[contains(@class,'nbkr-interviews-wraper')]"
                                                        "//div[6]//div[2]"))).click()
    time.sleep(5)
    # switch to current page
    driver.switch_to.window(driver.window_handles[0])

    # search bar
    wait = WebDriverWait(driver, 10)
    wait.until(ec.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']"))).send_keys("dec 10")
    time.sleep(2)
