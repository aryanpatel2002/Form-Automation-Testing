import unittest
import time
import os
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.options import ArgOptions
from HtmlTestRunner import HTMLTestRunner

class AppiumOptions(ArgOptions):
    KEY = "appium:"

class TestEekiFormSubmission(unittest.TestCase):

    def setUp(self):
        caps = {
            "platformName": "Android",
            "deviceName": "RZCX113FA9P",
            "automationName": "UiAutomator2",
            "appPackage": "com.eekifoods.dev",
            "appActivity": "com.eekifoods.MainActivity",
            "noReset": True
        }

        options = AppiumOptions()
        for k, v in caps.items():
            options.set_capability(k, v)

        self.driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
        self.driver.implicitly_wait(10)

    def test_submit_50_records(self):
        for i in range(1, 51):
            try:
                print(f"[+] Submitting entry #{i}")

                dome = f"Dome {i}"
                line_letter = str(i)
                set_value = str(i % 10 if i % 10 != 0 else 10)
                chamber_value = str(i)
                position_value = str(i)

                # Fill form
                self.driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="dome-0-0"]').clear()
                self.driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="dome-0-0"]').send_keys(dome)

                self.driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="line-0-1"]').clear()
                self.driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="line-0-1"]').send_keys(line_letter)

                self.driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="set-0-2"]').clear()
                self.driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="set-0-2"]').send_keys(set_value)

                self.driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="chamber-0-3"]').clear()
                self.driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="chamber-0-3"]').send_keys(chamber_value)

                self.driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="position-0-4"]').clear()
                self.driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="position-0-4" ]').send_keys(position_value)

                # Submit
                self.driver.find_element(
                    AppiumBy.XPATH, 
                    '//android.widget.TextView[@resource-id="button-text" and @text="Submit"]'
                ).click()

                time.sleep(2)  # Wait for navigation

                # Click Add button for next record
                self.driver.find_element(
                    AppiumBy.XPATH, 
                    '//android.widget.TextView[@text="󰐕"] '
                ).click()

                time.sleep(1.5)  # Wait for form to load

            except Exception as e:
                self.fail(f"[!] Error at entry #{i}: {str(e)}")

        print("[✓] All 50 submissions done.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    report_dir = "./reports"
    os.makedirs(report_dir, exist_ok=True)
    report_file = os.path.join(report_dir, "EekiFormTestReport.html")

    with open(report_file, "w") as output:
        runner = HTMLTestRunner(
            stream=output,
            report_title="Eeki Foods Form Automation Report",
            descriptions="Automated test for submitting 50 form records"
        )
        unittest.main(testRunner=runner, exit=False)
