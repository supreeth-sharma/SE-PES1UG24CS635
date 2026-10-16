# Lab 5 - Static Code Analysis

## About the Lab

In this lab, I worked on a Python program for managing blood donations and used static code analysis tools to identify problems in the code. I fixed the issues found and ran the tools again to check whether the changes improved the code.

## Tools Used

- **Pylint** – Used to check code quality, naming conventions, and documentation.
- **Bandit** – Used to find potential security issues in the program.
- **Flake8** – Used to check code formatting and style.

## Files in This Folder

- `blood_donation.py` – The Python program used for the lab.
- `issues.md` – A list of the issues found and how they were fixed.
- `reports/before/` – Contains the reports generated before making the changes.
- `reports/after/` – Contains the reports generated after making the changes.

## How to Run

First, create and activate a virtual environment and install the required tools:

```cmd
python -m venv venv
venv\Scripts\activate
python -m pip install pylint bandit flake8
```

Run the program using:

```cmd
python blood_donation.py
```

To run the analysis tools individually:

```cmd
python -m pylint blood_donation.py
python -m bandit -r blood_donation.py
python -m flake8 blood_donation.py
```

## Results

After fixing the issues, I ran all three tools again and tested the program. Pylint gave a score of **10/10**, Bandit reported no issues, and Flake8 reported no style violations. The program also ran successfully.

The reports before and after the changes are included in the `reports` folder for comparison.