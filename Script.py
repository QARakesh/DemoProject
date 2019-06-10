import os
from time import sleep
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
class MMsignup(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver:webdriver=webdriver.Chrome()
        cls.driver.maximize_window()
        sleep(1)
    def test_signup(self):
        self.driver.get("https://www.mondaymorning.in")
        self.driver.execute_script("window.alert('Please Sign UP');")
        sleep(2)
        alert = self.driver.switch_to_alert()
        sleep(1)
        alert.accept()
        self.driver.find_element_by_xpath("(//A[@class='btn-job'])").click()
        sleep(1)
        self.driver.find_element_by_xpath("(//INPUT[@type='text'])[2]").send_keys("Rakesh")
        sleep(1)
        self.driver.find_element_by_xpath("(//INPUT[@type='text'])[3]").send_keys("Patra")
        sleep(1)
        self.driver.find_element_by_xpath("(//INPUT[@type='email'])[1]").send_keys("rakesh_patra+001@mondaymorning.in")
        sleep(1)
        self.driver.find_element_by_id("password").send_keys("1234")
        sleep(1)
        self.driver.find_element_by_xpath("(//INPUT[@class='log-btn'])[2]").submit()
        sleep(2)
    @classmethod
    def tearDownClass(cls):
        #cls.driver:webdriver=webdriver.Chrome()
        cls.driver.close()

if __name__=='__main__':
    unittest.main()

