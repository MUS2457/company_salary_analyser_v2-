from datetime import datetime
from get_departement_data import get_departement_data
from average_salary_per_department import average_salary_per_department
from high_paid_employee import high_paid_employee
from lowest_paid_employee import lowest_paid_employee
from company_stats import company_stats
import json

company_data = get_departement_data()
average_departments_data = average_salary_per_department(company_data)
high_paid_employee_data = high_paid_employee(company_data)
lowest_paid_employee_data = lowest_paid_employee(company_data)
company_stats_data = company_stats(company_data)

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

report = {
    "timestamp": timestamp,
    "top_paid_employee": high_paid_employee_data,
    "lowest_paid_employee": lowest_paid_employee_data,
    "average_departments": average_departments_data,
    "company_stats": company_stats_data,
    "company_structure": company_data
}

with open("company_salary_analyser_v2.json", "w") as j:
    json.dump(report, j, indent=4)

with open("company_salary_analyser_v2.txt", "w") as f:
    f.write(f"Report generated on: {timestamp}\n\n")

    f.write("=== Top Paid Employee ===\n")
    f.write(f"Name: {high_paid_employee_data['employee']}\n")
    f.write(f"Salary: {high_paid_employee_data['salary']}\n")
    f.write(f"Department: {high_paid_employee_data['department']}\n\n")

    f.write("=== Lowest Paid Employee ===\n")
    f.write(f"Name: {lowest_paid_employee_data['employee']}\n")
    f.write(f"Salary: {lowest_paid_employee_data['salary']}\n")
    f.write(f"Department: {lowest_paid_employee_data['department']}\n\n")

    f.write("=== Average Salary per Department ===\n")
    for dep, avg in average_departments_data.items():
        f.write(f"{dep}: {avg}\n")

    f.write("\n=== Company Structure ===\n")
    for dep, employees in company_data.items():
        f.write(f"\n{dep}:\n")
        for emp, sal in employees.items():
            f.write(f"  - {emp}: {sal}\n")

print(json.dumps(report, indent=4))
