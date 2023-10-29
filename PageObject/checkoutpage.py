from base.test_main import BaseDriver
from selenium.webdriver.common.by import By
from utilities.custom_loggers import LogGen


class CheckOut(BaseDriver):
    back_pack = "//body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/button[1]"
    bolt_tshirt = "//body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[2]/div[2]/button[1]"
    one_sie = "//body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[5]/div[2]/div[2]/button[1]"
    cart_with_badge3_for_checkout = "//body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/a[1]/span[1]"
    continue_shopping = "//body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/button[1]"
    checkout_btn = "//body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/button[2]"
    multiple_item_locator = "//body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/a[1]/span[1]"
    multiple_item_name = "multiple item selected in cart"
    check_out_page_validation_locator = "//body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/span[1]"
    check_out_page_validation_name = "multiple item selected"
    testlog = LogGen.logger()

    def __init__(self, driver):
        self.driver = driver

    def multiple_item_selected(self):
        self.driver.find_element(By.XPATH, self.back_pack).click()
        self.driver.find_element(By.XPATH, self.bolt_tshirt).click()
        self.driver.find_element(By.XPATH, self.one_sie).click()
        print("selecting multiple item test successful")

    def multiple_item_ss(self):
        self.screenshot_image_display(self.multiple_item_locator, self.multiple_item_name)
        print("Add to cart multiple Item selected test successful")

    def checking_out(self):
        self.driver.find_element(By.XPATH, self.cart_with_badge3_for_checkout).click()

    def multiple_item_validation_ss(self):
        self.screenshot_image_display(self.check_out_page_validation_locator, self.check_out_page_validation_name)
        print("Check out page successfully show with selected item displayed test successful")

    def continued_shopping(self):
        self.driver.find_element(By.XPATH, self.continue_shopping).click()
        print("Continue shopping button test successful")

    def check_out_na(self):
        self.driver.find_element(By.XPATH, self.checkout_btn).click()
        # print("Back to check out page test successful")
        self.testlog.info("*** login Test Successful ***")
