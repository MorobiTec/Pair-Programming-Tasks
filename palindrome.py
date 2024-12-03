num = int(input('Enter number: '))
temp = num
reversed_num = 0
while num > 0: 
    digit = num % 10
    reversed_num =  reversed_num * 10 + digit
    num = num // 10
if temp == reversed_num : 
    print('f{temp} is a palindrome')
else : 
    print('f{temp} is not palindrome')