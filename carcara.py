from scraping_paths import *
from pandas_lib import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

class Carcara():
  def __init__(self, driver):
    self.driver = driver

  def login(self, user, password):
    print('Login...')
    self.driver.get(login_path)
    time.sleep(10)
    username_field = self.select_by_xpath(username_xpath)
    self.set_value(username_field, user)
    password_field = self.select_by_xpath(password_xpath)
    self.set_value(password_field, password)
    time.sleep(5)
    object = self.select_by_xpath(login_button_xpath)
    object.click()
    time.sleep(10)
    object = self.select_by_xpath(button_after_login_xpath)
    object.click()
    time.sleep(10)
    object = self.select_by_xpath(button_no_updates_xpath)
    object.click()
    print('Login Completed')

    
  #basic tools
  def select_by_xpath(self, element):
    return self.driver.find_element(By.XPATH, element)

  def set_value(self, element, value):
    element.send_keys(value)

  def use_key(self, key):
    if(key == 'esc'):
      key = '\ue00c'
    elif(key == 'down'):
      key = '\ue015'
    ActionChains(self.driver).send_keys(key).perform()

  def to_csv(self, columns_list, data_list, filename):
    d = {}
    for i in range(0, len(columns_list)):
      current_data = []
      for data in data_list:
        current_data.append(data[i])
      d[columns_list[i]] = current_data
    df = create_df_by_dictionary(d)
    save_csv(filename, df)

  def json_to_csv(self, json, filename):
    columns_list = list(json[0].keys())
    data_list = []
    for j in json:
      data_list.append(list(j.values()))
    self.to_csv(columns_list, data_list, filename)