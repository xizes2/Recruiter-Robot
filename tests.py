from selenium import webdriver

webpage='https://www.linkedin.com/'
browser = webdriver.Edge()
browser.get(webpage)
browser.maximize_window()
 
login = browser.find_element_by_class_name("nav__button-secondary")
login.click()
user = browser.find_element_by_id("username")#.click()
user.send_keys("email@hotmail.com")

#browser.close()       