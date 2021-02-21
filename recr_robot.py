from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException, MoveTargetOutOfBoundsException, NoSuchWindowException


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
def login(browser, email='email@mail.com', pword='password'):
    #Find login button, click it, insert login string and click it.
    try:        
        login_button = browser.find_element_by_class_name("nav__button-secondary")
        login_button.click()
        user_button = browser.find_element_by_id("username")
        user_button.send_keys(email)
    #If we get any error on the process, we call the function #again.
    except (WebDriverException, AttributeError):
        print('Something wrong here, man. Trying again...')
        #login(browser)

browser = openWebPage()
login(browser)






