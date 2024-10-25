import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import logging

logger = logging.getLogger(__name__)
@pytest.fixture(scope="session")
def setup_chrome(app_config):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    logger.info("Google Chrome Driver Created")
    driver.get(f"{app_config.base_url}/practice-test-login/")
    logger.info("Web page opened")
    driver.maximize_window()
    logger.info("Windows maximized")
    yield driver
    driver.quit()

@pytest.fixture
def setup_safari(app_config):
    driver = webdriver.Safari()
    driver.get(f"{app_config.base_url}/practice-test-login/")
    driver.maximize_window()
    yield driver
    driver.quit()