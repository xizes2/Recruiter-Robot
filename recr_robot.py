from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException, MoveTargetOutOfBoundsException, NoSuchWindowException
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
def login(browser, email='MAIL@mail.com', pword='password'):
    try:        
        #Find login button, click it.
        login_button = browser.find_element_by_class_name('nav__button-secondary')
        login_button.click()
        #Find user login box, insert login string.
        user_button = browser.find_element_by_id('username')
        user_button.send_keys(email)
        #Find user password box, insert password
        pword = browser.find_element_by_id('password')
        pword.send_keys('PASSWORD')
        #Find login button and click to finish login
        browser.find_element_by_class_name('login__form_action_container').click()
    #If we get any error on the process, we call the function #again.
    except (WebDriverException, AttributeError):
        print('Something wrong here, man. Trying again...')
        #login(browser)

#Access LinkeIn search bar and input the name of the job we want.
def searchBar(browser):
    search_bar = browser.find_element_by_id('ember20')
    search_bar.click()
    keyboard.write('analista de datos')
    keyboard.press_and_release('Return')

browser = openWebPage()
sleep(3)
login(browser)
sleep(3)
searchBar(browser)






