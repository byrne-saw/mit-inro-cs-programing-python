"""Finger exercise: Write a program that asks the user to enter an integer and prints two integers, root and pwr, such that 0 < pwr < 6 and root**pwr is equal to the integer entered by the user. If no such pair of integers exists, it should print a mes- sage to that effect.
I think it should read: such that 0 < pwr < 6 and root**pwr is equal to the integer entered by the user. Any integer to the power 1 will ultimately match.
"""

def find_root_power():
    x = int(input('Enter an integer: '))
    root = 0
    pwr = 2

    while root < abs(x):
        while pwr < 6:
            if root**pwr == abs(x):
                if x < 0:
                    root = -root
                return print('root =', root, 'and pwr =', pwr)
            else:
                pwr +=1
        root += 1
        pwr = 2
    
    print('No such pair of root**pwr (where pwr is between 2 and 5) integers for', x, 'exists.')

find_root_power()