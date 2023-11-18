import base.test_main
from PageObject.loginpage import LoginPage
import pytest
from base.test_main import BaseDriver


@pytest.mark.usefixtures("setup")
class TestLogging(BaseDriver):

    @pytest.fixture(autouse=True)
    def class_setup(self, setup):
        self.lp = LoginPage(setup)
        self.bp = base.test_main.BaseDriver()

    def test_log_in_page(self, setup):
        self.driver = setup
        self.lp = LoginPage(self.driver)

        self.lp.test_login()

        self.lp.page_scroll()

        self.lp.ss_login_page()


