import time
from pynput.keyboard import Controller, Key
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from attend_interview import interview
from test_my_iq import test_my_iq


# interview function calling
def my_interviews(driver,n):

    # attend interviews
    interview(driver, n)

    "View attended Interviews"
    # Searchbar
    time.sleep(5)
    (driver.find_element(By.XPATH, "//input[@placeholder='Search Job Role, Job Sector or Skills...']").send_keys
     ("Computer Science "))
    time.sleep(2)
    keyboard = Controller()
    keyboard.press(Key.down)
    wait = WebDriverWait(driver, 60)
    wait.until(ec.element_to_be_clickable((By.XPATH, "(//div[contains(@class,'all-interview-cards-hovering row')])[1]"))).click()
    time.sleep(4)

    # Downloading Resume
    wait = WebDriverWait(driver, 60)
    wait.until(ec.element_to_be_clickable((By.XPATH, "(//a[normalize-space()='Resume.pdf'])[1]"))).click()
    time.sleep(5)


    # Technical Interview
    wait = WebDriverWait(driver, 60)
    wait.until(ec.element_to_be_clickable((By.XPATH, "//div[contains(text(),'View Technical Interview')]"))).click()

    # AI Analysis
    wait = WebDriverWait(driver, 60)
    wait.until(ec.element_to_be_clickable((By.XPATH, "(//div[@id='metrics-card-ai-analysis'])[1]"))).click()
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(2)

    # interview page
    driver.find_element(By.XPATH, "(//a[normalize-space()='Interviews'])[1]").click()
    time.sleep(2)

    keyboard = Controller()
    keyboard.press(Key.page_down)
    time.sleep(2)
    wait = WebDriverWait(driver, 60)
    wait.until(ec.element_to_be_clickable((By.XPATH, "(//*[name()='path'])[11]"))).click()
    time.sleep(2)

    # to make active profile
    driver.find_element(By.XPATH, "//div[normalize-space()='Make this Profile Active']").click()
    time.sleep(8)

    # Archive
    wait = WebDriverWait(driver, 60)
    wait.until(ec.invisibility_of_element_located((By.CSS_SELECTOR, "div.loader")))
    wait.until(ec.visibility_of_element_located((By.XPATH, "(//*[name()='svg'][contains(@class,'dots-icon')])[2]")))
    wait.until(ec.element_to_be_clickable((By.XPATH, "(//*[name()='svg'][contains(@class,'dots-icon')])[2]"))).click()
    wait = WebDriverWait(driver, 60)
    wait.until(ec.element_to_be_clickable((By.XPATH, "//div[normalize-space()='Archive']"))).click()
    time.sleep(10)

    # Un archive
    keyboard = Controller()
    keyboard.press(Key.page_up)
    time.sleep(2)
    wait = WebDriverWait(driver, 60)
    wait.until(ec.visibility_of_element_located((By.XPATH, "(//button[@id='2'])[2]")))
    wait.until(ec.element_to_be_clickable((By.XPATH, "(//button[@id='2'])[2]"))).click()
    time.sleep(10)
    wait = WebDriverWait(driver, 60)
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[5]//div[7]//div[1]//*[name()='svg']")))
    wait.until(ec.element_to_be_clickable((By.XPATH, "//div[5]//div[7]//div[1]//*[name()='svg']"))).click()
    time.sleep(8)
    keyboard.press(Key.page_down)

    # Share
    time.sleep(2)
    wait = WebDriverWait(driver, 30)
    wait.until(ec.element_to_be_clickable((By.XPATH, "(//*[name()='svg'][contains(@class,'dots-icon')])[3]"))).click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//div[normalize-space()='Share']").click()
    driver.find_element(By.XPATH, "//input[@placeholder='Mail ID']").send_keys("siddardha.tenali@gmail.com")
    time.sleep(2)
    driver.find_element(By.XPATH, "(//div[@class='contact-text-input'])[1]").send_keys("hello")
    time.sleep(1)
    driver.find_element(By.XPATH, "//button[normalize-space()='Send Message']").click()
    time.sleep(5)
    driver.find_element(By.XPATH, "//button[normalize-space()='OK']").click()
    time.sleep(2)

    """ Active profile details """
    driver.find_element(By.XPATH, "(//div[@class='act-card row'])[1]").click()
    time.sleep(2)
    wait = WebDriverWait(driver, 60)
    wait.until(ec.element_to_be_clickable((By.XPATH, "(//a[normalize-space()='Resume.pdf'])[1]"))).click()
    time.sleep(2)
    wait = WebDriverWait(driver, 60)
    wait.until(ec.element_to_be_clickable((By.XPATH, "(//div[contains(text(),'View Technical Interview')])[1]"))).click()
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(2)

    # My Interviews
    wait = WebDriverWait(driver, 60)
    wait.until(ec.visibility_of_element_located((By.XPATH, "(//a[normalize-space()='Interviews'])[1]")))
    wait.until(ec.element_to_be_clickable((By.XPATH, "(//a[normalize-space()='Interviews'])[1]"))).click()

    # to share active interview (three dots)
    time.sleep(2)
    driver.find_element(By.XPATH, "(//*[name()='path'])[10]").click()
    driver.find_element(By.XPATH, "(//div[@class='dropdown-item'])[1]").click()
    time.sleep(1)
    keyboard = Controller()
    keyboard.press(Key.page_down)

    driver.find_element(By.XPATH, "//input[@placeholder='Mail ID']").send_keys("siddardha.tenali@gmail.com")
    time.sleep(1)
    driver.find_element(By.XPATH, "(//div[@class='contact-text-input'])[1]").send_keys("hello")
    time.sleep(1)
    driver.find_element(By.XPATH, "//button[normalize-space()='Send Message']").click()
    time.sleep(1)
    wait = WebDriverWait(driver, 30)
    wait.until(ec.element_to_be_clickable((By.XPATH, "//button[normalize-space()='OK']"))).click()
    time.sleep(1)
    keyboard.press(Key.page_up)
    time.sleep(5)

    """ Test My IQ """
    test_my_iq(driver)


