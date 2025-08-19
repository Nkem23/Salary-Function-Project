# Step 1: Import necessary libraries
import pandas as pd
import csv
import zipfile

# Step 2: Load the SF Salaries dataset
try:
    data = pd.read_csv("Total.csv")
    print(data.head())
except FileNotFoundError:
    print("Error: 'Total.csv' not found in this directory.")

# Step 3: Define function to fetch employee details by name
def get_employee_details(name, df):
    emp = df[df['EmployeeName'] == name]
    return emp.to_dict(orient='records')[0] if not emp.empty else None


# Step 4: Convert dataframe into a dictionary keyed by employee_name
salary_dict = data.set_index('EmployeeName').T.to_dict()

# Step 5: Error handling and exporting specific employee_details
try:
    search_name = "RICHARD CORRIEA"  
    details = get_employee_details(search_name, data)
    if details:
        csv_filename = "employee_details.csv"
        with open(csv_filename, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=details.keys())
            writer.writeheader()
            writer.writerow(details)

        zip_name = "Employee_Profile.zip"
        with zipfile.ZipFile(zip_name, "w") as z:
            z.write(csv_filename)

        print(f"\nExported details for {search_name} into {zip_name}.")
    else:
        print(f"\nEmployee '{search_name}' not found in dataset.")
except Exception as e:
    print("An unexpected error occurred:", e)