# Linkedin Web Scraper

### After Downloading Or Cloning:
- Install all the dependencies and setup your environment:
```
$ pipenv --three
$ pipenv shell
$ pipenv install selenium
```
- Create a file in the linkedin folder called secret.py
- Add the following code to that file
```
USER_NAME='yourUsername@email.com'
PASSWORD='yourPassword'
```


### How to run the program:
- Make sure you're in your pipenv shell
- Make sure you're in the linkedin folder
```
$ pipenv shell
$ cd linkedin
$ python main.py
```

### Changing Search Terms
- You can change the following commands:
  - search_phrase
  - search_date_posted_range
  - filter_index
  - current_date
- Search phrase is whatever you're searching for:
  - example:
    - search_phrase = "Software Engineer"
- filter_index is based on the following id's:
  - 1 = internship
  - 2 = entry level
  - 3 = associate
  - Example:
    - Internship
      - filter_index = 1
- filter_date_range is based on the following strings:
  - '24'
  - 'week'
  - 'month'
  - Example:
    - Last 24 hours
      - search_date_posted_range = '24'
- current_date is whatever the current date is:
  - Future we will have this autopopulate
  - example
    - current_date = '2019-12-02'

### Linkedin Scraper Requirements:
- Use these searches
  - Software Engineer
  - Web Developer
- Use these filters and save to the information to these three files
  - Internship
  - Entry Level
  - Associate
- Get this data
  - Company
  - Job Title
  - Location
  - Link to posting (this could be the unique ID)
  - Recruiter information if it was posted by a recruiter