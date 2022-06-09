from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#simple methods, more understandable
#wide use functions
def set_value(element, value):
  element.send_keys(value)

def get_inner_html(element):
  return element.get_attribute('innerHTML')

#selection functions
def select_element_by_xpath(driver, element):
  return driver.find_element(By.XPATH, element)

def select_element_by_id(driver, element):
  return driver.find_element(By.ID, element)

def select_element_by_name(driver, element):
  return driver.find_element(By.NAME, element)

def select_element_by_tag_name(driver, element):
  return driver.find_element(By.TAG_NAME, element)