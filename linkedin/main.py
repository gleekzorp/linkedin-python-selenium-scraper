from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time
# from secrets import secret
import secret

global_driver = webdriver.Chrome()


def login(driver):
    driver.get('https://www.linkedin.com')
    driver.find_element(By.CSS_SELECTOR, "[class*='nav__button-secondary']").click()
    time.sleep(2)
    driver.find_element(By.ID, 'username').send_keys(secret.USER_NAME)
    driver.find_element(By.ID, 'password').send_keys(secret.PASSWORD + Keys.ENTER)
    time.sleep(5)
    print('login')


def job_search(driver):
    login(driver)
    driver.find_element(By.XPATH, '//*[@id="jobs-nav-item"]').click()
    driver.close()


job_search(global_driver)
