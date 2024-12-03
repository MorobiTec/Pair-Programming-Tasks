seat_list, element, even = [], 0, 0
n = int(input("Enter n: "))

for i in range(n):
    temp = []
    for j in range(n):
        element += 1
        temp.append(element)
    if even % 2 == 0:
        for t in temp:
            seat_list.append(t)
    else:
        for t in reversed(temp):
            seat_list.append(t)
    even += 1

counter = 0
for i in seat_list:
    if counter % n == 0:
        print()
    print("{:2d}".format(i), end=" ")
    counter += 1
