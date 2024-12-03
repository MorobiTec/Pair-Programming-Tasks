"""capital_dic = {
    "Korea" : "Seoul",
    "China" : "Beijing",
    "USA" : "Washington DC",
}
for cap in capital_dic:
    print('key : {:16s} \nvalue : {:}'.format(cap, capital_dic[cap]))

print(capital_dic['Korea'])
"""

fruits_dic = {
    'apple': 5000,
    'banana': 6000,
    'grape': 6000,
    'melon': 6500
}

"""
search_name = (input("Enter name: "))

for fruit, price in fruits_dic.items():
    if price == search_price:
        print(fruit, ':', price)

print("Displaying Manually")
for fruit in fruits_dic:
    if fruits_dic[fruit] == 6000:
        print(fruit, ':',fruits_dic[fruit])
print()       
print('*****************************')

print("Displaying with Items()")
for fruit, value in fruits_dic.items():
    if value == 6000:
        print(fruit, ':',value)
print(len(fruits_dic))
        
print('*****************************')

print('Inserting Manually')

while True : 
    fruit_name = input("Enter fruit name:(or q to quit) ")
    fruit_price = int(input("Enter fruit price: (1 to quite) "))
    
    if fruit_name == 'q' and fruit_price == 1:
        break
    
    fruits_dic[fruit_name] = fruit_price

    for fruit in fruits_dic:
        print(f'{fruit} : {fruits_dic[fruit]}')
    print('Total fruits: ',len(fruits_dic))
"""

print('*****************************')
print('Deleting Manually')

while True : 
    print(fruits_dic.items())
    name = input('Enter fruit to delete: (q to quit) ')
    if name == 'q':
        break
    del(fruits_dic[name])
    for fruit in fruits_dic:
        if fruit: 
            print(fruit, ':', fruits_dic[fruit])
    