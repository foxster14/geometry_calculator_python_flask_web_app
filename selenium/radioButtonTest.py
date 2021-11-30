import time
import unittest
from selenium import webdriver

class SelectRadioButton(unittest.TestCase):

    #opening browser
    def setUp(self):
        self.driver = webdriver.Chrome('/Users/sarahfox/Downloads/chromedriver')

    def testShapeSelection(self):

        #navigating to  url and maximizing window
        pageUrl = "http://localhost:5000/" #geometry website url
        driver=self.driver
        driver.maximize_window()
        driver.get(pageUrl)

        #cylinder selection test
        time.sleep(1) #wait for 1
        driver.find_element_by_css_selector("input#cylinder").click() #clicks cylinder button
        time.sleep(1) #wait for 1
        driver.find_element_by_css_selector('button').click() #clicks submit
        assert "Cylinder" in driver.title
        time.sleep(1) #wait for 1

        #cone selection test
        driver.get(pageUrl) #navigate back to home page
        time.sleep(1) #wait for 1
        driver.find_element_by_css_selector("input#cone").click() #clicks cone button
        time.sleep(1) #wait for 1
        driver.find_element_by_css_selector('button').click() #clicks submit
        assert "Cone" in driver.title
        time.sleep(1) #wait for 1       

        #sphere selection test
        driver.get(pageUrl) #navigate back to home page
        time.sleep(1) #wait for 1
        driver.find_element_by_css_selector("input#sphere").click() #clicks sphere button
        time.sleep(1) #wait for 1
        driver.find_element_by_css_selector('button').click() #clicks submit
        assert "Sphere" in driver.title
        time.sleep(1) #wait for 1   
    
    #closing browser
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()