'''example script
setup: find your Python installation package. go to dir "Scripts" under it.
pip install selenium
File -> Settings -> Inside your project's name -> Project Interpreter ->
click on "+" button -> search for selenium (current version 3.141.0) ->
click on install -> restart PyCharm.
put geckodriver in same position as your script (your project)

Skills demonstrated:
set up Selenium
get driver
go to a url
use by_id, by_css, by_xpath to locate element
actions: click, send text (keys)
assert: in source, string comparison
'''


from selenium import webdriver
from selenium.webdriver.common.keys import Keys     # needed to send key
import unittest                                     # needed for assert

driver = webdriver.Firefox()
home_url = "https://www.seleniumeasy.com/test/"
driver.get(home_url)       # go to home page

# find element by xpath
#element_list = {"input_forms": "#treemenu > li > ul > li:nth-child(1) > a"}
#by css: #treemenu > li > ul > li:nth-child(1) > a

# find element by partial link text
element_list = {"input_forms": "Input"}
element_list = {"simple_forms": "Simple Form"}
# element_list = {"input_forms": "Input"}
# element_list = {"input_forms": "Input"}
# element_list = {"input_forms": "Input"}
#   //a[@href='/docs/configuration']#treemenu > li > ul > li:nth-child(1) > a
#print(element_link_text["input_forms"])

input_form = driver.find_element_by_xpath('//*[@id="treemenu"]/li/ul/li[1]/a').click()     # click "Input Forms"
#element = driver.find_element_by_partial_link_text(element_list["input_forms"]).click()
simple_form_demo = driver.find_element_by_xpath('//*[@id="treemenu"]/li/ul/li[1]/ul/li[1]/a').click()   # simple form

#simple_form_demo = "#easycont > div > div.col-md-6.text-left > div:nth-child(4) > div.panel-heading"    #click Simple Input Form
#simple_input_label = driver.find_element_by_css_selector(simple_form_demo)      # by css and verify txt displayed
assert "Single Input Field" in driver.page_source

enter_message_id = "user-message"
driver.find_element_by_id(enter_message_id).send_keys("hello")
driver.find_element_by_xpath('//button[text()="Show Message"]').click()         # using text on button to identify
display_text = driver.find_element_by_id("display").text                        # assert using text in technique
assert display_text == "hello"
driver.close()