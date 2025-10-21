from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Start ChromeDriver
driver = webdriver.Chrome()

# Open your Kubernetes app
driver.get("http://localhost:30844")  # Replace with correct NodePort
time.sleep(2)

# Fill the form
driver.find_element(By.NAME, "full_name").send_keys("Test User")
driver.find_element(By.NAME, "email").send_keys("test_user@gmail.com")
driver.find_element(By.NAME, "username").send_keys("testuser123")
driver.find_element(By.NAME, "password").send_keys("password123")
driver.find_element(By.NAME, "confirm_password").send_keys("password123")
driver.find_element(By.NAME, "phone").send_keys("9876543210")
driver.find_element(By.NAME, "dob").send_keys("2000-01-01")
driver.find_element(By.NAME, "gender").send_keys("Male")
driver.find_element(By.NAME, "address").send_keys("Hyderabad, India")

# Wait until the submit button is clickable, then click
submit_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
)
submit_button.click()

time.sleep(3)
print("Test Completed Successfully!")
driver.quit()

