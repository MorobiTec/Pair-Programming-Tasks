"""functions"""

"""def star():
    return '*^^^^^^^^^*'
x = star()
print(x)

print('------------------')

def star2():
    print('*^^^^^^^^^*')
star2()

print()
print('------------------')
print()

import string

def cipher(a):
    idx = src_str.index(a)
    return dst_str[idx]

src_str = string.ascii_uppercase
dst_str = src_str[3:] + src_str[:3]

src = input("Enter a sentence: ")
encrypted_text = ''  # Initialize an empty string to hold the encrypted text

for ch in src:
    if ch in src_str:
        encrypted_text += cipher(ch)  # Append the returned value to the encrypted text
    else:
        encrypted_text += ch  # Append the original character if it is not in src_str

print('Encrypted text :', encrypted_text)  # Print the final encrypted text


print()
print('------------------')
print()"""
"""
import string

def cipher(a):
    idx = src_str.index(a)
    print(dst_str[idx], end='')  # Print the encrypted character directly

src_str = string.ascii_uppercase
dst_str = src_str[3:] + src_str[:3]

print(dst_str)

src = input("Enter a sentence: ")

print('Encrypted text :', end='')

for ch in src:
    if ch in src_str:
        cipher(ch)  # Directly call the cipher function which prints the character
    else:
        print(ch, end='')  # Print the original character if it is not in src_str

print()  # Print a newline character at the end

def accumulate_sum(numbers):
    total_sum = 0  # Initialize an accumulation variable

    for num in numbers:
        total_sum += num  # Accumulate the sum of numbers
    print(total_sum)
    # No explicit return statement here

# Example usage:
nums = [1, 2, 3, 4, 5]
accumulate_sum(nums)

"""
def product_set(set1, set2):
    res = set()
    for i in set1:
        for j in set2:
            res = res | {(i, j)}    # Product set using double for loop
    return res

def exp(input_set, exponent):   # A function that performs powers on input_set
    res = input_set     # res initialization
    for _ in range(exponent - 1):   # Repeated for (exponent-1) to become a power
        res = product_set(res, input_set)
    return res

A = {1, 3}
A3 = exp(A, 3)  # Perform 3 powers on set A
print(A3)
def print_sum(a, b):
    result = a + b 
    print('a: ',a, 'b: ', b, 'sum: ')
    return result

res = print_sum(10, 20)
print(res)

print('*****************************')

def foo(*args):
    print('length of args: ', len(args))
    print('Arguments:', args)

foo(10,20,30)

print('*****************************')

def sum_nums(*numbers):
    sum = 0
    for num in numbers:
        sum += num
    return sum

print(sum_nums(10,20,30))
print(sum_nums(10,20,30,40,50))


print('*****************************')

def mile2km(mi):
    for _ in range(1, mi + 1):
        mile = 1.61
        print(_, 'mile =', mile * _, 'kilometers')

mile2km(5)

def mile2km(mi):
    return mi*1.61

for n in range(1,6):
    print(n, ':', mile2km(n))
    
def formula(cel):
    return cel * 9/5 * 32


for i in range(10, 60, 10):
    print(i, ':', formula(i))

"""Pair Programming"""
def mean3(a, b, c):
    return (a + b + c) / 3

def max3(a, b, c):
    return max(a, b, c)

def min3(a, b, c):
    return min(a, b, c)

a, b, c = input("Enter three numbers: ").split()
a = int(a)
b = int(b)
c = int(c)

print('The average value of {}, {}, {} is'.format(a, b, c), mean3(a, b, c))
print('The maximum value of {}, {}, {} is'.format(a, b, c), max3(a, b, c))
print('The minimum value of {}, {}, {} is'.format(a, b, c), min3(a, b, c))