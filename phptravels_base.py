"""this is the base class for my phptravels example"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys     # needed to send text / key
import unittest  # needed for assert
import HtmlTestRunner

class phptravel_base():

    def setUp(self):
        self.driver = webdriver.Firefox()
        home_url = "https://www.seleniumeasy.com/test/"
        self.driver.get(home_url)  # go to home page

        # def click(self, by_locator):
        #     WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()
        #
        # # this function asserts comparison of a web element's text with passed in text.
        # def assert_element_text(self, by_locator, element_text):
        #     web_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        #     assert web_element.text == element_text
        #
        # # this function performs text entry of the passed in text, in a web element whose locator is passed to it.
        # def enter_text(self, by_locator, text):
        #     return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)
        #
        # # this function checks if the web element whose locator has been passed to it, is enabled or not and returns
        # # web element if it is enabled.
        # def is_enabled(self, by_locator):
        #     return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        #
        # # this function checks if the web element whose locator has been passed to it, is visible or not and returns
        # # true or false depending upon its visibility.
        # def is_visible(self, by_locator):
        #     element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        #     return bool(element)
        #
        # # this function moves the mouse pointer over a web element whose locator has been passed to it.
        # def hover_to(self, by_locator):
        #     element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        #     ActionChains(self.driver).move_to_element(element).perform()

    def get_driver(self):
        return self.driver

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    #unittest.main()
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='c://temp/phptravels_test.html'))