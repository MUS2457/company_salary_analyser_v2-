def high_paid_employee(company_dict) :
    amount = 0
    top_paid_employee = ""
    top_employee_departement = ""

    for depatement,employees in company_dict.items() :
        for employee,salaries in employees.items() :

            if salaries > amount :
                amount = salaries
                top_paid_employee = employee
                top_employee_departement = depatement

    return {
        "employee": top_paid_employee,
        "salary": amount,
        "department": top_employee_departement
    }



