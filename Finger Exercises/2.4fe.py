"""
Finger exercise: Replace the comment in the following code with a while loop.
numXs = int(input('How many times should I print the letter X? ')) toPrint = ''
#concatenate X to toPrint numXs times
print(toPrint)
"""
# numXs = int(input('How many times should I print the letter X? ')) 
# toPrint = ''
# #concatenate X to toPrint numXs times
# while numXs > 0:
#     toPrint = toPrint + 'X'
#     numXs -= 1
# print(toPrint)


"""
Finger exercise: Write a program that asks the user to input 10 integers, and then prints the largest odd number that was entered. If no odd number was entered, it should print a message to that effect.
"""

int_list = []
for i in range(10):
    int_list.append(int(input('Enter integer ' + str(i + 1) + ': ')))

int_list.sort(reverse=True)

for i in int_list:
    if i % 2 != 0:
        print(i)
        break

print('There was no odd number entered')


