def average_salary_per_department(company_dict):

    average_salary = {}

    for item,info in company_dict.items() :
        salaries    = list(info.values())
        tl_salaries = sum(salaries)
        average_dep = round(tl_salaries / len(salaries),1)

        average_salary[item] = average_dep

    return average_salary

   
