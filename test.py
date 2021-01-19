from selenium import webdriver
import unittest
import time

tc = unittest.TestCase('__init__')

driver = webdriver.Chrome('chromedriver.exe')
driver.get('http://automationpractice.com/index.php')
time.sleep(2)
driver.find_element_by_id('search_query_top').send_keys('hola')
driver.find_element_by_name('submit_search').click()
time.sleep(2)

driver.find_element_by_id('center_column')

tc.assertEqual('No results were found for your search "hola"',driver.find_element_by_id('center_column').text)
driver.close()
driver.quit()
