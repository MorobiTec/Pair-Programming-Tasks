#Q1
bts = ['Kaara', 'Potloane', 'Tlokotsi', 'Morobi', 'Rele']

for i in bts : 
    print(i, '', end ='')
print()
#Q2

cum_sum = sum(range(1,101))
print('Sum of integers from 1 to 100 :', cum_sum)

#Q3

even_sum = sum(range(0, 101, 2))
print('Sum of even from 1 to 100 :', even_sum)

#Q4

odd_sum = sum(range(1, 100, 2))
print('Sum of odd from 1 to 100 :', odd_sum) 


x = 2
y = 5 

if x == 3 or x < 5 and y > 10:
    print("you won")
elif not (x == 3 or x < 5 and y > 10):
    print("you tied")
else:
    print("you lost")

