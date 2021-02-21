from selenium import webdriver

#Create the 'bridge' with driver, opening the page we want to see and returning the browser element to be used further on.
#def openwebpage(webpage='https://www.linkedin.com/'):
#    #Try open the page the 1st time.
#    try:
#        browser = webdriver.Edge()
#        browser.get(webpage)
#        browser.maximize_window()
#        return browser
#    #If we get any error on the process, we cal the function #again.
#    except (NoSuchWindowException, WebDriverException):
#        print('Webpage not found, trying again...')
#        openwebpage()

webpage='https://www.linkedin.com/'
browser = webdriver.Edge()
browser.get(webpage)
#browser.maximize_window() 
browser.close()       