from selenium import webdriver
import keyboard

webpage='https://www.linkedin.com/'
browser = webdriver.Edge()
browser.get(webpage)
browser.maximize_window()
 
login = browser.find_element_by_class_name("nav__button-secondary")
login.click()
user = browser.find_element_by_id("username")#.click()
user.send_keys("MAIL@mail.com")

pword = browser.find_element_by_id("password")
pword.send_keys('PASSWORD')

browser.find_element_by_class_name("login__form_action_container").click()
#enter.click()
#browser.close()  
# 
search_bar = browser.find_element_by_id("ember20")
search_bar.click()
#browser.find_element_by_id("ember18").send_keys("data analyst")
keyboard.write("analista de datos")
keyboard.press_and_release('Return')