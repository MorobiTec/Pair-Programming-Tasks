"""lambda"""

"""paper coding 1"""
print('paper coding 1')
n_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_list = []
for n in filter(lambda x: x % 2 == 0, n_list):
    even_list.append(n)

print(even_list)

"""paper coding 2"""
print()
print('paper coding 2')

n_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('even_list =', list(filter(lambda x: x % 2 == 0, n_list)))


"""paper coding 3"""
print()
print('paper coding 3')

a_list = ['a', 'b', 'c', 'd']

def upper(letter):
    return letter.upper()

upper_a_list = list(map(upper, a_list))

print(upper_a_list)

"""paper coding 4"""
print()
print('paper coding 4')

from functools import reduce

print('Sum of 1 to 100 :', reduce(lambda x, y: x + y, range(1, 101)))

"""Pair Programming"""

scores = [100, 90, 95, 90, 80, 70, 0, 80, 90, 90, 0, 90, 100, 75, 20, 30, 50, 90]

sub_groups = [scores[i: i + 3] for i in range(0, len(scores), 3)]
print('Sub-groups:', sub_groups)
valid_scores = [sub_group for sub_group in sub_groups if 0 not in sub_group]


n_students = len(scores) // 3
n_students_valid = len(valid_scores)
print('The number of total students is {}.'.format(n_students))
print('The number of students with valid scores is {}.'.format(n_students_valid))
print(valid_scores)