from igramscraper.instagram import Instagram
from credentials import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from scraping_lib import *
import time


#SOURCES
# igramscraper - https://github.com/realsirjoe/instagram-scraper


#OBJECTIVES
# BASIC - Posts, nº of comme

#REAL CODE
#instagram = Instagram()

# authentication supported
#instagram.with_credentials(login, password)
#instagram.login()

#Getting an account by id
#account = instagram.get_account_by_id(3)
#account = instagram.get_account(account)

def login_procedures():
  driver.get(login_path)
  username_field = select_element_by_name(driver, 'username', login)
  set_value(username_field,login)
  password_field = select_element_by_name(driver,'password', password)
  set_value(password_field,password)
  time.sleep(3)
  object = select_element_by_xpath(driver, login_xpath)
  object.click()
  time.sleep(3)
  object = select_element_by_xpath(driver, button_after_login_xpath)
  object.click()
  time.sleep(5)
  object = select_element_by_xpath(driver, button_no_updates_xpath)
  object.click()

driver = webdriver.Firefox()

time.sleep(5)
login_procedures()
time.sleep(5)

time.sleep(10000)

#driver.close()