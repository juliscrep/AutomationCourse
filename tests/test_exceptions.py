import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


@pytest.fixture()
def driver():
    print("Creating chrome driver")
    my_driver = webdriver.Firefox()
    yield my_driver
    print("Closing chrome driver")
    my_driver.quit()


@pytest.mark.exceptions
class TestExceptions:

    def test_no_such_element_exception(self, driver):

        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Click Add button
        add_button_locator = driver.find_element(By.ID, "add_btn")
        add_button_locator.click()

        # Verify Row 2 input field is displayed
        row_2_input_locator = driver.find_element(By.XPATH, "//div[@id='row2']/input")
        assert row_2_input_locator.is_displayed()

    def test_element_not_interactable_exception(self, driver):

        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Click Add button
        add_button_locator = driver.find_element(By.ID, "add_btn")
        add_button_locator.click()

        # wait for the second row to load
        wait = WebDriverWait(driver, 10)
        row_2_input_locator = wait.until(ec.presence_of_element_located((By.XPATH, "//div[@id='row2']/input")))

        # Type text into the second field
        row_2_input_locator.send_keys("Sushi")

        # push save
        driver.find_element(By.NAME, "Save").click()

        # Verify text saved
        confirmation_element = wait.until(ec.presence_of_element_located((By.ID, "confirmation")))
        confirmation_message = confirmation_element.text
        assert confirmation_message == "Row 2 was saved"

    def test_invalid_element_state_exception(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Clear input field
        row_1_input_element = driver.find_element(By.XPATH, "//div[@id='row1']/input")
        row_1_input_element.clear()

        # Type text into the input field
        row_1_input_element.send_keys("Sushi")

        # Verify text changed
        text = row_1_input_element.get_attribute("value")
        assert text == "Sushi", "Expected Sushi" + text

    def test_state_element_reference_exception(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Find the instructions text element
        instruction_element = driver.find_element(By.ID, "instructions")

        # Push add button
        add_button_locator = driver.find_element(By.ID, "add_btn")
        add_button_locator.click()

        # Verify instruction text element is no longer displayed
        assert not instruction_element.is_displayed()

    def test_timeout_exception(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Click Add button
        add_button_locator = driver.find_element(By.ID, "add_btn")
        add_button_locator.click()

        # Wait for 3 seconds for the second input field to be displayed
        wait = WebDriverWait(driver, 3)
        row_2_input_element = wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@id='row2']/input")))

        # Verify second input field is displayed
        assert row_2_input_element.is_displayed()
