from credentials import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from scraping_lib import *
from scraping_paths import *
from pandas_lib import *
import time


def login_procedures():
  driver.get(login_path)
  username_field = select_element_by_xpath(driver, username_xpath)
  set_value(username_field, login)
  password_field = select_element_by_xpath(driver, password_xpath)
  set_value(password_field, password)
  time.sleep(3)
  object = select_element_by_xpath(driver, login_button_xpath)
  object.click()
  time.sleep(3)
  object = select_element_by_xpath(driver, button_after_login_xpath)
  object.click()
  time.sleep(5)
  object = select_element_by_xpath(driver, button_no_updates_xpath)
  object.click()

def get_profile_data():
  driver.get(target_profile)
  time.sleep(5)
  global profile_name 
  global profile_real_name 
  global profile_post_count 
  global profile_followers_count 
  global profile_following_count 
  
  profile_name = select_element_by_xpath(driver, profile_name_xpath)
  profile_real_name = select_element_by_xpath(driver, profile_real_name_xpath)
  profile_post_count = select_element_by_xpath(driver, profile_posts_count_path)
  profile_followers_count = select_element_by_xpath(driver, profile_followers_path)
  profile_following_count = select_element_by_xpath(driver, profile_following_path)
  print(profile_name, profile_real_name, profile_post_count, profile_followers_count, profile_following_count)

def export_profile_data():
  d = { 
    'profile_real_name': [profile_real_name],
    'profile_post_count': [profile_post_count],
    'profile_followers_count': [profile_followers_count],
    'profile_following_count': [profile_following_count]
  }
  df = create_df_by_dictionary(d)
  save_csv_file('', profile_name, 'profile_data', df)

driver = webdriver.Firefox()

time.sleep(5)
login_procedures()
time.sleep(5)
get_profile_data()
time.sleep(10)
export_profile_data()
time.sleep(10000)

#driver.close()