import time
from pynput.keyboard import Controller, Key
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from admin_active_users import active_user
from admin_inactive_users import inactive_users
from admin_registered_users import registered_users

driver = webdriver.Chrome()
driver.maximize_window()

""" Sign In """
driver.get("https://master.d3rqcznoic140q.amplifyapp.com/")
# sign in button
driver.find_element(By.CSS_SELECTOR, "button[class='header_button']").click()
# email id
driver.find_element(By.ID, "email-id").send_keys("admin_aditya@iquizuanswer.com")
# password
driver.find_element(By.ID, "password-id").send_keys("Aditya@000")
# submit button
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# Dashboard heading
wait = WebDriverWait(driver, 30)  # Set an explicit wait time
wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, ".admin_dashboard_main_heading")))
time.sleep(4)

""" Registered Users """
registered_users(driver)
time.sleep(1)

'''  Active Users  '''
active_user(driver)
time.sleep(0.5)

# Active_Inactive
driver.find_element(By.XPATH, "//a[@id='navigation-bar-1']").click()
time.sleep(2)

# inactive
driver.find_element(By.XPATH, "//div[normalize-space()='Inactive Users']").click()
time.sleep(1)
# active
driver.find_element(By.XPATH, "//div[normalize-space()='Active Users']").click()
time.sleep(1)

# dashboard
WebDriverWait(driver, 10)
wait.until(ec.element_to_be_clickable((By.XPATH, "//a[@id='navigation-bar-1']"))).click()
time.sleep(1)

""" Inactive users """
inactive_users(driver)

""" Side bar collapsed """
driver.find_element(By.XPATH, "(//*[name()='svg'][@class='collapsed-icon'])[1]").click()
time.sleep(1)
driver.find_element(By.XPATH, "(//*[name()='svg'][@class='collapsed-icon'])[1]").click()
time.sleep(2)

# Interview Statistics - Department-Wise Interview Participation
wait = WebDriverWait(driver, 30)
wait.until(ec.element_to_be_clickable((By.XPATH, "(//select[@aria-label='Department wise comparison select'])"))).click()

# weekly
driver.find_element(By.XPATH, "//option[@value='weekly']").click()
time.sleep(1)

# monthly
driver.find_element(By.XPATH, "//option[@value='monthly']").click()
time.sleep(1)

# quarterly
driver.find_element(By.XPATH, "//option[@value='quarterly']").click()
time.sleep(1)

# half_yearly
driver.find_element(By.XPATH, "//option[@value='half_yearly']").click()
time.sleep(1)

# yearly
driver.find_element(By.XPATH, "//option[@value='yearly']").click()
time.sleep(2)

# To Download All Interview Data
wait = WebDriverWait(driver, 15)
wait.until(ec.invisibility_of_element_located((By.CLASS_NAME, "loader")))
wait.until(ec.element_to_be_clickable((By.XPATH, "//div[@class='department-wise-download-button']"))).click()
driver.switch_to.window(driver.window_handles[0])

# My Account
wait = WebDriverWait(driver, 15)
wait.until(ec.invisibility_of_element_located((By.CSS_SELECTOR, "div.loader")))
wait.until(ec.element_to_be_clickable((By.XPATH, "//div[@title='My Account']//div[contains(@class,'SideBar_JS_Icon')]"
                                                 "//*[name()='svg']"))).click()
time.sleep(1)

# Bulk Registration
wait = WebDriverWait(driver, 15)
wait.until(ec.invisibility_of_element_located((By.CSS_SELECTOR, "div.loader")))
wait.until(ec.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Bulk Registration']"))).click()

# AI Interviews
time.sleep(1)
wait = WebDriverWait(driver, 15)
wait.until(ec.invisibility_of_element_located((By.CSS_SELECTOR, "div.loader")))
wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "button[id='feature-2'] span"))).click()

# Performance Metrics
wait = WebDriverWait(driver, 15)
wait.until(ec.invisibility_of_element_located((By.CSS_SELECTOR, "div.loader")))
wait.until(ec.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Performance Metrics']"))).click()

# AI Analysis
wait = WebDriverWait(driver, 15)
wait.until(ec.invisibility_of_element_located((By.CSS_SELECTOR, "div.loader")))
wait.until(ec.element_to_be_clickable((By.XPATH, "//span[normalize-space()='AI Analysis']"))).click()

# Admin Profile
wait = WebDriverWait(driver, 15)
wait.until(ec.invisibility_of_element_located((By.CSS_SELECTOR, "div.loader")))
wait.until(ec.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Admin Profile']"))).click()

# Share Interviews
wait = WebDriverWait(driver, 15)
wait.until(ec.invisibility_of_element_located((By.CSS_SELECTOR, "div.loader")))
keyboard = Controller()
keyboard.press(Key.page_down)
wait.until(ec.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Share Interviews']"))).click()

# Dashboard
keyboard.press(Key.page_down)
wait = WebDriverWait(driver, 15)
wait.until(ec.invisibility_of_element_located((By.CSS_SELECTOR, "div.loader")))
wait.until(ec.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Dashboard']"))).click()
# driver.execute_script("arguments[0].click();", element3)
time.sleep(2)

# website
driver.find_element(By.XPATH, "//h1[@id='website-link']").click()
time.sleep(5)
driver.switch_to.window(driver.window_handles[0])


""" Student Profile """
wait = WebDriverWait(driver, 15)
wait.until(ec.element_to_be_clickable((By.XPATH, "(//*[name()='svg'])[6]"))).click()
time.sleep(4)

# Dashboard
wait = WebDriverWait(driver, 15)
wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@title='Dashboard']//div[contains(@class,'SideBar_JS_Icon')]"
                                                         "//*[name()='svg']"))).click()
time.sleep(2)

""" For Support Contact """
action = ActionChains(driver)
action.move_to_element(driver.find_element(By.XPATH, "(//div[@class='Support-Bar'])[1]")).perform()
time.sleep(4)

""" Logout icon """
driver.find_element(By.XPATH, "//button[@class='button-sidebar']//*[name()='svg']").click()
time.sleep(2)

""" Clicking Yes as logout option """
driver.find_element(By.XPATH, "//button[normalize-space()='Yes']").click()
time.sleep(5)
