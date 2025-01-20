# app_automation

This project automates the testing of a mobile application Bree using **Appium**, **Python**, and **pytest**. The tests include scenarios like navigation, login, dashboard validation, and logout.

---

## 📊 Prerequisites

Before running this project, ensure you have the following installed and configured:

- **[Node.js](https://nodejs.org/)** (for Appium server)
- **[Python 3.8 or higher](https://www.python.org/downloads/)**
- **Appium server** (install globally via npm):
  ```bash
  npm install -g appium
  ```
- **Android SDK** (set up using [Android Studio](https://developer.android.com/studio))
- **Android Emulator or Physical Device**
  - Start an emulator or connect a physical Android device.
  - Verify the device using:
    ```bash
    adb devices
    ```

---

## ⚙️ Installation and Setup

Follow these steps to set up the project:

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/appium-automation-project.git
cd appium-automation-project
```

### 2. Set Up a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
```

### 3. Install Python Dependencies
Install the required Python libraries listed in `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 4. Start Appium Server
Start the Appium server:
```bash
appium
```

---

## 🧪 Running Tests

This project uses **pytest** for running test cases.

### Run All Tests
```bash
pytest --html=report.html
```

### Generate HTML Reports
Make sure you have the `pytest-html` plugin installed:
```bash
pip install pytest-html
```
The HTML reports will be generated in the specified file (e.g., `report.html`).

---


## 🌟 Key Features

- Automated testing for Android applications.
- Uses **Appium** for mobile app interaction.
- Tests are structured with **pytest** for better modularity and scalability.
- Supports detailed HTML test reports.

---

## 🔗 Environment Configuration

Ensure the following capabilities are correctly configured in `conftest.py` or your test scripts:

| Capability           | Value                         | Description                                |
|----------------------|-------------------------------|--------------------------------------------|
| `platformName`       | Android                      | Mobile platform                            |
| `platformVersion`    | 10                           | Version of the emulator or device          |
| `deviceName`         | emulator-5554               | Name of the emulator/device                |
| `appPackage`         | com.breemobile               | Package name of the app under test         |
| `appActivity`        | com.breemobile.MainActivity | Main activity to launch the app            |
| `noReset`            | true                         | Prevents clearing app data after tests     |

---

## 🔖 Dependencies

The required Python dependencies are listed in `requirements.txt`:

```plaintext
Appium-Python-Client==4.3.0
args==0.1.0
asgiref==3.8.1
atomicwrites==1.4.1
attrs==24.2.0
beautifulsoup4==4.12.3
cachetools==5.5.0
certifi==2024.8.30
cffi==1.17.1
charset-normalizer==3.4.0
clint==0.5.1
clr-loader==0.2.6
colorama==0.4.6
comtypes==1.4.8
configobj==5.0.9
cssselect==1.2.0
cssutils==2.11.1
datefinder==0.7.3
deepdiff==8.0.1
Django==5.1.3
EasyProcess==1.1
entrypoint2==1.1
et_xmlfile==2.0.0
google-api-core==2.22.0
google-auth==2.35.0
google-cloud-bigquery==3.27.0
google-cloud-bigquery-storage==2.27.0
google-cloud-core==2.4.1
google-crc32c==1.6.0
google-resumable-media==2.7.2
googleapis-common-protos==1.65.0
grpcio==1.67.1
grpcio-status==1.67.1
h11==0.14.0
html-diff==0.4.1
idna==3.10
image==1.5.33
imap-tools==1.7.4
importlib_metadata==8.5.0
imutils==0.5.4
iniconfig==2.0.0
Jinja2==3.1.4
jsonpointer==3.0.0
jsonschema==4.23.0
jsonschema-specifications==2024.10.1
keyboard==0.13.5
lxml==5.3.0
markdown-it-py==3.0.0
MarkupSafe==3.0.2
mdurl==0.1.2
more-itertools==10.5.0
mouse==0.7.1
MouseInfo==0.1.3
mss==9.0.2
numpy==2.1.3
opencv-python==4.10.0.84
openpyxl==3.1.5
orderly-set==5.2.2
outcome==1.3.0.post0
packaging==24.1
pandas==2.2.3
pdf2image==1.17.0
pillow==11.0.0
platformdirs==4.3.6
pluggy==0.13.1
premailer==3.10.0
proto-plus==1.25.0
protobuf==5.28.3
psutil==6.1.0
py==1.11.0
pyasn1==0.6.1
pyasn1_modules==0.4.1
pyautocad==0.2.0
PyAutoGUI==0.9.54
PyAutoIt==0.6.5
pycparser==2.22
PyGetWindow==0.0.9
Pygments==2.18.0
PyMsgBox==1.0.9
pyodbc==5.2.0
PyPDF2==3.0.1
pyperclip==1.9.0
pypiwin32==223
PyRect==0.2.0
pyrsistent==0.20.0
pyscreenshot==3.1
PyScreeze==1.0.1
pyserial==3.5
pyshortcuts==1.9.5
PySocks==1.7.1
pytesseract==0.3.13
pytest==6.1.2
python-dateutil==2.9.0.post0
python-dotenv==1.0.1
pythonnet==3.0.4
pyttsx3==2.71
pytweening==1.2.0
pytz==2024.2
pywin32==308
PyYAML==6.0.2
rauth==0.7.3
referencing==0.35.1
regex==2024.11.6
requests==2.32.3
rfc3339-validator==0.1.4
rfc3986-validator==0.1.1
rich==13.9.4
rpds-py==0.20.1
rsa==4.9
selenium==4.26.1
simplejson==3.19.3
six==1.16.0
sniffio==1.3.1
sortedcontainers==2.4.0
soupsieve==2.6
SpeechRecognition==3.11.0
sqlparse==0.5.1
toml==0.10.2
tomli==2.0.2
tqdm==4.67.1
trio==0.27.0
trio-websocket==0.11.1
typing_extensions==4.12.2
tzdata==2024.2
tzlocal==5.2
uiautomator==1.0.2
urllib3==2.2.3
webcolors==24.11.1
webdriver-manager==4.0.2
websocket-client==1.8.0
winshell==0.6
WMI==1.5.1
wsproto==1.2.0
xlwings==0.33.3
xmltodict==0.14.2
yapf==0.40.2
zipp==3.20.2

```

Install them using:
```bash
pip install -r requirements.txt
```

---

## 🛡️ Troubleshooting

- **Appium Server Issues**:
  - Ensure the server is running at `http://127.0.0.1:4723`.
  - Use the `--allow-insecure` flag if needed:
    ```bash
    appium --allow-insecure=chromedriver_autodownload
    ```

- **Device Not Found**:
  - Ensure the device is connected and visible via `adb devices`.
  - Restart the emulator or physical device if necessary.

- **Driver Initialization Fails**:
  - Verify that the Appium capabilities are correctly configured.
  - Ensure the app is installed on the device.

---

## 📧 Contact

For any questions or feedback, reach out to:

- **Name**: Saqib Haider
- **Email**: saqibhaider567@gmail.com
- **GitHub**: [SaqibHaider](https://github.com/your-username)

---

This README provides all the necessary information to set up and run, the project.😊
