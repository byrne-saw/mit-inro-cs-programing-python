import locale

locale.setlocale(locale.LC_ALL, '')


def months_to_save():
    total_cost = float(input("Enter the total cost of your dream home: "))
    annual_salary = float(input("Enter your annual salary: "))
    portion_saved = float(input("Enter the portion of your monthly income that you will save, this should be in decimal form (i.e. 0.1 for 10%): "))
    current_savings = float(input("Enter your current savings towards a house: "))
    
    portion_down_payment = 0.25
    r = 0.04
    
    down_payment = total_cost * portion_down_payment
    monthly_salary = annual_salary / 12
    num_months = 0

    while current_savings < down_payment:
        current_savings = (
            current_savings 
            + (current_savings * r / 12) 
            + (monthly_salary * portion_saved)
            )
        num_months += 1

    total_cost_formatted = locale.currency(total_cost)
    down_payment_formatted = locale.currency(down_payment)
    current_savings_formated = locale.currency(current_savings)

    print(f'It will take {num_months} months to save {down_payment_formatted} as a down payment for the house that costs {total_cost_formatted}. At the end of the last month you will have {current_savings_formated} in savings.')


months_to_save()