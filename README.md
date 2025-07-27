# Android Form Automation with Appium

This project automates the submission of a form inside an Android app using **Appium**, **Python**, and **UiAutomator2**. It fills out the form 50 times with dynamic values and generates a detailed HTML report of the test execution.

---

## Features

- Automates Android form filling for 50 records
- Uses XPath and resource-id for element interaction
- Handles exceptions gracefully
- Generates an HTML test report
- Includes application flow diagram

---

## Tech Stack

- Python 3.9
- Appium
- Selenium (only used for options class)
- HTMLTestRunner (for reporting)

---

## Folder Structure

```

android-form-automation/
│
├── test\_form\_automation.py     # Main automation script
├── reports/
│   └── TestResults.html        # HTML report generated after run               
├── README.md                   # This file

````

---

## ⚙Setup Instructions

1. **Start Appium Server**
   ```bash
   appium
````

2. **Install required packages**

   ```bash
   pip install Appium-Python-Client selenium html-testRunner
   ```

3. **Connect your Android device**

   * Enable USB debugging
   * Check connection:

     ```bash
     adb devices
     ```

4. **Run the automation**

   ```bash
   python3 test_form_automation.py
   ```

---

## Sample Values Submitted

Each submission includes:

| Field    | Value Example      |
| -------- | ------------------ |
| Dome     | Dome 1, Dome 2 ... |
| Line     | Line A, Line B ... |
| Set      | Set 1–9            |
| Chamber  | Chamber 1–50       |
| Position | Position 1–50      |

---

## Application Flow

> Below is a high-level flowchart of the automation logic:

```mermaid
flowchart TD
    A[Start] --> B[Launch Android App]
    B --> C[Locate Form Fields]
    C --> D[Enter Values (Loop x50)]
    D --> E[Click Submit]
    E --> F[Wait for Success]
    F --> G{More entries?}
    G -- Yes --> C
    G -- No --> H[Generate Report]
    H --> I[End]

---

## Report

After successful execution, a detailed report is generated at:

```
./reports/TestResults.html
```

### Sample Report Screenshot

![Sample Report](assets/report-screenshot.png) <!-- optional, if you want -->

---

## Author

* **Aryan Patel**
* Internship @ Kanini Software Solutions
* Applying for **QA/Automation roles**

---

## Final Notes

* Make sure the resource-IDs used match your Android app's actual layout.
* You can modify the `range(1, 51)` if you want to submit fewer or more records.
* For real-time logs, check your terminal output.
