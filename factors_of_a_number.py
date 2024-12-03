number = int(input("Enter a positive whole number to find its factors: "))
factors = [1]

for divisor in range(2, number // 2 + 1):
    if number % divisor == 0:
        factors.append(divisor)

factors.append(number)
print(f"The factors of {number} are: {factors}")
