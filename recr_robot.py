from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException, MoveTargetOutOfBoundsException, NoSuchWindowException, StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import keyboard
from time import sleep


#Create the 'bridge' with driver, opening the page we want to see and returning the browser element to be used further on.
def openWebPage(webpage='https://www.linkedin.com/'):
    #Try open the page the 1st time.
    try:
        browser = webdriver.Edge()
        browser.get(webpage)
        browser.maximize_window()
        return browser
    #If we get any error on the process, we call the function #again.
    except (NoSuchWindowException, WebDriverException):
        print('Webpage not found, trying again...')
        #openwebpage()

#Logging in.
def login(browser, email='', pword=''):
    try:        
        #Find login button, click it.
        login_button = browser.find_element_by_class_name('nav__button-secondary')
        login_button.click()
        #Find user login box, insert login string.
        user_button = browser.find_element_by_id('username')
        user_button.send_keys(email)
        #Find user password box, insert password
        password = browser.find_element_by_id('password')
        password.send_keys(pword)
        #Find login button and click to finish login
        browser.find_element_by_class_name('login__form_action_container').click()
    #If we get any error on the process, we call the function #again.
    except (WebDriverException, AttributeError):
        print('Something wrong here, man. Trying again...')
        #login(browser)

#Locate and press 'jobs' button on the header.
def jobsButton(browser):
    WebDriverWait(browser, 15).until(expected_conditions.presence_of_element_located((By.ID, 'ember25'))).click()

#Locate and insert keywords on the job title search box.
def jobsBar(browser):
    #WebDriverWait(browser, 10).until(expected_conditions.presence_of_element_located((By.ID, 'jobs-search-box-keyword-id-ember1073'))).send_keys('data analyst')
    browser.find_element_by_xpath('//*[@id="jobs-search-box-keyword-id-ember361"]').send_keys('data analyst')

def locationBar(browser, location='Barcelona'):
    #Access location bar
    browser.find_element_by_class_name('jobs-search-box__input.jobs-search-box__input--location').click()
    #Double click the bar to select the default word
    webdriver.ActionChains(browser).double_click(browser.find_element_by_class_name ('jobs-search-box__input.jobs-search-box__input--location')).perform()
    #Erase it
    keyboard.press_and_release('backspace')
    #Write the location I want
    keyboard.write('Barcelona')
    #Press Enter
    keyboard.press_and_release('return')

def solicitudSencillaButton(browser):
    #Access arrow button and press it to make 'solicitud sencilla' button visible
    WebDriverWait(browser, 15, ignored_exceptions=[StaleElementReferenceException]).until(expected_conditions.presence_of_element_located((By.ID,'ember867'))).click()
    '''#Double click the bar to select the default word
    webdriver.ActionChains(browser).double_click(browser.find_element_by_class_name ('jobs-search-box__input.jobs-search-box__input--location')).perform()
    #Erase it
    keyboard.press_and_release('backspace')
    #Write the location I want
    keyboard.write('Barcelona')
    #Press Enter
    keyboard.press_and_release('return')'''

browser = openWebPage()
sleep(3)
login(browser)
sleep(3)
jobsButton(browser)
sleep(3)
jobsBar(browser)
sleep(3)
locationBar(browser)
sleep(3)
solicitudSencillaButton(browser)






