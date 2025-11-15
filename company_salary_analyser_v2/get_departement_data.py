def get_departement_data() :
    company = {}
    
    while True :
        departement = input(" enter the depatement ,'done' to finish oe 'exit' to quit : ").strip() 

        if departement.lower() == 'exit' :
            print("the program is closed ! ")
            break
        if departement.lower() == 'done' :
            break
        if departement == "" :
            print("enter a valid departement name !")
            continue
        if departement not in company:
            company[departement] = {}  

        while True :
            employee = input(f" the name of the employee from {departement},and 'done' to finish : ").strip()

            if employee.lower() == 'done' :
                break
            if employee == "" :
                print("enter a valid departement name !")
                continue

            try :
                salary = int(input(f"the salary of {employee} from {departement} ,and 'done' to finish : "))
                if salary < 0 :
                    print("the salary can't be negative !")
                    continue
            except ValueError :
                print("a valid number.")

            company[departement][employee] = salary

    return company   