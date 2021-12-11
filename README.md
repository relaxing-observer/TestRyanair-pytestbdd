# Testing Ryanair Project
**PythonTestAutomationFramework**

**Description**

Test Automation Framework for web automation of "www.ryanair.com" using Selenium and Python using BDD testing approach with the below features:

* Framework is based on Page Object Model. 
* BDD approach (Pytest-BDD plugin) with Scenario Outline
* Reporting using Allure report.
* Logging to external file.

    
The project is being developed during the iTechArt internship.

# How to install it
Make sure you have python3.10 installed on your machine by typing in cmd ``python3 --version`` if not - go to https://realpython.com/installing-python/#step-1-download-the-python-3-installer.

1) Clone the repository to any local path.

``$ git clone https://github.com/EgorSolenok/TestRyanair.git``

2) Make sure you have  allure command line  by typing in cmd ``allure --version``. If not - you have to install allure command line and add the allure folder installation into system environment variable: https://docs.qameta.io/allure/#_installing_a_commandline

3) Make sure you have pipenv  by typing in cmd ``pipenv --version``. If not - you have to install pipenv for creation virtual environment and installation packages: https://pipenv.pypa.io/en/latest/  

``$ pip install --user pipenv``

4) Install dependencies:

``pipenv install``


# How to run it

**For all tests runs you should to type commands in project directory.**
**You should type your actual credentials to commandline instead of < USER@EMAIL.COM > and < PASSWORD > in every case (without brackets).**


To run scenario steps in feature "Verify user is finding flights in specified dates" and create report:

`` pipenv run python -m pytest -k -v "flights_search" --tb=line --user=<USER@EMAIL.COM> --password=<PASSWORD> 
 --alluredir=report_data``

To run scenario steps in feature "Verify user is finding hotels in specified dates" and create report:

`` pipenv run python -m pytest -k "hotels_search" --user=<USER@EMAIL.COM> --password=<PASSWORD> -v --tb=line
 --alluredir=report_data``

To change the data using in steps you should open files .\tests\features\hotels_search.feature and .\tests\features\hotels_search.feature.
You can change values in the table accordingly to the web-service  (should be correct names) and put your own locations or dates in it, or add lines with new values.

To create **Allure report** and open it type in cmd being located in the folder path:

``allure serve report_data``

**Logging**

To read logs you should open file ``logging_data.log``

