"""print('Prime List')

prime_list = [2,3,5,7]
print('Prime numbers: ', prime_list)
prime_list.append(11)
print('Prime numbers after addition: ', prime_list)

print()
print('Out')
list1 = [3,5,7]

list2 = [2,3,5,7]
for i in list1 :
    #print(i)
    for j in list2 :
        print(f"{i} * {j} = ", i*j)
        #print("{} * {} = {}".format(i,j,i*j))
    print('out oj j')
print('out of i')
"""

print()
print('***Average***')

person_set = set() 
person_set1 = set()
person1 = ['kaara', 25, 1, 101, 102]
person2 = ['skrilla', 26, 7, 33, 104]
person3 = ['code', 27, 33, 105, 106]
person4 = ['py', 33, 33, 107, 108]

person_list = person1 + person2 + person3 + person4
#print(len(person_list))
#'skrilla', 25, 1, 101, 102, 'skrilla', 25, 1, 103, 104, 'code', 25, 1, 105, 106, 'code', 25, 1, 107, 108
#print(person_list[19])
#person_set = set(person_list)
#print(person_set)
#print(len(person_set))

"""
n_persons = len(person_list) / 5
print(n_persons)
age_sum = 0
for item in person_list[1::5]:
    age_sum += item
    print(item)

for i in person_list[1::5]:
    for j in person_list[1::5]:
        person_set.add(i) 
        person_set.add(j)
print(person_set)
print(len(person_set))
if 33 in person_set:
    person_set.remove(33)
print(person_set)
print(len(person_set))


print('********set1 before union')
for i in person_list[1::5]:
    for j in person_list[2::5]:
        person_set1.add(i) 
        person_set1.add(j)
print(person_set1)
print(len(person_set1))
if 33 in person_set1:
    person_set1.remove(33)
print(person_set1)
print(len(person_set1))

print('****find union\n')

print(person_set | person_set1)"""

for i in person_list[1::5]:
        person_set.add(i)
print('sum: ',sum(person_set))

for i in person_list[2::5]:
        person_set1.add(i) 
print("set_0 unsorted: ",person_set)
print("set_0 sorted: ",sorted(person_set))
print('set_1 unsorted: ',person_set1)
print('set_1 sorted: ',sorted(person_set1))
"""if 33 in person_set1:
    person_set1.remove(33)"""

print('****find find intersection\n')

print(person_set1 & person_set)
print('****find find union\n')
print(person_set1 | person_set)
print('****find find difference of set\n')
print(person_set - person_set1)
print('****find symmetric difference of set\n')
print(person_set ^ person_set1)




