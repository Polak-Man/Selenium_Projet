import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestPracticeForm(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = "https://www.techlistic.com/p/selenium-practice-form.html"

    def open(self):
        self.driver.get(self.url)

    def fill_name(self, name):
        name_input = self.driver.find_element(By.NAME, "firstname")
        name_input.clear()
        name_input.send_keys(name)

    def fill_last_name(self, last_name):
        last_name_input = self.driver.find_element(By.NAME, "lastname")
        last_name_input.clear()
        last_name_input.send_keys(last_name)

    def submit(self):
        submit_button = self.driver.find_element(By.NAME, "photo")
        submit_button.click()

    def get_success_message(self):
        return self.driver.find_element(By.CLASS_NAME, "success").text

    def test_fill_form(self):
        self.open()
        self.fill_name("John")
        self.fill_last_name("Doe")
        self.submit()

        success_message = self.get_success_message()
        self.assertIn("Success", success_message)  # Vérifiez que le message de succès est affiché

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()