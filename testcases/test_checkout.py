import pytest
from PageObject.checkoutpage import CheckOut
import PageObject
from PageObject.loginpage import LoginPage


@pytest.mark.usefixtures("setup")
class TestCheckOut:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = PageObject.loginpage.LoginPage(self.driver)
        self.checkout = PageObject.checkoutpage.CheckOut(self.driver)

    def test_check_out(self):

        # Open browser and url
        # self.driver = setup

        # Loging in
        self.lp.test_login()

        # Selecting multiple item and taking screenshot
        self.checkout.multiple_item_selected()

        # Clicking cart with 3 item selected or 3 badge
        self.checkout.checking_out()

        # Clicking Continue shopping
        self.checkout.continued_shopping()

        # Back to check out page
        self.checkout.checking_out()

        # Clicking checkout button
        self.checkout.check_out_na()

        self.driver.quit()
