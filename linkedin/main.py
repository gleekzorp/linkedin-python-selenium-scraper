from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
# from linkedin_secrets import secret
import secret

driver = webdriver.Chrome()
search_phrase = 'Software Engineer'
# filter_index: 1 = internship, 2 = entry level, 3 = associate
filter_index = 1


def login():
    driver.get('https://www.linkedin.com')
    driver.find_element(By.CSS_SELECTOR, "[class*='nav__button-secondary']").click()
    time.sleep(2)
    driver.find_element(By.ID, 'username').send_keys(secret.USER_NAME)
    driver.find_element(By.ID, 'password').send_keys(secret.PASSWORD + Keys.ENTER)
    time.sleep(5)
    print('logged in')


def filter_search():
    driver.find_element(By.XPATH, '//*[@aria-label="Filter results by: Experience Level"]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, f'//*[@id="experience-level-facet-values"]//ul//li[{filter_index}]//label').click()
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@id="experience-level-facet-values"]//button[2]').click()


def job_search():
    login()
    driver.find_element(By.XPATH, '//*[@id="jobs-nav-item"]').click()
    driver.find_element(By.XPATH, '//*[@class="jobs-search-box__text-input"]').send_keys(search_phrase + Keys.ENTER)
    time.sleep(5)
    filter_search()
    # pagination = driver.find_element(By.XPATH, '//*[@class="jobs-search-two-pane__pagination"]')
    # time.sleep(5)
    # ActionChains(driver).move_to_element(pagination).perform()
    # time.sleep(5)
    # links = driver.find_elements(By.XPATH, '//*[@class="jobs-search-results__list artdeco-list"]//li//div//h3//a')

    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # driver.execute_script("arguments[0].scrollIntoView();", pagination)
    time.sleep(5)
    links = WebDriverWait(driver, 20).until(
        # EC.presence_of_all_elements_located((By.XPATH, '//*[@class="jobs-search-results__list artdeco-list"]//li//div//h3//a'))
        EC.presence_of_all_elements_located((By.XPATH, '//*[@class="jobs-search-results__list artdeco-list"]//h3//a'))
    )
    print(len(links))

    # for link in links:
    #     link.click()
    #     time.sleep(1)

    # for link in links:
    #     print(f"{link.text} - {link.get_attribute('href')}")
    driver.close()


job_search()



# $('#jobs-search-box-keyword-id-ember529')
# $('.jobs-search-box__text-input')
# //*[@class="jobs-search-results__list artdeco-list"]//li//div//h3//a
# //*[@class="jobs-search-two-pane__pagination"]
# A_jobssearch_job_result_click
# //*[@itemtype='http://schema.org/ItemList']//h3//a
# //*[@aria-label='Filter results by: Experience Level']
# //*[@id='experience-level-facet-values']//ul//li[1]//input
# //*[@id="experience-level-facet-values"]//div//div//div//button[2]
# //*[@id="experience-level-facet-values"]//button[2]

# https://stackoverflow.com/questions/35641019/how-do-you-use-credentials-saved-by-the-browser-in-auto-login-script-in-python-2
