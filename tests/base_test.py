import pytest
from utils.logger import setup_logger

logger = setup_logger(__name__)


class BaseTest:

    @staticmethod
    def log_test_start(test_name):
        """Log the start of a test."""
        logger.info(f'======> Starting test: {test_name}')

    @staticmethod
    def assert_page_title(actual_title, expected_title, context=""):
        """Assert that the page title matches the expected title."""
        logger.info(f"{context} Expected title: '{expected_title}', Actual title: '{actual_title}'")
        assert actual_title == expected_title, (
            f"{context} Assertion failed. "
            f"Expected title: '{expected_title}', Actual title: '{actual_title}'"
        )
