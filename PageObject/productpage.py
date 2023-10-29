from selenium.webdriver.common.by import By
from base.test_main import BaseDriver


class ProductPages(BaseDriver):

    filter_click = "//body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/span[1]/select[1]"
    a_to_z_select = "//body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/span[1]/select[1]/option[1]"
    z_to_a_select = "//body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/span[1]/select[1]/option[2]"
    low_to_hi_select = "//body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/span[1]/select[1]/option[3]"
    hi_to_lo_select = "//body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/span[1]/select[1]/option[4]"
    product1_click = "//body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]/img[1]"
    product_page_validation = "//bo# Add to cart on selected item"
    add_to_cart_click = "//body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/button[1]"
    add_to_cart_badge = "//body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/a[1]/span[1]"
    remove_item_click = "//body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/button[1]"
    back_to_product_click = "//body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/button[1]"
    add_to_cart1_click = "//body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/button[1]"
    remove_item1_click = "//body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/button[1]"
    cart_no_item = "//body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/button[1]"
    add_to_cart_main_page = "//body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/button[1]"
    cart_image_click = "//body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/a[1]"
    check_out_page_validation = "//body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/span[1]"
    product3_click = "//body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[4]/div[2]/div[2]/button[1]"
    continue_shopping_click = "//body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/button[1]"
    checkout_button_click = "//body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/button[2]"
    Checkout_remove_btn_click = "//body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[2]/div[2]/button[1]"
    checkout_btn_click_validation = "//body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/span[1]"
    add_cart_locator = '//body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/a[1]/span[1]'
    add_cart_image_name = "Product page "
    product_page_locator = "//div[@id='']"
    product_image = "Item selected page"
    remove_item_locator = "//body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/a[1]"
    remove_item_name = "Removed Item to cart"
    add_item_ss_locator = "//body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/a[1]/span[1]"
    add_item_ss_name = "Item added to cart in main page"
    remove_item_in_main_page = "//body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/a[1]"
    remove_item_in_main_name = "Item removed to cart in main page"

    def __init__(self, driver):
        self.driver = driver

    def filters(self):
        filter_x_paths = [self.a_to_z_select, self.z_to_a_select, self.low_to_hi_select, self.hi_to_lo_select]

        for xpath in filter_x_paths:
            self.driver.find_element(By.XPATH, self.filter_click).click()
            self.driver.find_element(By.XPATH, xpath).click()

    def product_page(self):
        self.driver.find_element(By.XPATH, self.product1_click).click()

    # Page validation. product should display and taking Screen shot for successful test reference.
    def ss_product(self):
        self.screenshot_image_display(self.product_page_locator, self.product_image)
        print("Selecting product test successful")

    def add_to_cart(self):
        self.driver.find_element(By.XPATH, self.add_to_cart_click).click()

    # Taking Screenshot of the added item on the cart as successful reference.
    def ss_add_to_cart(self):
        self.screenshot_image_display(self.add_cart_locator, self.add_cart_image_name)
        print("Add to cart successful")

    def remove_item(self):
        self.driver.find_element(By.XPATH, self.remove_item_click).click()

    # Taking Screenshot of the removed item on the cart as successful reference.
    def ss_remove_item_to_cart(self):
        self.screenshot_image_display(self.remove_item_locator, self.remove_item_name)
        print("Removed Item successful successful")

    def back_to_main_page(self):
        self.driver.find_element(By.XPATH, self.back_to_product_click).click()
        print("Back to main page successful")

    def product_page1(self):
        self.driver.find_element(By.XPATH, self.add_to_cart_main_page).click()

        #  Taking Screenshot if the item is added to cart badge count = 1
    def ss_add_item(self):
        self.screenshot_image_display(self.add_item_ss_locator, self.add_item_ss_name)
        print("Item successfully added in the main page")

    def remove_item_main_page(self):
        self.driver.find_element(By.XPATH, self.remove_item1_click).click()

    def ss_remove_item_main_page(self):
        self.screenshot_image_display(self.remove_item_in_main_page, self.remove_item_in_main_name)

        print("***** Product testing ended *****")







