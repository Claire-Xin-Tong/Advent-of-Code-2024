import re

lst = []
pos_even = []
pos_odd = []
mul = 0

with open('C:/Users/sweet/Downloads/input_3.txt', 'r') as file:
    for line in file:
        line = line.strip()
        line = re.findall(r'mul\(\d*,\d*\)', line)
        for item in line:
            item = item.strip('mul()')
            item = item.split(',')
            lst.extend(item)

lst = [int(i) for i in lst]

idx = 0
while idx in range(len(lst)):
    mul += lst[idx] * lst[idx+1]
    idx += 2

print(f'The result of the multiplications is {mul}.')

# Part 2
lst_1 = []
lst_num = []
mul_product = 0

with open('C:/Users/sweet/Downloads/input_3.txt', 'r') as file:
    for lines in file:
        lines = re.sub('\n', '', lines.strip())
        lst_1.extend(re.findall(r'do\(\)|don\'t\(\)|mul\(\d+,\d+\)', lines))

lst_1.insert(0, 'do()')

str_lst_1 = ''.join(lst_1)

lst_2 = re.findall(r'do\(\)[a-zA-Z0-9,()]+don\'t\(\)|do\(\)[a-zA-Z0-9,()]+$', str_lst_1)

for i in range(len(lst_2)):
    lst_num.extend(re.findall(r'[0-9]+', lst_2[i]))

lst_num = [int(i) for i in lst_num]

idx = 0
while idx in range(len(lst_num)):
    mul_product += lst_num[idx] * lst_num[idx+1]
    idx += 2

print(f'The result of the enabled multiplications is {mul_product}.')
