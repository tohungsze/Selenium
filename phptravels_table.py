"""This tests table
Illustrates how to
count number of rows (visible / total) and columns """

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
for i in range(len(visible_row_list)):
    for rows in driver.find_elements_by_xpath('//*[@id="myTable"]/tr["+str(i)+"]/td[1]'):
        print("Rows:")
        for j in range(len(column_list)):
            for row_element in driver.find_elements_by_xpath('//*[@id="myTable"]/tr["+str(i)+"]/td["+str(j)+"]'):
                print("row data =",row_element.text)
# not sure why keeps printing "row data" after row 5 but not before


driver.close()

