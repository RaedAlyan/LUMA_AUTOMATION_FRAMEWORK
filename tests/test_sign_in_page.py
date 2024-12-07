import pytest
from pages.sign_in_page import SignInPage
from utils.logger import setup_logger
from utils.custom_selenium_webdriver import CustomSeleniumWebDriver
from tests.base_test import BaseTest

logger = setup_logger()


class TestSignInPage(BaseTest):

    def test_sign_in_page_title(self, driver):
        """Verify that the title of the sign-in page is correct."""
        self.log_test_start(self.test_sign_in_page_title.__name__)
        sign_in_page = SignInPage(driver)
        actual_title = sign_in_page.get_sign_in_title_page()
        expected_title = 'Customer Login'
        self.assert_page_title(actual_title, expected_title, context="Sign-In Page")

    def test_sign_in_process(self, driver, generated_data):
        """Verify the sign-in process and the resulting page title."""
        self.log_test_start(self.test_sign_in_process.__name__)
        sign_in_page = SignInPage(driver)
        sign_in_page.sign_in(email=generated_data['email'], password=generated_data['password'])
        web_driver = CustomSeleniumWebDriver(driver)
        actual_title = web_driver.get_title()
        expected_title = 'My Account'
        self.assert_page_title(actual_title, expected_title, context="After Sign-In")
