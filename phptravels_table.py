"""This tests table
Illustrates how to
count number of rows (visible / total) and columns
using visible filter """

from selenium import webdriver
from selenium.webdriver.common.keys import Keys     # needed to send key
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Firefox()
home_url = "https://www.seleniumeasy.com/test/"
driver.get(home_url)       # go to home page


# for the table
driver.find_element_by_xpath('//*[@id="treemenu"]/li/ul/li[3]/a').click()               # Table
driver.find_element_by_xpath('//*[@id="treemenu"]/li/ul/li[3]/ul/li[1]/a').click()      # Pagination

column_list = []
column_list = driver.find_elements_by_xpath('/html/body/div[2]/div/div[2]/section/div/table/thead/tr/th')
print("number of columns =", len(column_list) - 1)     # minus 1 because first column is row number

row_list = []
total_row_list = driver.find_elements_by_xpath('//*[@id="myTable"]/tr')
visible_row_list = driver.find_elements_by_xpath('//*[@id="myTable"]/tr[not(contains(@style,"display: none;"))]')
print("TOTAL number of rows displayed=", len(total_row_list))         # this is the TOTAL, not just displayed
print("VISIBLE number of rows displayed=", len(visible_row_list))         # this is the rows displayed / visible

row_elements = []   # iterating through each row
row_elements = driver.find_elements_by_xpath('//*[@id="myTable"]/tr[not(contains(@style,"display: none;"))]/td')
# row_elements has 35 elements

# printing only first 5 and adding a print line to mark row number
for i in range(len(row_elements)):
    if i % 7 == 0:          # calculate the row number and print a heading, the list contains all 13 * 7 elements
        n = int(i/7 +1)
        print("Row:", n)
    print(row_elements[i].text)


driver.close()

