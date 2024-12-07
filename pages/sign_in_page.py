from selenium.webdriver.common.by import By
from utils.custom_selenium_webdriver import CustomSeleniumWebDriver
from utils.config_reader import load_config
from utils.logger import setup_logger
from selenium.common import WebDriverException


class SignInPage:

    _EMAIL_INPUT_LOCATOR = (By.ID, 'email')
    _PASSWORD_INPUT_LOCATOR = (By.ID, 'pass')
    _SIGN_IN_BUTTON_LOCATOR = (By.XPATH, '//button[@type="submit" and @class="action login primary"]')

    def __init__(self, driver):
        self.driver = CustomSeleniumWebDriver(driver)
        self.logger = setup_logger()

    def get_sign_in_page_url(self) -> str:
        """
        Retrieves the sign-in page URL from the configuration file.

        :return: URL of the sign-in page.
        :raises KeyError: If no sign-in page URL is found in the configuration file.
        :raises Exception: if an error occurred while retrieving the sign-in page URL from the configuration file.
        """
        self.logger.info(f'********** {self.get_sign_in_page_url.__name__}() **********')
        try:
            config = load_config()
            sign_in_page_url = config['sign_in_page_url']
            return sign_in_page_url
        except KeyError as e:
            self.logger.error(f'"sign_in_page_url" not found in the configuration file. Error: {e}')
        except Exception as e:
            self.logger.error(f'An error occurred while retrieving the sign-in page URL from the configuration file. '
                              f'Error: {e}')

    def sign_in(self, email: str, password: str) -> None:
        """

        :param email:
        :param password:
        :return:
        """
        sign_in_page_url = self.get_sign_in_page_url()
        self.driver.navigate_to_url(sign_in_page_url)
        self.driver.type_text(self._EMAIL_INPUT_LOCATOR, email)
        self.driver.type_text(self._PASSWORD_INPUT_LOCATOR, password)
        self.driver.click(self._SIGN_IN_BUTTON_LOCATOR)

    def get_sign_in_title_page(self) -> str:
        """
         Retrieves the title of the sign-in page.

        :return: Title of the sign-in page.
        """
        self.logger.info(f'********** {self.get_sign_in_title_page.__name__}() **********')
        try:
            sign_in_page_url = self.get_sign_in_page_url()
            self.driver.navigate_to_url(sign_in_page_url)
            sign_in_title_page = self.driver.get_title()
            return sign_in_title_page
        except WebDriverException as e:
            self.logger.error(f'An error occurred while retrieving the sign-in page title. Error: {e}')
