import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from student_my_interviews import my_interviews
from student_my_profile import my_profile


reset = input("Do you want reset password? then press (y) : ")

n = int(input("how many times do you want interview? : "))


# Allow camera and microphone access automatically
# Set default permissions for camera, microphone
chrome_options = Options()
prefs = {
    "profile.default_content_setting_values.media_stream_camera": 1,  # 1 = Allow, 0 = not Allow.
    "profile.default_content_setting_values.media_stream_mic": 1  # 1 = Allow, 0 = not Allow.
}

chrome_options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()


""" Sign In """
driver.get("https://master.d3rqcznoic140q.amplifyapp.com/")
# sign in button
driver.find_element(By.CSS_SELECTOR, "button[class='header_button']").click()
# email id
driver.find_element(By.ID, "email-id").send_keys("test333@test.com")
# password
driver.find_element(By.ID, "password-id").send_keys("Aditya@1234")
# submit button
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

""" My Profile """
my_profile(driver, reset)

""" Aditya logo """
driver.find_element(By.XPATH, "//img[@class='LogoHeader']").click()
time.sleep(2)

""" My Interviews """
my_interviews(driver,n)

""" logout """
driver.find_element(By.XPATH, "(//*[name()='svg'][@class='BellIcon-Header-JS'])[1]").click()
time.sleep(1)

# yes
driver.find_element(By.XPATH, "//button[normalize-space()='Yes']").click()
time.sleep(4)
