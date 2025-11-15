Company Salary Analyser – Version 2

A modular Python program that collects employee salary data and generates a full analysis report.
This version is fully separated into functions and modules, and produces a JSON + TXT report for easy reading.

What This Program Does

Collects departments, employees, and salaries through user input

Calculates:

Highest paid employee

Lowest paid employee

Average salary per department

Total salaries in the whole company

Total number of employees

Overall average salary

Saves a detailed report as both:

company_salary_analyser_v2.json

company_salary_analyser_v2.txt

Prints the analysis in the terminal

Code split into multiple files for cleaner structure and easier maintenance
How It Works
1. Data Collection

The program asks for:

Department names

Employee names

Salaries

All of this happens inside get_departement_data.py.

2. Calculations

Each calculation is in its own file:

average_salary_per_department.py

high_paid_employee.py

lowest_paid_employee.py

company_stats.py

3. Reporting

main.py merges everything into a dictionary and saves it as:

JSON → for technical use

TXT → for human reading
