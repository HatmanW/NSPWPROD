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
        driver = self.driver
        driver.maximize_window()
        user = ""
        pwd = ""
        driver.get("http://hatmanwgrey.pythonanywhere.com/")

        time.sleep(3)
        elem = driver.find_element(By.ID,"id_username")
        elem.send_keys(user)
        elem = driver.find_element(By.ID,"id_password")
        elem.send_keys(pwd)
        time.sleep(3)
        elem.send_keys(Keys.RETURN)

        time.sleep(5)

        try:
            # verify Book List exists on new screen after clicking "All books" button
            # note that this test requires at least one book in the database to be successful
            elem = driver.find_element(By.LINK_TEXT, "Home")
            driver.find_element(By.XPATH, "//a[contains(., 'Home')]").click()
            time.sleep(1)
            elem = driver.find_element(By.LINK_TEXT, "All Products")
            driver.find_element(By.XPATH, "//a[contains(., 'All Products')]").click()
            time.sleep(1)
            driver.find_element(By.XPATH, "//a[contains(., 'Home')]").click()
            time.sleep(1)
            elem = driver.find_element(By.LINK_TEXT, "Men's")
            driver.find_element(By.XPATH, "//a[contains(., 'Men's')]").click()
            time.sleep(1)
            driver.find_element(By.XPATH, "//a[contains(., 'Home')]").click()
            time.sleep(1)
            elem = driver.find_element(By.LINK_TEXT, "Women's")
            driver.find_element(By.XPATH, "//a[contains(., 'Women's')]").click()
            time.sleep(1)
            driver.find_element(By.XPATH, "//a[contains(., 'Home')]").click()
            time.sleep(1)
            elem = driver.find_element(By.LINK_TEXT, "Kids's")
            driver.find_element(By.XPATH, "//a[contains(., 'Kids's')]").click()
            time.sleep(1)
            driver.find_element(By.XPATH, "//a[contains(., 'Home')]").click()
            time.sleep(1)
            self.driver.close()
            assert True

        except NoSuchElementException:
            driver.close()
            self.fail("User other then administrator can see .")

        time.sleep(2)


if __name__ == "__main__":
    unittest.main()