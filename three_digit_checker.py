digit_to_check = 3
digit_position = 100
number = int(input("Enter a 3-digit integer: "))
hundredth_digit = number // digit_position == digit_to_check
print(hundredth_digit)
