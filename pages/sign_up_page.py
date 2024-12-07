from selenium.common import WebDriverException
from selenium.webdriver.common.by import By
from utils.custom_selenium_webdriver import CustomSeleniumWebDriver
from utils.config_reader import load_config
from utils.logger import setup_logger
from utils.random_data_generator import RandomDataGenerator


class SignUpPage:

    _FIRST_NAME_INPUT_LOCATOR = (By.ID, 'firstname')
    _LAST_NAME_INPUT_LOCATOR = (By.ID, 'lastname')
    _EMAIL_INPUT_LOCATOR = (By.ID, 'email_address')
    _PASSWORD_INPUT_LOCATOR = (By.ID, 'password')
    _CONFIRM_PASSWORD_INPUT_LOCATOR = (By.ID, 'password-confirmation')
    _CREATE_AN_ACCOUNT_BUTTON_LOCATOR = (By.XPATH, '//button[@type="submit" and @title="Create an Account"]')

    def __init__(self, driver):
        self.driver = CustomSeleniumWebDriver(driver)
        self.logger = setup_logger()
        self.data_generator = RandomDataGenerator()

    def get_sign_up_page_url(self) -> str:
        """
        Retrieves the sign-up page URL from the configuration file.

        :return: URL of the sign-up page.
        :raises KeyError: If no sign-up page URL is found in the configuration file.
        :raises Exception: if an error occurred while retrieving the sign-up page URL from the configuration file.
        """
        self.logger.info(f'********** {self.get_sign_up_page_url.__name__}() **********')
        try:
            config = load_config()
            sign_up_page_url = config['sign_up_page_url']
            return sign_up_page_url
        except KeyError as e:
            self.logger.error(f'"sign_up_page_url" not found in the configuration file. Error: {e}')
        except Exception as e:
            self.logger.error(f'An error occurred while retrieving the sign-up page URL from the configuration file. '
                              f'Error: {e}')

    def get_sign_up_title_page(self) -> str:
        """
         Retrieves the title of the sign-up page.

        :return: Title of the sign-up page.
        """
        self.logger.info(f'********** {self.get_sign_up_title_page.__name__}() **********')
        try:
            sign_up_page_url = self.get_sign_up_page_url()
            self.driver.navigate_to_url(sign_up_page_url)
            sign_up_title_page = self.driver.get_title()
            return sign_up_title_page
        except WebDriverException as e:
            self.logger.error(f'An error occurred while retrieving the sign-up page title. Error: {e}')

    def create_account(self, first_name, last_name, email, password):
        """

        :return:
        """
        self.logger.info(f'********** {self.create_account.__name__}() **********')
        try:
            sign_up_page_url = self.get_sign_up_page_url()
            self.driver.navigate_to_url(sign_up_page_url)
            self.logger.info(f'Typing First name: {first_name}')
            self.driver.type_text(self._FIRST_NAME_INPUT_LOCATOR, first_name)
            self.logger.info(f'Typing Last name: {last_name}')
            self.driver.type_text(self._LAST_NAME_INPUT_LOCATOR, last_name)
            self.logger.info(f'Typing Email: {email}')
            self.driver.type_text(self._EMAIL_INPUT_LOCATOR, email)
            self.logger.info(f'Typing Password: {password}')
            self.driver.type_text(self._PASSWORD_INPUT_LOCATOR, password)
            self.logger.info(f'Typing confirmation password: {password}')
            self.driver.type_text(self._CONFIRM_PASSWORD_INPUT_LOCATOR, password)
            self.logger.info('Clicking create account button...')
            self.driver.click(self._CREATE_AN_ACCOUNT_BUTTON_LOCATOR)
        except:
            pass
