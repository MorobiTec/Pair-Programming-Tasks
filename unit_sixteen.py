num = 48
divisors = set()

for i in range(2, num):
    if num % i == 0:
        divisors.add(i)

num1 = 60 
divisors1 = set()

for i in range(2, num1):
    if num1 % i == 0:
        divisors1.add(i)     

print('48: ',divisors)
print('60: ',divisors1)

print(max(divisors.intersection(divisors1)))

print('********zip***********')

a_list = set([7,7,5,3,1])
b_list = set(['a', 'b', 'c','d', 'd'])

for val in zip(a_list, b_list):
    print(val) 

"""mylist = [(1, 2), (4, 5), (4, 2), (3, 1), (9, 4)]

while True:
    a, b = input("Enter two integers (or 'q' to quit): ").split()
    
    if a == 'q' or b == 'q':
        print("Exiting program.")
        break
    
    a = int(a)
    b = int(b)

    setlist = []
    for item in mylist:
        setlist.append(set(item))

    found_ab = -1
    found_ba = -1

    index = 1

    for item in setlist:
        if item == {a, b}:
            if (a, b) in mylist:
                found_ab = index
            elif (b, a) in mylist:
                found_ba = index
        index += 1

    if found_ab != -1:
        print(f'There is ({a}, {b}) at position {found_ab}.')
    elif found_ba != -1:
        print(f'There is no ({a}, {b}) but ({b}, {a}) is at position {found_ba}.')
    else:
        print(f'There is no ({a}, {b}) nor ({b}, {a}), there is no such element.')
"""