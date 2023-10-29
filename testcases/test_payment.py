import pytest
from PageObject.checkoutpage import CheckOut
import PageObject
from PageObject.loginpage import LoginPage
from PageObject.checkout_info_page import CheckOutInfo
from PageObject.payment_overview_page import PaymentOverView


@pytest.mark.usefixtures("setup")
class TestCheckOutInfo:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = PageObject.loginpage.LoginPage(self.driver)
        self.checkout = PageObject.checkoutpage.CheckOut(self.driver)
        self.checking_out = PageObject.checkout_info_page.CheckOutInfo(self.driver)
        self.payment_over_view = PageObject.payment_overview_page.PaymentOverView(self.driver)

    def test_check_out_info(self):
        # Open browser and url
        # self.driver = setup

        # Loging in
        self.lp.test_login()

        # Selecting multiple item and taking screenshot
        self.checkout.multiple_item_selected()

        # Clicking cart with 3 item selected or 3 badge
        self.checkout.checking_out()

        # Clicking checkout button
        self.checkout.check_out_na()

        # Testing the input details positive scenario and continue checking out
        self.checking_out.details_positive()

        # Clicking checkout button final
        self.checking_out.check_out_btn()

        # Checking the computation of all item to final total price and click finish and back to main page
        self.payment_over_view.item_computation()

        self.driver.quit()




