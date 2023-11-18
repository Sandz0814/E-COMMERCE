import pytest
from PageObject.checkoutpage import CheckOut
import PageObject
from PageObject.loginpage import LoginPage
from PageObject.checkout_info_page import CheckOutInfo


@pytest.mark.usefixtures("setup")
class TestCheckOutInfo:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = PageObject.loginpage.LoginPage(self.driver)
        self.checkout = PageObject.checkoutpage.CheckOut(self.driver)
        self.checking_out = PageObject.checkout_info_page.CheckOutInfo(self.driver)

    def test_check_out_info(self, setup):
        # Open browser and url
        self.driver = setup

        # Loging in
        self.lp.test_login()

        # Selecting multiple item and taking screenshot
        self.checkout.multiple_item_selected()

        # Clicking cart with 3 item selected or 3 badge
        self.checkout.checking_out()

        # Clicking checkout button
        self.checkout.check_out_na()

        # Checking the cancel button and return to your information page
        self.checking_out.cancel_and_return_to_info()

        # Testing the input details negative scenario
        self.checking_out.details_negative()

        # Clearing the input field
        self.checking_out.clear_field()

        # Testing the input details positive scenario and continue checking out
        self.checking_out.details_positive()

        # Clicking checkout button final
        self.checking_out.check_out_btn()

        self.driver.quit()
