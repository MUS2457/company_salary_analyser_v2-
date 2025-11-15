def company_stats(company_dict):
    tl_salaries = 0
    tl_employees = 0

    for departements, employees in company_dict.items():
        tl_salaries  += sum(employees.values())
        tl_employees += len(employees)

    average_salary = round(tl_salaries / tl_employees, 1) if tl_employees else 0

    return {
        "total_salaries_across_company": tl_salaries,
        "total_employees": tl_employees,
        "average_salary": average_salary
    }
