# 📱 Android Form Automation with Appium

This project automates the submission of a form in an Android application using **Appium**, **Python**, and **UiAutomator2**. It dynamically fills the form 50 times and generates an interactive **HTML test report**.

---

## ✨ Features

* ✅ Automates Android form filling for 50 submissions
* 🔍 Uses XPath and resource-id selectors
* 🔁 Loops over dynamic values for each form field
* ⚠️ Handles UI exceptions gracefully
* 📊 Generates an HTML report with test results
* 🧭 Includes visual **application flow diagram**

---

## 🧰 Tech Stack

* **Python 3.9**
* **Appium**
* **UiAutomator2 driver**
* **Selenium (for select options)**
* **HTMLTestRunner** (for HTML reporting)

---

## 📁 Folder Structure

```
android-form-automation/
│
├── test_form_automation.py       # Main automation script
├── TestResults.html              # Generated HTML test report
├── DemoVideo.mp4                 # Walkthrough video (under 3 mins)
├── README.md                     # Project documentation
```

---

## ⚙️ Setup Instructions

1. **Start Appium Server**

   ```bash
   appium
   ```

2. **Install Dependencies**

   ```bash
   pip install Appium-Python-Client selenium html-testRunner
   ```

3. **Connect Android Device**

   * Enable USB Debugging from Developer Options
   * Verify connection:

     ```bash
     adb devices
     ```

4. **Run Automation Script**

   ```bash
   python3 test_form_automation.py
   ```

---

## 📝 Sample Submitted Values

Each record submission consists of:

| Field    | Example Values              |
| -------- | --------------------------- |
| Dome     | Dome 1, Dome 2, ..., Dome N |
| Line     | Line A, Line B, ..., Line Z |
| Set      | Set 1 – Set 9               |
| Chamber  | Chamber 1 – Chamber 50      |
| Position | Position 1 – Position 50    |

---

## 🔄 Application Flow

> The automation process is illustrated below:

```mermaid
flowchart TD
    A[Start] --> B[Launch Android App]
    B --> C[Locate Form Fields]
    C --> D[Enter Values (Loop x50)]
    D --> E[Click Submit]
    E --> F[Wait for Success]
    F --> G{More Entries?}
    G -- Yes --> C
    G -- No --> H[Generate HTML Report]
    H --> I[End]
```

---

## 📈 Report

After successful execution, an HTML report is generated at:

```
./TestResults.html
```

It includes:

* Test name and duration
* Pass/fail status
* Timestamp
* Exception trace (if any)

---


