

def months_to_save():
    total_cost = float(input("Enter the total cost of your dream home: "))
    annual_salary = float(input("Enter your annual salary: "))
    portion_saved = float(input("Enter the portion of your monthly income that you will save, this should be in decimal form (i.e. 0.1 for 10%): "))
    portion_down_payment = 0.25
    current_savings = 0.0
    r = 0.04

    monthly_salary = annual_salary / 12
    # at the end of each month, you receive an additional ​current_savings*r/12

months_to_save()