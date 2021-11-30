import time
import unittest
from selenium import webdriver

class SearchFormsCheck(unittest.TestCase):
    #Opening browser.
    def setUp(self):
        self.driver = webdriver.Chrome('/Users/sarahfox/Downloads/chromedriver')
    #Testing Single Input Field.    
    def test_singleInputField(self):
        pageUrl = "http://www.seleniumeasy.com"
        driver=self.driver
        driver.maximize_window()
        driver.get(pageUrl)
        time.sleep(5) # Let the user actually see something!
        #Finding "Search box" input text field by id. And sending keys(entering data) in it.
        eleSearch = driver.find_element_by_id("edit-search-block-form--2")
        eleSearch.clear()
        eleSearch.send_keys("Test Python" + "\n")
        time.sleep(5) # Let the user actually see something!
        #Finding "First Search Result" link element by css selector class name.
        eleFirstSearchResult=driver.find_element_by_class_name("search-result")
     
        #Checking whether the resulting page contains a title with "First Example".
        assert "First Example" in eleFirstSearchResult.text
 
    # Closing the browser.
    def tearDown(self):
        self.driver.close()
# This line sets the variable “__name__” to have a value “__main__”.
# If this file is being imported from another module then “__name__” will be set to the other module's name.
if __name__ == "__main__":
    unittest.main()