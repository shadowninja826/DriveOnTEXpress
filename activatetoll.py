#!/usr/bin/python3
# Install Selenium
#
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

username = "YourLogin"
password = "YourPW"
driver = webdriver.Firefox()
driver.get("https://www.driveontexpress.com")
driver.find_element_by_id("username").send_keys(username)
driver.find_element_by_id("password").send_keys(password)
driver.find_element_by_id("loginButton").click()
#elem.send_keys(Keys.RETURN)
time.sleep(5)
#driver.switchTo().frame("1");
driver.switch_to_frame("main")
driver.find_element_by_id("33893").click()
driver.find_element_by_id("33894").click()
driver.find_element_by_id("33895").click()
driver.find_element_by_id("33896").click()
driver.find_element_by_id("33897").click()
driver.find_element_by_id("33898").click()
driver.find_element_by_id("33899").click()
driver.find_element_by_id("33900").click()
driver.find_element_by_id("33901").click()
driver.find_element_by_id("33902").click()
driver.find_element_by_id("33903").click()
driver.find_element_by_id("33904").click()
driver.find_element_by_id("33905").click()
driver.find_element_by_id("33906").click()
driver.switch_to_default_content()
driver.switch_to_frame("side2")
driver.find_element_by_id("saveHovButton").click()
#driver.close()
