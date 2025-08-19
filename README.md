## Overview
This project demonstrates working with employee salary data using Python and R.

In Python:

Load employee salary dataset (Total.csv).
Fetch details for a selected employee.
Export details into a .csv file.
Zip the file into Employee_Profile.zip.

In R:
Unzip the created folder.
Display the extracted file.

This repository contains both the Python and R code for the workflow.R.

Files in Repository

salary  function assignment.py → Python script to process dataset and export employee details.
unzipping and displaying in R.r → R script to unzip and display data
Total.csv → The salary dataset used (provided).
Employee_Profile.zip → Zipped file containing employee details (created by Python script).
unzipped_data/ → Folder created when unzipping the zip file in R .
README.md → Instructions on how to run both Python and R code.

Requirements
Python
Juypter Notebook

Libraries:
pandas
csv (built-in)
zipfile (built-in)

R

Instructions
Step 1: Run the Python Script
Make sure Total.csv is in the same directory as assignment.py.
Run the script:

The script will:
Load Total.csv.
Fetch details for a specified employee (you can change the name inside the script).
Save the details as employee_details.csv.
Zip it into Employee_Profile.zip.

Step 2: Run the R Code
Ensure Employee_Profile.zip is in your working directory.
Run this R code:

Notes
Change the employee name in salary function assignment.py (search_name) to look up a different employee.
Make sure file names (Total.csv, Employee_Profile.zip) are consistent.
