from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

#Open webpage
webpage='https://www.linkedin.com/'
browser = webdriver.Edge()
browser.implicitly_wait(15)
browser.get(webpage)
browser.maximize_window()

#Login  
login = browser.find_element_by_class_name('nav__button-secondary')
login.click()
browser.find_element_by_id('username').send_keys('mail@mail.com')
browser.find_element_by_id('password').send_keys('password')
browser.find_element_by_class_name('login__form_action_container').click()

#Search keywords
#search_bar = 
browser.find_element_by_class_name('search-global-typeahead__input always-show-placeholder'.replace(' ', '.')).send_keys('analista de datos' + Keys.ENTER)

#Click on 'Jobs' button
WebDriverWait(browser, 5).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, 'mr2'))).click()
#browser.find_element_by_class_name('mr2').click()

#Select location
ActionChains(browser).move_to_element(browser.find_element_by_class_name('jobs-search-box__text-input').click())




   
#search_boxes[1]