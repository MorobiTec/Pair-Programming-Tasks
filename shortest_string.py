"""
s_list = ['abc', 'bcd', 'bcdefg', 'a', 'cddc', 'opq']
for i in s_list:
    if len(i) < len(s_list[0]):
        s_list[0] = i
        print('The shortest string :', s_list[0])

print()
s_list = ['abc', 'bcd', 'bcdefg', 'abba', 'cddc', 'opguiffjq']

for i in s_list:
    if len(i) > len(s_list[0]):
        s_list[0] = i
print('The longest string :', s_list[0])

"""

print()
s_list = ['abc', 'bcd', 'bcdefg', 'a', 'a' 'cddc', 'opq', 'opq']
s_list.sort(key=len)

for i in s_list:
    if len(i) == len(s_list[0]):
        print(i)

