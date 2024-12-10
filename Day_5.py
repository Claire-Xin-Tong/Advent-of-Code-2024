import re
lst_rules = []
lst_pages = []
rules_keys = []
rules_values = []
rule_dict = {}
pages_correct = []
pages_correct_mid = []

with open('C:/Users/sweet/Downloads/input_5.txt', 'r') as file:
    sections = file.read()
    rules, pages = sections.split('\n\n')

    lst_rules.extend(re.findall('[0-9]+\|[0-9]+', rules))
    str_of_rules = '|'.join(lst_rules)
    lst_rules = re.split('\|', str_of_rules)
    for i in range(len(lst_rules) - 1):
        if i % 2 == 0:
            rule_dict[lst_rules[i]] = lst_rules[i+1]

    lst_pages.extend(pages.split('\n'))
    lst_pages = [re.split(',', i) for i in lst_pages]
    lst_pages.remove([''])

for i in range(len(lst_pages)):
    validity = True
    for j in range(len(lst_pages[i])):
        if lst_pages[i][j] in rule_dict.keys():
            value = rule_dict[lst_pages[i][j]]
            if value in lst_pages[i]:
                if j > lst_pages[i].index(value):
                    validity = False
                    break
        else:
            pass
    if validity:
        pages_correct.append(lst_pages[i])

for i in range(len(pages_correct)):
    if len(pages_correct[i]) % 2 == 0:
        k = int(len(pages_correct[i]) / 2)
        pages_correct_mid.append(int(pages_correct[i][k]))
    else:
        k = int((len(pages_correct[i]) - 1) / 2)
        pages_correct_mid.append(int(pages_correct[i][k]))

mul_product = sum(i for i in pages_correct_mid)

print(mul_product)
print(pages_correct)






