import re
lst = []
results_xmas = 0

with open('C:/Users/sweet/Downloads/input_4.txt', 'r') as file:
    for lines in file:
        lines = re.sub(r'\n', '', lines.strip())
        characters = lines.split()
        lst.extend([list(character) for character in characters])

for i in range(len(lst)):
    for j in range(len(lst[i]) - 3):
        if lst[i][j] == 'X':
            if lst[i][j+1] == 'M':
                if lst[i][j+2] == 'A':
                    if lst[i][j+3] == 'S':
                        results_xmas += 1
        elif lst[i][j] == 'S':
            if lst[i][j+1] == 'A':
                if lst[i][j+2] == 'M':
                    if lst[i][j+3] == 'X':
                        results_xmas += 1
        else:
            pass

for i in range(len(lst) - 3):
    for j in range(len(lst[i])):
        if lst[i][j] == 'X':
            if lst[i+1][j] == 'M':
                if lst[i+2][j] == 'A':
                    if lst[i+3][j] == 'S':
                        results_xmas += 1
        elif lst[i][j] == 'S':
            if lst[i+1][j] == 'A':
                if lst[i+2][j] == 'M':
                    if lst[i+3][j] == 'X':
                        results_xmas += 1
        else:
            pass

for i in range(len(lst) - 3):
    for j in range(len(lst[i]) -3):
        if lst[i][j] == 'X':
            if lst[i+1][j+1] == 'M':
                if lst[i+2][j+2] == 'A':
                    if lst[i+3][j+3] == 'S':
                        results_xmas += 1
        elif lst[i][j] == 'S':
            if lst[i+1][j+1] == 'A':
                if lst[i+2][j+2] == 'M':
                    if lst[i+3][j+3] == 'X':
                        results_xmas += 1
        else:
            pass

for i in range(3, len(lst)):
    for j in range(len(lst[i]) - 3):
        if lst[i][j] == 'X':
            if lst[i-1][j+1] == 'M':
                if lst[i-2][j+2] == 'A':
                    if lst[i-3][j+3] == 'S':
                        results_xmas += 1
        elif lst[i][j] == 'S':
            if lst[i-1][j+1] == 'A':
                if lst[i-2][j+2] == 'M':
                    if lst[i-3][j+3] == 'X':
                        results_xmas += 1
        else:
            pass

print(f'XMAS appears {results_xmas} times.')

# Part 2
results_x_mas = 0

for i in range(1, len(lst) - 1):
    for j in range(1, len(lst[i]) - 1):
        if lst[i][j] == 'A':
            if lst[i-1][j-1] == 'M' and lst[i-1][j+1] == 'M' and lst[i+1][j-1] == 'S' and lst[i+1][j+1] == 'S':
                results_x_mas += 1
            elif lst[i-1][j-1] == 'S' and lst[i-1][j+1] == 'M' and lst[i+1][j-1] == 'S' and lst[i+1][j+1] == 'M':
                results_x_mas += 1
            elif lst[i-1][j-1] == 'S' and lst[i-1][j+1] == 'S' and lst[i+1][j-1] == 'M' and lst[i+1][j+1] == 'M':
                results_x_mas += 1
            elif lst[i-1][j-1] == 'M' and lst[i-1][j+1] == 'S' and lst[i+1][j-1] == 'M' and lst[i+1][j+1] == 'S':
                results_x_mas += 1
            else:
                pass
        else:
            pass

print(f'X-MAS appears {results_x_mas} times.')