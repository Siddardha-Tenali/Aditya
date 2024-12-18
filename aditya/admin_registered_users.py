import time
import pyautogui
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


def registered_users(driver):
    """ Registered Users """
    driver.find_element(By.CSS_SELECTOR, "h2[class='user_count_card_header']").click()

    # Search Bar
    driver.find_element(By.CSS_SELECTOR, ".AdminPanel-searchbar").send_keys("ind")

    # View All Interview of searched candidate.
    wait = WebDriverWait(driver, 15)
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "button[class='nbkr-admin-student-profile-interview"
                                                            "-button']"))).click()
    # Student Profile Navigation Bar
    wait = WebDriverWait(driver, 30)
    # Wait until the loader is no longer visible
    wait.until(ec.invisibility_of_element_located((By.CSS_SELECTOR, "div.loader")))
    driver.find_element(By.ID, "navigation-bar-1").click()

    # information icon
    action = ActionChains(driver)
    action.move_to_element(driver.find_element(By.CSS_SELECTOR, "div[class='register_infoicon']")).perform()

    # Student Registration Upload Label
    wait = WebDriverWait(driver, 30)
    wait.until(ec.invisibility_of_element_located((By.CSS_SELECTOR, "div.loader")))
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "label[class='upload-label']"))).click()

    # uploading  Student details excel ...
    wait = WebDriverWait(driver, 30)
    wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, "input[id ='open-bulk-upload-file']"))
               ).send_keys('C:\\Users\\HP\\Downloads\\aditya.xlsx')
    time.sleep(1)

    # to close the opened folder window while uploading Excel file ...
    pyautogui.hotkey('alt', 'f4')

    wait = WebDriverWait(driver, 30)
    wait.until(ec.invisibility_of_element_located((By.CSS_SELECTOR, "div.loader")))

    # Sample Registration Excel Template
    wait.until(ec.element_to_be_clickable((By.XPATH, "//button[@id='download-template']//*[name()='svg']"))).click()
    time.sleep(1)

    # Filter by Department
    dropdown = Select(driver.find_element(By.NAME, "Filter by Department"))
    dropdown.select_by_visible_text("CSE")

    # Filter by College
    dropdown1 = Select(driver.find_elements(By.NAME, "Filter by Department")[1])
    dropdown1.select_by_visible_text("All Colleges")

    # Public Profiles
    wait = WebDriverWait(driver, 30)
    wait.until(ec.invisibility_of_element_located((By.CSS_SELECTOR, "div.loader")))
    wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, "div[id='click2']"))).click()

    # Sort Metrics
    Select(driver.find_element(By.CSS_SELECTOR, "select[name='Sort Metrics']")).select_by_visible_text("High - Low")
    time.sleep(1)

    # Filter by Departments
    dropdown3 = Select(driver.find_element(By.NAME, "Filter by Department"))
    dropdown3.select_by_visible_text("All Departments")
    time.sleep(1)

    # Filter By College
    dropdown4 = Select(driver.find_elements(By.NAME, "Filter by Department")[1])
    dropdown4.select_by_visible_text("All Colleges")
    time.sleep(1)

    # All Public Profile Data
    wait = WebDriverWait(driver, 20)
    wait.until(
        ec.element_to_be_clickable((By.CSS_SELECTOR, "div[class='public_profiles_download_report_button']"))).click()

    # Information icon
    action.move_to_element(driver.find_element(By.CSS_SELECTOR, "div[class='active_infoicon']")).perform()

    # Search Bar
    driver.find_element(By.CSS_SELECTOR, ".AdminPanel-searchbar1").send_keys("ind")

    # Download Resume of Searched Student
    wait = WebDriverWait(driver, 30)
    wait.until(ec.invisibility_of_element_located((By.CLASS_NAME, "loader")))
    wait.until(ec.element_to_be_clickable((By.XPATH, "//p[normalize-space()='Download Resume']"))).click()
    time.sleep(2)

    # Self Introduction
    wait = WebDriverWait(driver, 30)
    wait.until(ec.presence_of_element_located((By.XPATH, "//p[normalize-space()='Self Introduction']"))).click()
    time.sleep(5)
    driver.switch_to.window(driver.window_handles[0])

    # Technical Interview
    wait = WebDriverWait(driver, 30)
    wait.until(ec.element_to_be_clickable((By.ID, "admin-view-technical"))).click()
    time.sleep(5)
    # switch to current webpage
    driver.switch_to.window(driver.window_handles[0])

    # Profile Share icon
    wait = WebDriverWait(driver, 10)
    wait.until(ec.element_to_be_clickable((By.ID, "admin-share-profile"))).click()

    # PopUP copy the link Button
    wait = WebDriverWait(driver, 20)
    wait.until(ec.element_to_be_clickable((By.ID, "active-profile-share-popup-copy"))).click()

    # Popup Close Button
    driver.find_element(By.ID, "active-profile-share-popup-close").click()

    # Side Dashboard Icon
    wait = WebDriverWait(driver, 10)
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "div.SideBar_JS_Icon"))).click()
