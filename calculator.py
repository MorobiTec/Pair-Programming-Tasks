print('1) Addition  2) Subtraction 3) Multiplication 4) Division')
choice = int(input('Enter the desired number of operation : '))

if choice <= 4 :
    print('Enter  two numbers for operation. ')
    first_num = int(input(''))
    second_num = int(input(''))
    
    if choice == 1 : 
        print(first_num, '+', second_num, '=', first_num + second_num)
    elif choice == 2 : 
        print(first_num, '-', second_num, '=', first_num - second_num)
    elif choice == 3 : 
        print(first_num, '*', second_num, '=', first_num * second_num)
    elif choice == 4 : 
        print(first_num, '/', second_num, '=', first_num / second_num)

else : 
    print('Entered an incorrect number.')