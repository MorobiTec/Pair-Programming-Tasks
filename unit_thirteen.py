print('Paper Coding Q1')
value = 1
for i in range(1, 5):
    for j in range(4):
        print(value, end=' ')
        value += 1
    print()


print()
print('Question 1')
print()

list1 = []
n = int(input("Enter n: "))
for i in range(n):
    line = []
    for j in range(n):
        if (i + j) % 2 == 0:
            line.append(1)
        else:
            line.append(0)
    list1.append(line)
for i in list1:
    for j in i:
        print(j, end = ' ')
    print()

