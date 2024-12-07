import pytest
from pages.sign_up_page import SignUpPage
from utils.logger import setup_logger
from utils.custom_selenium_webdriver import CustomSeleniumWebDriver
from tests.base_test import BaseTest


logger = setup_logger()


class TestSignUpPage(BaseTest):

    @pytest.mark.run(order=1)
    def test_sign_up_page_title(self, driver):
        """Verify that the title of the sign-up page is correct."""
        self.log_test_start(self.test_sign_up_page_title.__name__)
        sign_up_page = SignUpPage(driver)
        actual_title = sign_up_page.get_sign_up_title_page()
        expected_title = 'Create New Customer Account'
        self.assert_page_title(actual_title, expected_title, context="Sign-Up Page")

    @pytest.mark.run(order=2)
    def test_sign_up_process(self, driver, generated_data):
        """Verify the sign-up process and the resulting page title."""
        self.log_test_start(self.test_sign_up_process.__name__)
        sign_up_page = SignUpPage(driver)
        sign_up_page.create_account(
            first_name=generated_data['first_name'],
            last_name=generated_data['last_name'],
            email=generated_data['email'],
            password=generated_data['password']
        )
        web_driver = CustomSeleniumWebDriver(driver)
        actual_title = web_driver.get_title()
        expected_title = 'My Account'
        self.assert_page_title(actual_title, expected_title, context="After Sign-Up")
