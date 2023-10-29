from selenium.webdriver.common.by import By
from base.test_main import BaseDriver
from utilities.custom_loggers import LogGen


class CheckOutInfo(BaseDriver):

    cancel_btn = "//body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/button[1]"
    back_to_info_btn = "//body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/button[2]"
    first_name_field = "firstName"
    last_name_field = "lastName"
    postal_code_field = "postalCode"
    submit_btn = "//body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/input[1]"
    ss_of_negative_info_test = "//body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[1]/div[4]/h3[1]"
    negative_info_test_error = "Required field error"
    check_out_button = "//body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/input[1]"
    testlog = LogGen.logger()

    def __init__(self, driver):
        self.driver = driver

    def cancel_and_return_to_info(self):
        self.driver.find_element(By.XPATH, self.cancel_btn).click()
        self.driver.find_element(By.XPATH, self.back_to_info_btn).click()

    def clear_field(self):
        self.driver.find_element(By.NAME, self.first_name_field).clear()
        self.driver.find_element(By.NAME, self.last_name_field).clear()
        self.driver.find_element(By.NAME, self.postal_code_field).clear()

    def details_negative(self):
        self.clear_field()
        self.driver.find_element(By.NAME, self.first_name_field).send_keys("")
        self.driver.find_element(By.NAME, self.last_name_field).send_keys("Jimena")
        self.driver.find_element(By.NAME, self.postal_code_field).send_keys("12345")
        self.driver.find_element(By.XPATH, self.submit_btn).click()

    def error_message_ss(self):
        self.screenshot_image_display(self.ss_of_negative_info_test, self.negative_info_test_error)

    def details_positive(self):
        self.driver.find_element(By.NAME, self.first_name_field).clear()
        self.driver.find_element(By.NAME, self.first_name_field).send_keys("sandro")
        self.driver.find_element(By.NAME, self.last_name_field).clear()
        self.driver.find_element(By.NAME, self.last_name_field).send_keys("Jimena")
        self.driver.find_element(By.NAME, self.postal_code_field).clear()
        self.driver.find_element(By.NAME, self.postal_code_field).send_keys("12345")
        print("input details successful")

    def check_out_btn(self):
        self.driver.find_element(By.XPATH, self.check_out_button).click()

        self.testlog.info("*** login Test Successful ***")
