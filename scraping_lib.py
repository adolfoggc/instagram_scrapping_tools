from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import selenium.common.exceptions
import time

#simple methods, more understandable
#wide use functions
def set_value(element, value):
  element.send_keys(value)

def get_inner_html(element):
  return element.get_attribute('innerHTML')

def get_href(element):
  return element.get_attribute('href')

#use keys

def use_key(driver, key):
  if(key == 'esc'):
    key = '\ue00c'
  elif(key == 'down'):
    key = '\ue015'
  ActionChains(driver).send_keys(key).perform()

#selection functions
def select_by_xpath(driver, element):
  return driver.find_element(By.XPATH, element)

def select_by_id(driver, element):
  return driver.find_element(By.ID, element)

def select_by_name(driver, element):
  return driver.find_element(By.NAME, element)

def select_by_tag_name(driver, element):
  return driver.find_element(By.TAG_NAME, element)

def find_and_select(driver, method, element, count):
  try:
    if(method == 'xpath'):
      return select_by_xpath(driver, element)
  except selenium.common.exceptions.MoveTargetOutOfBoundsException:
    if(count < 10):
      count += 1
      print('Tentativa ' + str(count) +' falhou')
      use_key(driver, 'down')
      time.sleep(1)
    elif(count >= 10):
      print('10 tentativas para alcançar o elemento falharam')
      print('Abortando busca')
#page

#polishing data
def get_quantity_of_views_or_likes(str):
  str = remove_tag(str, 'span', True)
  break_point = str.find(' ')
  value = str[:break_point]
  text = str[break_point + 1 :]
  return [value, text]

def remove_tag(str, tag_name, open_and_close):
  str = str.replace('<'+ tag_name + '>', '')
  if(open_and_close):
    str = str.replace('</'+ tag_name + '>', '')
  return str