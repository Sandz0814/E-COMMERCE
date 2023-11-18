from PageObject.credentials import user, passw
from PageObject.credentials import username, passwords, login
from selenium.webdriver.common.by import By
from base.test_main import BaseDriver
from utilities.custom_loggers import LogGen


class LoginPage(BaseDriver):

    locator = '//*[@id="header_container"]/div[2]/span'
    image_name = "Test login SS"
    testlog = LogGen.logger()

    def __init__(self, driver):
        self.driver = driver

    def test_login(self):
        self.driver.find_element(By.NAME, username).clear()
        self.driver.find_element(By.NAME, username).send_keys(user)
        self.driver.find_element(By.NAME, passwords).clear()
        self.driver.find_element(By.NAME, passwords).send_keys(passw)
        self.driver.find_element(By.NAME, login).click()

    def ss_login_page(self):
        self.screenshot_image_display(self.locator, self.image_name)

        self.testlog.info("*** login Test Successful ***")

















