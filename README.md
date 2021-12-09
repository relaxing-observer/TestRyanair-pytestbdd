This project requires an up-to-date version of Python 3. It also uses pipenv to manage packages.

To set up this project on your local machine:

    Clone it from this GitHub repository.
    Run pipenv install from the command line in the project's root directory.
    For Web UI tests, install the appropriate browser and WebDriver executable.
        These tests use Firefox and geckodriver.


 pipenv run python -m pytest -v  .\tests\step_defs\test_hotels_search.py --alluredir=report_data

# Testing Ryanair Project
**PythonTestAutomationFramework**

**Description**

Test Automation Framework for web automation of "https://github.com" using Selenium and Python using BDD testing approach with the below features:

* Framework is based on Page Object Model. 
* Reporting using Allure report.
* Logging to external file.
* BDD approach (Pytest-BDD)
    
The project is being developed during the iTechArt internship.

# How to install it

Make sure you have python3 installed on your machine by typing in cmd ``python3 --version`` if not - go to https://realpython.com/installing-python/#step-1-download-the-python-3-installer.

1) Clone the repository to any local path.

``$ git clone https://github.com/EgorSolenok/TestRyanair.git``

2) You have to install allure command line and add the allure folder installation into system environment variable: https://docs.qameta.io/allure/#_installing_a_commandline

[//]: # (3&#41; You have to install package pipenv for creation virtual: https://pipenv.pypa.io/en/latest/  )

[//]: # ()
[//]: # (4&#41; Install dependencies in python3 from requirements.txt:)

[//]: # ()
[//]: # (``pip3 install -r requirements.txt``)

5) Add your own credentials (**USERNAME** and **PASSWORD**) for logging  in ``utils/credentials.py``:

**class Credentials**
* USERNAME = ``'type here'``
* PASSWORD = ``'type here'``

# How to run it

**For all tests runs you should to type commands in folder ``tests``.**

To run the test cases in feature "Guest login actions on the main page" and create report:

``pytest -v -m "guest_actions" --alluredir=report_data/``

To run the test cases in feature "User main actions with repository" and create report:

``pytest -v -m "main_actions" --alluredir=report_data/``


To run the test cases in feature "User additional actions with repository" and create report:

``pytest -v -m "addition_actions" --alluredir=report_data/``

To run required tests from PythonInternship_Task0 use in brackets following marks:
* Correct user is logged in -  ``pytest -v -m "sign_in" --alluredir=report_data/``
* Create repository -  ``pytest -v -m "create_repository" --alluredir=report_data/``
* Rename repository -  ``pytest -v -m "rename_repository" --alluredir=report_data/``
* Add README -  ``pytest -v -m "add_readme" --alluredir=report_data/``
* Delete repository -  ``pytest -v -m "delete_repository" --alluredir=report_data/``

To create **Allure report** and open it type in cmd being located in the folder path:

``allure serve report_data``

**How to logging**

To read logs you should to read or copy file ``logging_data.log`` to your machine after every test run. 
File will be overwritten after starting the next test.
The ability to append logs in file will be added in next version of the framework.
