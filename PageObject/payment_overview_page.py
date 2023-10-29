from selenium.webdriver.common.by import By
from base.test_main import BaseDriver
from utilities.custom_loggers import LogGen

class PaymentOverView(BaseDriver):

    payment_overview_locator = "//body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[8]"
    payment_overview_image = "Payment overview"
    success_order_locator = "//body[1]/div[1]/div[1]/div[1]/div[2]/h2[1]"
    success_order_image = "Add to cart transaction successful"
    back_pack_price_element = "//body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[2]/div[2]/div[1]"
    bolt_tshirt_price_element = "//body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[4]/div[2]/div[2]/div[1]"
    one_sie_price_element = "//body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[5]/div[2]/div[2]/div[1]"
    finish_btn = "//body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[9]/button[2]"
    back_to_home_btn = "//body[1]/div[1]/div[1]/div[1]/div[2]/button[1]"
    testlog = LogGen.logger()

    def __init__(self, driver):
        self.driver = driver

    def item_computation(self):
        backpack_price = self.driver.find_element(By.XPATH, self.back_pack_price_element).text
        bolt_tshirt_price = self.driver.find_element(By.XPATH, self.bolt_tshirt_price_element).text
        one_sie_price = self.driver.find_element(By.XPATH, self.one_sie_price_element).text

        backpack_price = backpack_price[1:]
        bolt_tshirt_price = bolt_tshirt_price[1:]
        one_sie_price = one_sie_price[1:]

        print(backpack_price)
        print(bolt_tshirt_price)
        print(one_sie_price)

        x = float(backpack_price)
        y = float(bolt_tshirt_price)
        z = float(one_sie_price)

        total_price = x + y + z
        less_tax = float(total_price * .08)
        final_price = total_price + less_tax

        print(f'Tax is: {less_tax}')
        print(f'Total price is: {total_price}')
        print(f'Final Price is: {final_price}')
        print(" Item computation validation passed")

        # Taking Screenshot of Payment overview
        self.screenshot_image_display(self.payment_overview_locator, self.payment_overview_image)

        # Finish Button
        self.driver.find_element(By.XPATH, self.finish_btn).click()

        # Taking Screenshot of Payment overview
        self.screenshot_image_display(self.success_order_locator, self.success_order_image)

        print("Customer order successfully placed ")

        # Back to home button
        self.driver.find_element(By.XPATH, self.back_to_home_btn).click()

        self.testlog.info("*** Payment overview Test Successful ***")





