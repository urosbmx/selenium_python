import time

import pytest
from selenium.webdriver.common.by import By
import logging
logger = logging.getLogger(__name__)

@pytest.mark.page
class TestsPage:

    def test_first_test(self):
        logger.info("This test is pass")
        pass

    def test_secunde_test(self):
        logger.info("This test is pass")
        pass

    def test_third_test(self):
        logger.info("This test is pass")
        pass

    def test_pages_test(self):
        logger.info("This test is pass")
        pass

    def test_first_test(self):
        logger.info("This test is pass")
        pass