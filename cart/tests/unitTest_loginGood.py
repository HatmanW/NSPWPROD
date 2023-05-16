#import
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class ll_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_ll(self):
        #Pre-requisties #3
        user = "Testuser1"
        pwd = "testuser123!"

        driver = self.driver
        driver.maximize_window()
        '''this meets step 1 for website open, as well as step 3 for
        opening the django admin page. 
        This also meets step 4, and should successfully log into the site 
        as the admin testuser account'''
        driver.get("http://127.0.0.1:8000/admin")
        #step 4
        elem = driver.find_element(By.ID,"id_username")
        elem.send_keys(user)
        elem = driver.find_element(By.ID,"id_password")
        elem.send_keys(pwd)
        time.sleep(3)
        elem.send_keys(Keys.RETURN)
        #step 5
        driver.get("http://hatmanwgrey.pythonanywhere.com/")
        time.sleep(3)
        #step 6
        try:
            # attempt to find the 'Logout' button - if found, logged in
            elem = driver.find_element(By.LINK_TEXT, "Logout")
            driver.close()
            assert True

        except NoSuchElementException:
            driver.close()
            self.fail("Login Failed - user may not exist")

            time.sleep(3)

if __name__ == "__main__":
    unittest.main(warnings='ignore')