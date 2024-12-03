"""
print('Paper Coding Q1')
person_dic = {
    'Last Name' : 'Doe',
    'First Name' : 'David',
    'Company' : 'Samsung'
}
for str1, num in person_dic.items():
    print(str1, ':', num) 

print('*******************')
print('Paper Coding Q2')

items = {
    "Coffee" : 7,
    "Pen" : 3,
    "Paper cup" : 2,
    "Milk" : 1,
    "Coke" : 4,
    "Book" : 5
}

n = input("Enter name of the item: ")
print(items[n]) 

"""

print()
print('********************')
print('Pair Programming Q1')

items ={
    'Coffee' : 7,
    'Pen' : 3,
    'Paper cup' : 2,
    'Milk' : 1,
    'Coke' : 4,
    'Book' : 5
}

while True : 
    option = int(input("Select menu: \n1 - check stock\n2 - warehousing\n3 - release\n4 - add stock\n5 - total stock\n6 - exit\n:"))
    if option == 1: 
        item = input("[check stock] Enter item name: ")
        stock = items[item]
        print('Stock :', stock)
    elif option == 2:
        print('[Warehousing]')
        for key, value in items.items():
            print(key, ':', value)
    elif option == 3: 
        item, quantity = input('[release] Enter item and quantity:').split()
        quantity = int(quantity)
        items[item] -= quantity
        stock = items[item]
        print('Stock: ', stock)
    elif option == 4: 
        item, quantity = input('[inventory] Enter item and quantity:').split()
        quantity = int(quantity)
        items[item] += quantity
        stock = items[item]
        print('New Stock: ', stock)
    elif option == 5:
        total= 0
        for s in items.values():
            total += s
        print('Total Stock: ', total)
    elif option == 6:
        break
    else: 
        print('Invalid option')
        