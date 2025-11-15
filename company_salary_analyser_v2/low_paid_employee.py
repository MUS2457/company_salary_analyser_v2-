def lowest_paid_employee(company_dict) :
    amount = float('inf')
    lowest_paid_employee = ""
    low_employee_departement = ""

    for depatement,employees in company_dict.items() :
        for employee,salaries in employees.items() :

            if salaries < amount :
                amount = salaries
                lowest_paid_employee = employee
                low_employee_departement = depatement

    return {
        "employee": lowest_paid_employee,
        "salary": amount,
        "department": low_employee_departement
    }

