"""stage = 1
for stage in range(1,10): 
    multiplier = 1
    for multiplier in range(1,10): 
        product = stage * multiplier
        print(f"{stage} x {multiplier} = {product}")
        
num_list = [1,2,3]

for row in num_list :
    for col in num_list : 
        for col2 in num_list :
            print("{} {} {}".format(row, col, col2))"""

def product_set(set1, set2):
    res = set()
    for i in set1:
        for j in set2:
            res = res | {(i, j)}    # Productset using double for loop
    return res

def exp(input_set, exponent):   # A function that performs powers on input_set
    res = input_set     # res initialization
    for _ in range(exponent - 1):   # Repeated for (exponent-1) to become a power
        res = product_set(res, input_set)
    return res

A = {1, 3}
A3 = exp(A, 3)  # Perform 3 powers on set A
print(A3)