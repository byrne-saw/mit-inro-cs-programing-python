"""
Problem Set 1, Problem 1a
4/22/2021
Andrew Byrnes
"""

PORTION_DOWN_PAYMENT = 0.25
R = 0.04
ANNUAL_SALARY = float(input("Enter your annual salary: "))
PORTION_SAVED = float(input("Enter the percent of your salary to save, as a decimal: "))
DEAM_HOME_COST = float(input("Enter the cost of your dream home: "))
DOWN_PAYMENT = DEAM_HOME_COST * PORTION_DOWN_PAYMENT
MONTHLY_SALARY = ANNUAL_SALARY / 12

def months_to_save():
    """
    Expects 3 global variables to be defined:
        DOWN_PAYMENT, MONTHLY_SALARY, PORTION_SAVED
    Returns the number of months it will take to save for the down payment as int
    """
    current_savings = 0
    num_months = 0

    while current_savings < DOWN_PAYMENT:
        current_savings = (
            current_savings 
            + (current_savings * R / 12) 
            + (MONTHLY_SALARY * PORTION_SAVED)
            )
        num_months += 1

    print(f'Number of months: {num_months}')

months_to_save()