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
        driver.get("http://127.0.0.1:8000")
        time.sleep(3)

        try:

            driver.get("http://127.0.0.1:8000/register/")
            time.sleep(3)
            user = "jett_mixed"
            first_name = "Jetty"
            last_name = "Jetterson"
            email = "jetthacker@gmail.com"
            pwd = "gamerMan"
            pwd2 = "gamerMan"

            elem = driver.find_element(By.ID, "id_username")
            elem.send_keys(user)
            elem = driver.find_element(By.ID, "id_first_name")
            elem.send_keys(first_name)
            time.sleep(3)
            elem = driver.find_element(By.ID, "id_last_name")
            elem.send_keys(last_name)
            elem = driver.find_element(By.ID, "id_email")
            elem.send_keys(email)
            elem = driver.find_element(By.ID, "id_password1")
            elem.send_keys(pwd)
            elem = driver.find_element(By.ID, "id_password2")
            elem.send_keys(pwd2)
            time.sleep(3)
            elem.send_keys(Keys.RETURN)
            self.driver.close()
            assert True

        except NoSuchElementException:
            driver.close()
            self.fail("Couldn't register account.")

        time.sleep(2)


if __name__ == "__main__":
    unittest.main()

