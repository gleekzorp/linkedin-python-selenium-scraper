from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time
from secrets import secret


def login():
    driver = webdriver.Chrome()
    driver.get('https://www.linkedin.com')
    driver.find_element(By.CSS_SELECTOR, "[class*='nav__button-secondary']").click()
    time.sleep(2)
    driver.find_element(By.ID, 'username').send_keys(secret.USER_NAME)
    driver.find_element(By.ID, 'password').send_keys(secret.PASSWORD + Keys.ENTER)
    time.sleep(2)
    print(driver.title)
    driver.close()


login()
