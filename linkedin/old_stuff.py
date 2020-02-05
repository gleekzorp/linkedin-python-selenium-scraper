import os.path

# job_file = ['internship', 'entry_level', 'associate']

# def write_jobs_to_file(jobs, write_or_append):
#     # f = open(f'{job_file[filter_index]}-{current_date}.txt', "w")
#     f = open(f'{job_file[filter_index]}.txt', write_or_append)
#     for job in jobs:
#         job.click()
#         time.sleep(5)
#         job_company = driver.find_element(By.XPATH, '//*[@class="jobs-details-top-card__company-url ember-view"]')
#         job_title = driver.find_element(By.XPATH, '//*[@class="jobs-details-top-card__content-container"]/a')
#         # job_location = driver.find_element(By.XPATH, '//*[@class="jobs-details-top-card__content-container"]//span[3]')
#         f.write(
#             job_company.text + "\n" +
#             job_company.get_attribute('href') + "\n" +
#             job_title.text + "\n" +
#             job_title.get_attribute('href') + "\n\n"
#             # job_location.text + "\n" +
#         )
#         time.sleep(5)
#     f.close()


# def write_jobs_to_file(jobs, write_or_append):
#     # f = open(f'{job_file[filter_index]}-{current_date}.txt', "w")
#     f = open(f'{job_file[filter_index]}.txt', write_or_append)
#
#     for job in jobs:
#         job.click()
#         time.sleep(5)
#         if driver.find_elements(By.XPATH, '//*[@data-control-name="jobdetails_profile_poster"]') and driver.find_elements(By.XPATH, '//*[@class="jobs-details-top-card__content-container"]//span[3]'):
#             job_posted_by = driver.find_element(By.XPATH, '//*[@data-control-name="jobdetails_profile_poster"]')
#             job_company = driver.find_element(By.XPATH, '//*[@class="jobs-details-top-card__company-url ember-view"]')
#             job_title = driver.find_element(By.XPATH, '//*[@class="jobs-details-top-card__content-container"]/a')
#             job_location = driver.find_element(By.XPATH, '//*[@class="jobs-details-top-card__content-container"]//span[3]')
#             f.write(
#                 job_company.text + "\n" +
#                 job_company.get_attribute('href') + "\n" +
#                 job_title.text + "\n" +
#                 job_title.get_attribute('href') + "\n" +
#                 job_location.text + "\n" +
#                 'Posted By: ' + job_posted_by.get_attribute('href') + "\n\n"
#             )
#             time.sleep(5)
#         else:
#             print('something went wrong')
#     f.close()


# def add_jobs_to_list(jobs):
#     x = 0
#     for job in jobs:
#         job.click()
#         time.sleep(5)
#         job_company = driver.find_element(By.XPATH, '//*[@class="jobs-details-top-card__company-url ember-view"]')
#         job_title = driver.find_element(By.XPATH, '//*[@class="jobs-details-top-card__content-container"]/a')
#         job_dict = {'id': x, 'company_name': job_company.text, 'company_link': job_company.get_attribute('href'),
#                     'job_title': job_title.text, 'job_title_link': job_title.get_attribute('href')}
#         jobs_list.append(dict(job_dict))
#         time.sleep(2)
#         x += 1
#         print(job_dict)