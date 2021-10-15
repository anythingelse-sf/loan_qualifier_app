<<<<<<< HEAD
# Loan Qualifier Application

Business Needs:
    1) Prompt the user to save qualifying loans as a new CSV file
    2) Modulate the code to allow for adding new features and enhancements

User Story:
    1) I need the ability to save the qualifying loans to a CSV file so I can circulate the results as a spreadsheet

Acceptance Critera:
    1) The tool should prompt the user to save the results as a CSV file
    2) If no qualifying loans exist, then the program should notify the user and exit
    3) Once a list of qualifying loans has been generated, the user should be able to opt out of saving the file
    4) The tool should ask the user for a filepath to save the file to
    5) If the user elects to save the file, the file shoud save as a CSV to the filepath provided

---
## Code Structure
Primary Folder - Holds the primary application file
    a)

Data Folder - Holds the files we pull loan data from
    a)

Qualifier Folder - Contains all funtions that are imported into the main application file
    a)

Utils
    a) Financial Calculator Module
    b) FileIO

README.md
    a) Contains a Table of Contents
    b) List all libraries used in our Python code
    c) Instructions for creating the code
    d) Installation Guide

Version Control
- Text file showing command history


## Libraries
Pathlib -> Path
Pandas as pd
Questionary
Fire

---
## Installation Guide
Ensure that you are running your Python code from the correct directory to access the daily rate sheet. Otherwise you may need to copy and paste the full file path.

---
## Usage
Step 1: Input the relative path to your CSV file containing the daily rate sheet from banks
Step 2: Follow the prompts to filter down your search
Step 3: Export this data or read it straight from the terminal
Step 4: Happy home hunting!

---
## Contributors
Created by Dylan Nelson.
Reach out via Github for more info
---

## Licensing
No appplicable license necessary. 
This is an open source software project intended to aid young developers.
=======
# loan_qualifier_app
An application to filter daily bank loan sheets
>>>>>>> 1e594662c4aa795effa6ee2883af547e73d53e31
