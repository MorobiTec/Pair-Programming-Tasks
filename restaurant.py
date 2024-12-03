print('Welcome to the yummy restaurant. Here is the menu.')
print('- Burger (enter b) \n- Chicken (enter c) \n- Pizza (enter p)')

choice = input('Choose a menu (enter b,c,p):')
if choice == 'b':
    print('You chose burger.')
elif choice == 'c':
    print('You chose chicken')
elif choice == 'p':
    print('You chose pizza')
elif choice != 'b' and choice != 'c' and choice != 'p':
    print('Enter the menu again.')
    choice = input('Choose a menu (enter b,c,p):')
    if choice == 'b':
        print('You chose burger')
    elif choice == 'c':
        print('You chose chicken')
    elif choice == 'p':
        print('You chose pizza')
    else:
        print('Enter menu again.')
else:
    print('Enter menu again.')