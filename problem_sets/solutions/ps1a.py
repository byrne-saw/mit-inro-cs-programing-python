# import locale

# locale.setlocale(locale.LC_ALL, '')

PORTION_DOWN_PAYMENT = 0.25
R = 0.04

def months_to_save():
    annual_salary = float(input("Enter your annual salary: "))
    portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
    total_cost = float(input("Enter the cost of your dream home: "))
    
    current_savings = 0
    down_payment = total_cost * PORTION_DOWN_PAYMENT
    monthly_salary = annual_salary / 12
    num_months = 0

    while current_savings < down_payment:
        current_savings = (
            current_savings 
            + (current_savings * R / 12) 
            + (monthly_salary * portion_saved)
            )
        num_months += 1

    # total_cost_formatted = locale.currency(total_cost)
    # down_payment_formatted = locale.currency(down_payment)
    # current_savings_formated = locale.currency(current_savings)

    print(f'Number of months: {num_months}')

months_to_save()