import re
lst = []
lst_index = []
lst_value = []
diff = 0
similarity = 0

with open('C:/Users/sweet/Downloads/input.txt', 'r') as file:
    for lines in file:
        lst.extend(re.split(' ', lines.strip()))

lst = [int(i) for i in lst if i]

for i in range(len(lst)):
    if i % 2 == 0:
        lst_index.append(lst[i])
    else:
        lst_value.append(lst[i])

for i in range(len(lst_index)):
    diff += abs(sorted(lst_index)[i] - sorted(lst_value)[i])

print(f'diff = {diff}')

for i in range(len(lst_index)):
    similarity += lst_index[i] * lst_value.count(lst_index[i])

print(f'similarity = {similarity}')