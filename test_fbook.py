import time
from selenium import webdriver
from Pages.LoginPage import LoginPage
import unittest
import HtmlTestRunner


class searchFacebook(unittest.TestCase):
    baseURL = "https://www.facebook.com/"
    username = "8605128806"
    password = "DDPRp-YHP.+4RkE"

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

    def test_log(self):
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Facebook – log in or sign up":
            assert True
            print("log test completed")


    def test_login(self):
        self.driver.get(self.baseURL)
        login = LoginPage(driver=self.driver)
        login.enter_username(self.username)
        login.enter_password(self.password)
        login.click_login()
        login.click_profile()
        time.sleep(4)
        login.click_logout()
        act_title = self.driver.title
        if act_title =="Facebook – log in or sign up":
            assert True
            print("login test completed")

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if __name__ == "main":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/SHRISHA/TestProject/Reports"))


