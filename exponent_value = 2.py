exponent_value = 2
user_value = int(input("enter value: "))
if user_value >= 2 and user_value <= 6 : 
    square_value = user_value * user_value
    print("a","\t","n","\t","a**n")
    print(user_value,"\t", exponent_value,"\t", square_value)
else :
    print("Wrong value. Try again.")