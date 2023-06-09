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
        #Pre-requisties #3 as testuser2
        user = "testuser2"
        pwd = "test123!"

        driver = self.driver
        driver.maximize_window()
        '''this meets step 1 for website open, as well as step 3 for
        opening the django admin page. 
        This also meets step 4, and should successfully log into the site 
        as the admin testuser account'''
        driver.get("http://127.0.0.1:8000/admin/")
        time.sleep(1)
        #step 4
        elem = driver.find_element(By.ID,"id_username")
        elem.send_keys(user)
        elem = driver.find_element(By.ID,"id_password")
        elem.send_keys(pwd)
        time.sleep(3)
        elem.send_keys(Keys.RETURN)
        time.sleep(1)
        #step 6
        try:
            # attempt to find the 'Log out' button - if found, logged in.
            elem = driver.find_element(By.ID, "id_password")
            #elem = driver.find_element(By.LINK_TEXT, "Please enter the correct username and password for a staff account. Note that both fields may be case-sensitive.")
            driver.close()
            assert True

        except NoSuchElementException:
            driver.close()
            self.fail("Unautorized user can log into administration page.")

            time.sleep(3)

if __name__ == "__main__":
    unittest.main(warnings='ignore')