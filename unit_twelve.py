
print('Paper Coding Q1')
print()

sale_record = (100, 121, 120, 130, 140, 120, 122, 123, 190, 125)

sale_count = 0

for i in range(1, len(sale_record)):
    if sale_record[i] < sale_record[i - 1]:
        sale_count += 1
        print(sale_record[i])

print('Daily sales record:', sale_record)
print('Number if days had reduced sales:', sale_count)

print()

print('Pair Programming Question 1\n')

tup = (1, 2, 1, 2, 5, 4, 3, 2, 4, 7, 8, 9, 3, 7, 3, 9, 9, 7)

sorted_list = list(tup)

sorted_list.sort()

max = 1
most_frequent_element = None

for i in range(len(sorted_list)):
    count = 1
    for j in range(i, len(sorted_list)):
        if sorted_list[i] == sorted_list[j]:
            count += 1
    if count > max:
        max = count
        most_frequent_element = sorted_list[i]
    elif count == max:
        most_frequent_element = sorted_list[i]

print('The most frequent element: {}'.format(most_frequent_element))

print()
print('Pair Programming Question 2')

tuple1 = [(), (1,), [], 'abc', (), (),(1,),(), (),  ('a',), ('a', 'b'), ((),), '']

new_tuple = []

for item in tuple1:
    if item:
        new_tuple.append(item)
        
print('New List of Tuple: {}'.format(new_tuple))