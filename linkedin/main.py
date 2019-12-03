from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os.path

import time
# from linkedin_secrets import secret
import secret

driver = webdriver.Chrome()
search_phrase = 'Software Engineer'
# filter_index: 1 = internship, 2 = entry level, 3 = associate
filter_index = 1
job_file = ['internship', 'entry_level', 'associate']
current_date = '2019-12-02'
jobs_list = []


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


def add_jobs_to_list(jobs):
    for job in jobs:
        job.click()
        time.sleep(5)
        job_company = driver.find_element(By.XPATH, '//*[@class="jobs-details-top-card__company-url ember-view"]')
        jobs_list.append(job_company.text)
        jobs_list.append(job_company.get_attribute('href'))
        time.sleep(5)


def write_jobs_to_file(jobs):
    # f = open(f'{job_file[filter_index]}-{current_date}.txt', "w")
    f = open(f'{job_file[filter_index]}.txt', "w")
    for job in jobs:
        job.click()
        time.sleep(5)
        job_company = driver.find_element(By.XPATH, '//*[@class="jobs-details-top-card__company-url ember-view"]')
        job_title = driver.find_element(By.XPATH, '//*[@class="jobs-details-top-card__content-container"]/a')
        f.write(
            job_company.text + "\n" +
            job_company.get_attribute('href') + "\n" +
            job_title.text + "\n" +
            job_title.get_attribute('href') + "\n\n"
        )
        time.sleep(5)


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
    # add_jobs_to_list(links)
    write_jobs_to_file(links)

    # for link in links:
    #     print(f"{link.text} - {link.get_attribute('href')}")
    print(jobs_list)
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
# //*[@class="jobs-details-top-card__company-url ember-view"]
# //*[@class="jobs-details-top-card__content-container"]/a

# https://stackoverflow.com/questions/35641019/how-do-you-use-credentials-saved-by-the-browser-in-auto-login-script-in-python-2
