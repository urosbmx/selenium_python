import time

import pytest
from selenium.webdriver.common.by import By
import logging
logger = logging.getLogger(__name__)


@pytest.mark.login_regression
class TestsLoginPage:
    def test_with_incorrect_user(self, setup_chrome):
        username = setup_chrome.find_element(By.ID, "username")
        password = setup_chrome.find_element(By.ID, "password")
        submit = setup_chrome.find_element(By.CLASS_NAME, "btn")

        username.send_keys("incorrectUser")
        logger.info("Incorrect username inputted")
        password.send_keys("Password123")
        logger.info("Correct password inputted")
        submit.click()
        time.sleep(2)
        error = setup_chrome.find_element(By.ID,"error").text
        assert error == "Your username is invalid!"
        logger.info("Error message validated")
        logger.info("test pass")



    def test_with_incorrect_password(self, setup_chrome):
        username = setup_chrome.find_element(By.ID, "username")
        password = setup_chrome.find_element(By.ID, "password")
        submit = setup_chrome.find_element(By.CLASS_NAME, "btn")

        username.send_keys("student")
        password.send_keys("incorrectPassword")
        submit.click()
        time.sleep(2)
        error = setup_chrome.find_element(By.ID,"error").text
        assert error == "Your password is invalid!"

    def test_with_valid_data(self, setup_chrome):
        username = setup_chrome.find_element(By.ID, "username")
        password = setup_chrome.find_element(By.ID, "password")
        submit = setup_chrome.find_element(By.CLASS_NAME, "btn")

        username.send_keys("student")
        password.send_keys("Password123")
        submit.click()
        time.sleep(2)
        url = setup_chrome.current_url
        assert url == "https://practicetestautomation.com/logged-in-successfully/"
        time.sleep(2)





