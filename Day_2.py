lst = []
result = []

with open('C:/Users/sweet/Downloads/input_2.txt', 'r') as file:
    for line in file:
        line = line.strip()
        lst.append(line.split(' '))

for i in range(len(lst)):
    for j in range(len(lst[i])):
        lst[i][j] = int(lst[i][j])

lst_copy = [None] * len(lst)

for i in range(len(lst)):
    if sorted(lst[i]) == lst[i] or sorted(lst[i], reverse = True) == lst[i]:
        all_valid = True
        for j in range(len(lst[i]) - 1):
            diff = abs(int(lst[i][j+1]) - int(lst[i][j]))
            if not(1 <= diff <= 3):
                all_valid = False
                break # Exit early if any difference is invalid

        if all_valid: # Assign 'True' or 'False' after checking the entire condition
            lst_copy[i] = 'True'
        else:
            lst_copy[i] = 'False'
    else:
        lst_copy[i] = 'False'

print(lst)
print(lst_copy.count('True'))

# Part 2
import re

lst_1 = []
lst_diff = []
lst_diff_abs = []

with open('C:/Users/sweet/Downloads/input_2.txt', 'r') as file:
    for lines in file:
        lines.strip()
        lst_1.append(re.sub('\n', '', lines).split())

for i in range(len(lst_1)):
    for j in range(len(lst[i])):
        lst_1[i][j] = int(lst_1[i][j])


for i in range(len(lst_1)):
    lst_sub_diff = []
    lst_sub_diff_abs = []
    for j in range(len(lst_1[i]) - 1):
        diff = lst_1[i][j+1] - lst_1[i][j]
        lst_sub_diff.append(diff)
        lst_sub_diff_abs.append(abs(diff))
    lst_diff.append(lst_sub_diff)
    lst_diff_abs.append(lst_sub_diff_abs)

lst_diff_copy = []

for i in range(len(lst_diff)):
    sum_pos = sum(1 for j in lst_diff[i] if j > 0)
    sum_neg = sum(1 for j in lst_diff[i] if j < 0)
    sum_zero = sum(1 for j in lst_diff[i] if j == 0)
    if max(lst_diff[i]) <= 3 and min(lst_diff[i]) >= 1:
        if sum_pos >= len(lst_diff[i]) - 1:
            lst_diff_copy.append('True')
    elif max(lst_diff[i]) <= -1 and min(lst_diff[i]) >= -3:
        if sum_neg >= len(lst_diff[i]) - 1:
            lst_diff_copy.append('True')
    else:
        lst_diff_copy.append('False')


print(lst_diff_copy.count('True'))