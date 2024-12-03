
a, b = input("Write two integers: ").split()

if int(a) % int(b) == 0:
    print(a, "is a multiple of", b)
else:
    print(a, "is not a multiple of", b)