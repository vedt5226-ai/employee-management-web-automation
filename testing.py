from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class EmployeeAutomation:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 15)
        self.url = "https://opensource-demo.orangehrmlive.com/"

    def open_website(self):
        self.driver.get(self.url)
        print("Website opened")

    def login(self):
        username = self.wait.until(
            EC.visibility_of_element_located((By.NAME, "username"))
        )
        username.send_keys("Admin")

        self.driver.find_element(
            By.NAME, "password"
        ).send_keys("admin123")

        self.driver.find_element(
            By.CSS_SELECTOR, "button[type='submit']"
        ).click()

        self.wait.until(
            EC.url_contains("/dashboard")
        )

        print("Login successful")

    def open_employee_page(self):
        pim = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//span[text()='PIM']")
            )
        )
        pim.click()

        self.wait.until(
            EC.url_contains("/pim/")
        )

        print("Employee Management page opened")

    def search_employee(self):
        employee_id = self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//label[text()='Employee Id']/following::input[1]")
            )
        )

        employee_id.send_keys("001")

        search = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[normalize-space()='Search']")
            )
        )

        search.click()

        print("Employee search completed")

    def logout(self):
        self.wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, ".oxd-userdropdown-tab")
            )
        ).click()

        self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//a[normalize-space()='Logout']")
            )
        ).click()

        print("Logout successful")

    def close_browser(self):
        self.driver.quit()
        print("Browser closed")


# Main Program
automation = EmployeeAutomation()

try:
    automation.open_website()
    automation.login()
    automation.open_employee_page()
    automation.search_employee()
    automation.logout()

except Exception as e:
    print("Test failed:", e)

finally:
    automation.close_browser()