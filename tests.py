from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import keyboard
from time import sleep

#Open webpage
webpage='https://www.linkedin.com/'
browser = webdriver.Edge()
browser.implicitly_wait(15)
browser.get(webpage)
browser.maximize_window()

#Login  
login = browser.find_element_by_class_name('nav__button-secondary')
login.click()
browser.find_element_by_id('username').send_keys('mail@hotmail.com')
browser.find_element_by_id('password').send_keys('pass')
browser.find_element_by_class_name('login__form_action_container').click()

#Search keywords
#search_bar = 
WebDriverWait(browser, 5).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, 'search-global-typeahead__input always-show-placeholder'.replace(' ', '.')))).send_keys('analista de datos' + Keys.ENTER)

#Click on 'Jobs' button
WebDriverWait(browser, 5).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, 'mr2'))).click()

#Select location
#Access location bar
browser.find_element_by_class_name('jobs-search-box__input.jobs-search-box__input--location').click()
#Double click the bar to select the default word
webdriver.ActionChains(browser).double_click(browser.find_element_by_class_name('jobs-search-box__input.jobs-search-box__input--location')).perform()
#Erase it
keyboard.press_and_release('backspace')
#Write the location I want
keyboard.write('Barcelona')
#Press Enter
keyboard.press_and_release('return')
