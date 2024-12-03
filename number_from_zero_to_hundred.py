number = int(input('Enter an integer: '))
print('Is the input integer between 0 and 100?',(0 <= number <= 100) and number % 2 == 0)