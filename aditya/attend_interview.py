import time
from pathlib import Path
import pyautogui
from pynput.keyboard import Controller, Key
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


def interview(driver, n):
    wait = WebDriverWait(driver, 30)
    wait.until(ec.element_to_be_clickable((By.XPATH, "//h1[normalize-space()='My Interviews']"))).click()

    for i in range(n):

        element = driver.find_element(By.XPATH, "//span[@class='myInterviews-active-interviews-number-title-span']")
        element_text = element.text.strip()

        if element_text == "12":
            time.sleep(2)
            keyboard = Controller()
            keyboard.press(Key.page_down)
            keyboard.press(Key.down)
            time.sleep(5)

            wait = WebDriverWait(driver, 60)
            wait.until(ec.invisibility_of_element_located((By.CSS_SELECTOR, "div.loader")))
            wait.until(
                ec.visibility_of_element_located((By.XPATH, "(//*[name()='svg'][contains(@class,'dots-icon')])[3]")))
            wait.until(
                ec.element_to_be_clickable((By.XPATH, "(//*[name()='svg'][contains(@class,'dots-icon')])[3]"))).click()
            driver.find_element(By.XPATH, "//div[normalize-space()='Archive']").click()
            time.sleep(6)

            wait = WebDriverWait(driver, 30)
            wait.until(ec.invisibility_of_element_located((By.CSS_SELECTOR, "div.loader")))
            wait.until(
                ec.element_to_be_clickable((By.XPATH, "(//*[name()='svg'][contains(@class,'dots-icon')])[4]"))).click()
            driver.find_element(By.XPATH, "//div[normalize-space()='Archive']").click()
            time.sleep(6)

            wait = WebDriverWait(driver, 30)
            wait.until(ec.invisibility_of_element_located((By.CSS_SELECTOR, "div.loader")))
            wait.until(
                ec.visibility_of_element_located((By.XPATH, "(//*[name()='svg'][contains(@class,'dots-icon')])[5]")))
            wait = WebDriverWait(driver, 30)
            wait.until(
                ec.element_to_be_clickable((By.XPATH, "(//*[name()='svg'][contains(@class,'dots-icon')])[5]"))).click()
            driver.find_element(By.XPATH, "//div[normalize-space()='Archive']").click()
            time.sleep(10)

            wait = WebDriverWait(driver, 30)
            wait.until(ec.invisibility_of_element_located((By.CSS_SELECTOR, "div.loader")))
            wait.until(
                ec.visibility_of_element_located((By.XPATH, "(//*[name()='svg'][contains(@class,'dots-icon')])[6]")))
            wait = WebDriverWait(driver, 30)
            wait.until(
                ec.element_to_be_clickable((By.XPATH, "(//*[name()='svg'][contains(@class,'dots-icon')])[6]"))).click()
            driver.find_element(By.XPATH, "//div[normalize-space()='Archive']").click()
            time.sleep(10)

            wait = WebDriverWait(driver, 30)
            wait.until(ec.invisibility_of_element_located((By.CSS_SELECTOR, "div.loader")))
            wait.until(
                ec.visibility_of_element_located((By.XPATH, "(//*[name()='svg'][contains(@class,'dots-icon')])[7]")))
            wait = WebDriverWait(driver, 30)
            wait.until(
                ec.element_to_be_clickable((By.XPATH, "(//*[name()='svg'][contains(@class,'dots-icon')])[7]"))).click()
            driver.find_element(By.XPATH, "//div[normalize-space()='Archive']").click()
            time.sleep(6)

            keyboard = Controller()
            keyboard.press(Key.page_up)
            keyboard.press(Key.page_up)

        # Attend Interviews
        time.sleep(1)
        wait = WebDriverWait(driver, 30)
        wait.until(ec.invisibility_of_element_located((By.CSS_SELECTOR, "div.loader")))
        wait.until(ec.element_to_be_clickable((By.XPATH, "//div[@class='tabs-container']//div[3]//button[1]")))
        driver.find_element(By.XPATH, "//div[@class='tabs-container']//div[3]//button[1]").click()
        time.sleep(1)

        """You are about to attend an interview for the role of Junior Mechanical Engineer under the sector
           Mechanical Engineering ."""

        # Would you like to change them ? toggle-button
        wait = WebDriverWait(driver, 30)
        wait.until(ec.invisibility_of_element_located((By.CSS_SELECTOR, "div.loader")))
        wait = WebDriverWait(driver, 30)
        wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, ".toggle-button"))).click()
        time.sleep(1)

        # Branches
        driver.find_element(By.ID, "captureskills_jobsector").click()
        time.sleep(2)

        driver.find_element(By.CSS_SELECTOR, "span[title='Select this option if you are studying "
                                             "Computer Science Engineering (CSE)']").click()
        time.sleep(1)

        driver.find_element(By.ID, "captureskills_jobrole").click()
        time.sleep(1)
        wait.until(ec.invisibility_of_element_located((By.CSS_SELECTOR, "div.loader")))
        wait.until(ec.visibility_of_element_located((By.XPATH, "//*[text()='Software Developer - Entry Level']")))
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[text()='Software Developer - Entry Level']"))).click()
        time.sleep(2)

        # primary skills
        wait = WebDriverWait(driver, 60)
        wait.until(ec.invisibility_of_element_located((By.CSS_SELECTOR, "div.loader")))
        wait.until(ec.presence_of_element_located((By.ID, "captureskills_primaryskills"))).click()
        time.sleep(2)
        skill = "Python"
        pyautogui.write(skill)
        pyautogui.press('down')
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.press('tab')

        # Upload Resume
        wait = WebDriverWait(driver, 60)
        wait.until(ec.invisibility_of_element_located((By.CSS_SELECTOR, "div.loader")))
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".CS_Skill_Upload_Button_Cloud")))
        element1 = driver.find_element(By.CSS_SELECTOR, ".CS_Skill_Upload_Button_Cloud")
        action = ActionChains(driver)
        action.move_to_element(element1).click().perform()
        time.sleep(2)
        file_path = Path("C:/Users/HP/Downloads/upload/Resume.pdf")
        time.sleep(1)
        pyautogui.write(str(file_path))
        time.sleep(2)
        pyautogui.press('enter')
        time.sleep(2)

        # Submit
        wait = WebDriverWait(driver, 30)
        wait.until(ec.invisibility_of_element_located((By.CSS_SELECTOR, "div.loader")))
        wait = WebDriverWait(driver, 60)
        wait.until(ec.visibility_of_element_located((By.CLASS_NAME, "CS_Skill_Submit_button")))
        wait.until(ec.element_to_be_clickable((By.CLASS_NAME, "CS_Skill_Submit_button"))).click()
        time.sleep(4)

        # Start Recording ...
        wait = WebDriverWait(driver, 60)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Start Recording']"))).click()
        time.sleep(2)

        # Stop Recording ...
        wait = WebDriverWait(driver, 60)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Stop Recording']"))).click()
        time.sleep(3)

        # Retry Mic Check
        driver.find_element(By.XPATH, "//button[normalize-space()='Retry Mic Check']").click()
        time.sleep(2)

        # Pause recording ...
        driver.find_element(By.XPATH, "//img[@title='Pause recording']").click()
        time.sleep(1)

        # Stop Recording ...
        driver.find_element(By.XPATH, "//button[normalize-space()='Stop Recording']").click()
        time.sleep(1)

        # Start Recording Mike icon...
        driver.find_element(By.XPATH, "//img[@title='Start recording']").click()
        time.sleep(1)

        # Stop Recording ...
        driver.find_element(By.XPATH, "//button[normalize-space()='Stop Recording']").click()

        # Checkbox
        driver.find_element(By.XPATH, "(//input[contains(@class,'mr10')])[1]").click()
        time.sleep(2)



        # Start Interview ...
        wait = WebDriverWait(driver, 60)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//button[normalize-space()='Start Interview']")))
        driver.find_element(By.XPATH, "//button[normalize-space()='Start Interview']").click()
        time.sleep(5)

        # full screen mode popup
        pyautogui.press("enter")

        # Start Instructions
        wait = WebDriverWait(driver, 60)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//button[normalize-space()='START INSTRUCTIONS']"))).click()
        time.sleep(1)


        # Skip Instruction
        wait = WebDriverWait(driver, 60)
        wait.until(
            ec.visibility_of_element_located((By.XPATH, "//button[normalize-space()='SKIP INSTRUCTIONS']"))).click()

        # Start Recording
        wait = WebDriverWait(driver, 60)
        wait.until(
            ec.visibility_of_element_located((By.XPATH, "//button[normalize-space()='START RECORDING']"))).click()

        # Stop Recording
        wait = WebDriverWait(driver, 60)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//button[normalize-space()='STOP RECORDING']")))
        wait.until(ec.element_to_be_clickable((By.XPATH, "//button[normalize-space()='STOP RECORDING']"))).click()

        # Technical Interview - Start Interview
        wait = WebDriverWait(driver, 60)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//button[normalize-space()='START INTERVIEW']")))
        wait.until(
            ec.visibility_of_element_located((By.XPATH, "//button[normalize-space()='START INTERVIEW']"))).click()

        # Start Questions 1st Question
        wait = WebDriverWait(driver, 60)
        wait.until(
            ec.visibility_of_element_located((By.XPATH, "//button[normalize-space()='START QUESTIONS']"))).click()
        driver.find_element(By.XPATH, "//div[@class='tech_interview_wrap']").click()
        time.sleep(6)

        # Forwarding Questions
        # Q1 -Q24
        for _ in range(23):
            wait = WebDriverWait(driver, 60)
            wait.until(ec.invisibility_of_element_located((By.CSS_SELECTOR, "div.loader")))
            wait.until(ec.visibility_of_element_located((By.XPATH, "(//button[@class='btn-nextquestion'])[1]")))
            wait.until(ec.element_to_be_clickable((By.XPATH, "(//button[@class='btn-nextquestion'])[1]"))).click()
            time.sleep(5)
        time.sleep(4)

        # Ending - Stop Interview
        wait = WebDriverWait(driver, 60)
        wait.until(ec.invisibility_of_element_located((By.CSS_SELECTOR, "div.loader")))
        wait.until(ec.visibility_of_element_located((By.XPATH, "(//button[@class='btn-stopinterview'])")))
        wait = WebDriverWait(driver, 60)
        wait.until(ec.element_to_be_clickable((By.XPATH, "(//button[@class='btn-stopinterview'])"))).click()
        time.sleep(5)

        '''Back to Home'''
        wait = WebDriverWait(driver, 60)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//p[@class='successmessage_backhome_button']"))).click()
        time.sleep(3)

        wait = WebDriverWait(driver, 60)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//h1[normalize-space()='My Interviews']"))).click()
