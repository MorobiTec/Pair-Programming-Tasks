import random

n = random.randint(1,3)
if n == 1:
    computer_choice = 'left'
elif n == 2: 
    computer_choice = 'middle'
else:
    computer_choice = 'right'
    
user_choice = int(input("Which part are scoring? "))
if computer_choice == user_choice:
    print('Failed to score')
else: 
    print('Succeeded to score')
print('Computer defence:', computer_choice)
    
