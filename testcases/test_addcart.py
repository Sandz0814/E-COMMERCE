import pytest
from PageObject.productpage import ProductPages
from PageObject.loginpage import LoginPage
import time
import PageObject


@pytest.mark.usefixtures("setup")
class TestProduct:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = PageObject.loginpage.LoginPage(self.driver)
        self.product = PageObject.productpage.ProductPages(self.driver)

    def test_product(self):
        # Open browser and url
        # self.driver = setup

        self.lp.test_login()

        #  Testing the Filter function
        self.product.filters()

        #  Testing the Selected product by clicking the image and clicking add to cart.
        self.product.product_page()

        #  Add to cart button functionality testing. Badge image will display number of item added to cart. count = 1
        self.product.add_to_cart()

        # Removing the selected Item and go back to the main page
        self.product.remove_item()

        # Back to main page
        self.product.back_to_main_page()

        # Add to cart directly from main page
        self.product.product_page1()

        # Removed Item from main page
        self.product.remove_item_main_page()
        time.sleep(3)
        self.driver.quit()
