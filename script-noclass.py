from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


driver = webdriver.Chrome()

# Open the URL
driver.get("https://www.techlistic.com/p/selenium-practice-form.html")

# Maximize the browser window
driver.maximize_window()

# Enter Firstname
driver.find_element(By.NAME, "firstname").click()
driver.find_element(By.NAME, "firstname").send_keys("Tom")

# Enter Lastname
driver.find_element(By.NAME, "lastname").click()
driver.find_element(By.NAME, "lastname").send_keys("Wood")

# Select Gender
driver.find_element(By.ID, "sex-0").click()

# Select Experience
driver.find_element(By.ID, "exp-4").click()

# Enter Date
driver.find_element(By.ID, "datepicker").click()
driver.find_element(By.ID, "datepicker").send_keys("16-10-2020")

# Select Profession
driver.find_element(By.ID, "profession-1").click()

# Select Automation Tool
driver.find_element(By.ID, "tool-2").click()

# Select Continent
dropdown_continents = Select(driver.find_element(By.ID, "continents"))
dropdown_continents.select_by_visible_text("Europe")

# Select Selenium Command
dropdown_commands = Select(driver.find_element(By.ID, "selenium_commands"))
dropdown_commands.select_by_visible_text("Browser Commands")

# Scroll down to the Submit button (optional)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# Click Submit
driver.find_element(By.ID, "submit").click()

# Wait for a while to observe the result
time.sleep(5)

print("Form submitted successfully!")

# Close the browser
driver.quit()
