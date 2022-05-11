from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class LoginPage():
    def __init__(self, driver):
        self.driver = driver
        self.username_textbox_id = "email"
        self.password_textbox_id = "pass"
        self.login_button_name = "login"
        self.profile_tab_css_locator = "div[aria-label='Your profile']"
        self.logout_tab_xpath = "//span[normalize-space()='Log Out']"

    def enter_username(self, username):
        self.driver.find_element(By.ID, self.username_textbox_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.password_textbox_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.NAME, self.login_button_name).click()

    def click_profile(self):
        self.driver.find_element(By.CSS_SELECTOR, self.profile_tab_css_locator).click()

    def click_logout(self):
        self.driver.find_element(By.XPATH, self.logout_tab_xpath).click()

