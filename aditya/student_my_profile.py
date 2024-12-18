import time
from pynput.keyboard import Controller, Key
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from reset_password import reset_password


def my_profile(driver, reset):

    wait = WebDriverWait(driver, 60)
    wait.until(ec.element_to_be_clickable((By.XPATH, "//div[@id='myprofile']//img[@class='Entity-Box-Img']"))).click()
    time.sleep(4)

    """ Active Interview """
    # Professional Summary
    driver.find_element(By.XPATH, "//div[@id='jobseeker-myprofile-summary-text']//*[name()='svg']").click()

    # writing text
    driver.find_element(By.XPATH, "//textarea[@id='jobseeker-myprofile-summary-textarea']"
                        ).send_keys("backend developer")
    time.sleep(2)

    # saving summary
    driver.find_element(By.XPATH, "//button[@id='summary-save']").click()
    time.sleep(5)

    # again click professional summary
    wait = WebDriverWait(driver, 60)
    wait.until(ec.invisibility_of_element_located((By.CSS_SELECTOR, "div.loader")))
    wait.until(ec.element_to_be_clickable((By.XPATH, "//div[@id='jobseeker-myprofile-summary-text']//*[name()='svg']"))).click()

    # cancel icon
    wait = WebDriverWait(driver, 15)
    wait.until(ec.element_to_be_clickable((By.XPATH, "//span[@id='jobseeker-myprofile-summary-cancel-icon']"))).click()
    time.sleep(1)

    """ Education """
    wait = WebDriverWait(driver, 60)
    wait.until(ec.invisibility_of_element_located((By.CSS_SELECTOR, "div.loader")))
    wait.until(ec.element_to_be_clickable((By.XPATH, "//div[@id='jobseeker-myprofile-tab3']"))).click()

    # Add icon
    wait = WebDriverWait(driver, 30)
    wait.until(ec.invisibility_of_element_located((By.CSS_SELECTOR, "div.loader")))
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "div[id='education-details-add-icon'] svg"))).click()

    wait = WebDriverWait(driver, 30)
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "#education-page-name-id"))).send_keys("B.TECH")

    wait = WebDriverWait(driver, 30)
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "#education-page-academy-id"))
               ).send_keys("Geethanjali Institute of Science and Technology")
    time.sleep(1)

    wait = WebDriverWait(driver, 30)
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "#education-page-field-id"))).send_keys("Computer science"
                                                                                                    " and IT")
    # Percentage
    wait = WebDriverWait(driver, 30)
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "label[for='percentage-id']"))).click()

    # Score in Percentage
    wait = WebDriverWait(driver, 30)
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "#education-page-score-id"))).send_keys("89")
    time.sleep(2)

    # CGPA
    wait = WebDriverWait(driver, 30)
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, " label[for ='cgpa-id']"))).click()

    # Score in CGPA
    wait = WebDriverWait(driver, 30)
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "#education-page-score-id"))).send_keys("8.3")

    # Start Date
    driver.find_element(By.CSS_SELECTOR, "#education-page-startdate-id").send_keys("05-08-2018")

    # End Date
    driver.find_element(By.CSS_SELECTOR, "#education-page-enddate-id").send_keys("08-09-2022")

    # Submit
    driver.find_element(By.CSS_SELECTOR, "#education-page-submit-id").click()
    time.sleep(1)

    # Edit Education Details...
    wait = WebDriverWait(driver, 60)
    wait.until(ec.element_to_be_clickable((By.XPATH, "//div[@id='education-details-edit-container-0']//*[name()='svg']"))).click()

    # Cancel
    wait = WebDriverWait(driver, 60)
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, " #education-page-cancel-id"))).click()
    time.sleep(1)

    # Delete Education Details
    wait = WebDriverWait(driver, 60)
    wait.until(ec.element_to_be_clickable((By.ID, "education-details-delete-0"))).click()
    time.sleep(1)

    # Are you sure Delete?:  NO
    wait = WebDriverWait(driver, 60)
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "#certificate-no-id"))).click()
    time.sleep(1)

    # Delete Education Details
    driver.find_element(By.ID, "education-details-delete-0").click()

    # Are you sure Delete?: Yes
    wait = WebDriverWait(driver, 60)
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "#certificate-yes-id"))).click()
    time.sleep(2)

    """ Certificates"""
    wait = WebDriverWait(driver, 60)
    wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, "#jobseeker-myprofile-tab4"))).click()
    time.sleep(2)

    # Adding Certificates
    wait = WebDriverWait(driver, 60)
    wait.until(ec.presence_of_element_located((By.XPATH, "//div[@id='certifications-details-form-edu-icon']"
                                                         "//*[name()='svg']"))).click()

    # Certificate Name
    wait = WebDriverWait(driver, 60)
    (wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, "#certificate-page-name-id"))).send_keys
     ("AWS Cloud Computing"))

    # Issued Organization
    driver.find_element(By.CSS_SELECTOR, "#certificate-page-issuedby-id").send_keys("Amazon")

    # Credential Id
    driver.find_element(By.CSS_SELECTOR, "#certificate-page-credential-id").send_keys("siddardha.t")

    # Credential URL
    driver.find_element(By.CSS_SELECTOR, "#certificate-page-url-id").send_keys("www.aws.com")

    # Click URL
    wait = WebDriverWait(driver, 60)
    wait.until(ec.element_to_be_clickable((By.XPATH, "//a[@id='education-certifications-details-form-credentialUrl"
                                                     "-link']"))).click()
    # Switch to main webpage
    driver.switch_to.window(driver.window_handles[0])

    # Check Box, This certificate doesn't expire.
    driver.find_element(By.CSS_SELECTOR, "input[class='checkbox-input']").click()

    # Start Date
    driver.find_element(By.CSS_SELECTOR, "#certificate-page-startdate-id").send_keys("05-01-2024")

    # End Date
    driver.find_element(By.CSS_SELECTOR, "#certificate-page-startdate-id").send_keys("04-06-2024")

    # Submit
    driver.find_element(By.XPATH, "//button[@id='certificate-page-submit-id']").click()

    # Again adding certificates icon for testing cancel option.
    wait = WebDriverWait(driver, 60)
    wait.until(ec.invisibility_of_element_located((By.CLASS_NAME, "loader")))
    wait.until(ec.presence_of_element_located((By.XPATH, "//div[@id='certifications-details-form-edu-icon']"
                                                         "//*[name()='svg']"))).click()
    time.sleep(2)

    # Cancel
    driver.find_element(By.XPATH, "//button[@id='certificate-page-cancel-id']").click()

    # Edit Certificates
    driver.find_element(By.XPATH, "//div[@id='certifications-details-form-edit-delete-container-0']"
                                  "//*[name()='svg']").click()
    keyboard = Controller()
    keyboard.press(Key.page_down)

    #cancle
    driver.find_element(By.XPATH, "//button[@id='certificate-page-cancel-id']").click()

    # Delete Certificates
    driver.find_element(By.XPATH, "//div[@id='certifications-details-form-edit-delete-container-0']"
                                  "//*[name()='svg']//*[name()='path' and contains(@d,'M6 19c0 1.')]").click()
    time.sleep(1)
    # No
    driver.find_element(By.XPATH, "//button[@id='certificate-no-id']").click()
    time.sleep(1)

    # Delete Certificates
    driver.find_element(By.XPATH, "//div[@id='certifications-details-form-edit-delete-container-0']"
                                  "//*[name()='svg']//*[name()='path' and contains(@d,'M6 19c0 1.')]").click()
    time.sleep(2)
    # Yes
    driver.find_element(By.XPATH, "//button[@id='certificate-yes-id']").click()
    time.sleep(1)
    """ Reset Password """
    reset_password(driver, reset)

    """ Acceptance policy """
    wait = WebDriverWait(driver, 60)
    element2 = wait.until(ec.element_to_be_clickable((By.XPATH, "(//*[name()='path'])[9]")))
    actions = ActionChains(driver)
    actions.move_to_element(element2).click().perform()
    time.sleep(2)

    # to scroll down
    element3 = driver.find_element(By.XPATH, "(//div)[24]")
    actions.move_to_element(element3).click().perform()
    actions.send_keys(Keys.PAGE_DOWN).perform()

    """ PROFILE ICON """
    element4 = driver.find_element(By.XPATH, "(//*[name()='path'])[6]")
    actions = ActionChains(driver)
    actions.move_to_element(element4).click().perform()
    time.sleep(1)




