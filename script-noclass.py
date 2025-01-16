import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


class TestPracticeForm(unittest.TestCase):
    def setUp(self):
        # Set up the WebDriver and the URL
        self.driver = webdriver.Chrome()
        self.url = "https://www.techlistic.com/p/selenium-practice-form.html"

    def open_form(self):
        # Open the form URL
        self.driver.get(self.url)

    def accept_cookies(self):
        # Handle cookie banners
        time.sleep(5)
        self.driver.find_element(By.ID, "ez-accept-necessary").click()
        self.driver.find_element(By.ID, "cookieChoiceDismiss").click()

    def fill_name(self, first_name, last_name):
        # Fill out the first and last name fields
        self.driver.find_element(By.NAME, "firstname").send_keys(first_name)
        self.driver.find_element(By.NAME, "lastname").send_keys(last_name)

    def select_gender(self, gender_id):
        # Select gender
        self.driver.find_element(By.ID, gender_id).click()

    def select_experience(self, experience_id):
        # Select experience
        self.driver.find_element(By.ID, experience_id).click()

    def fill_date(self, date):
        # Fill out the date field
        self.driver.find_element(By.ID, "datepicker").send_keys(date)

    def select_profession(self, profession_id):
        # Select profession
        self.driver.find_element(By.ID, profession_id).click()

    def select_automation_tool(self, tool_id):
        # Select automation tool
        self.driver.find_element(By.ID, tool_id).click()

    def select_continent(self, continent):
        # Select continent from dropdown
        dropdown = Select(self.driver.find_element(By.ID, "continents"))
        dropdown.select_by_visible_text(continent)

    def select_selenium_command(self, command):
        # Select Selenium command from dropdown
        dropdown = Select(self.driver.find_element(By.ID, "selenium_commands"))
        dropdown.select_by_visible_text(command)

    def upload_file(self, file_path):
        # Upload a file
        self.driver.find_element(By.ID, "photo").send_keys(file_path)

    def submit_form(self):
        # Submit the form
        self.driver.find_element(By.ID, "submit").click()

    def test_form_submission(self):
        self.open_form()
        self.accept_cookies()

        # Fill out the form
        self.fill_name("Tom", "Wood")
        self.select_gender("sex-0")
        self.select_experience("exp-4")
        self.fill_date("16-10-2020")
        self.select_profession("profession-1")
        self.select_automation_tool("tool-2")
        self.select_continent("Europe")
        self.select_selenium_command("Browser Commands")
        self.upload_file("C:/Users/Dachi/Downloads/selenium/assets/images.png")

        # Submit the form
        self.submit_form()

        # Wait to observe the result
        time.sleep(5)

        # Assert form submission (you can enhance this with a specific success message or behavior)
        print("CONGRATULATIONS! Form submitted successfully!")

    def tearDown(self):
        # Close the browser
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

