import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])
grades = [int(x) for x in input_data[1:n+1]]

freq = {}
for g in grades:
    freq[g] = freq.get(g, 0) + 1

max_freq = -1
best_grade = -1

for g, f in freq.items():
    if f > max_freq:
        max_freq = f
        best_grade = g
    elif f == max_freq:
        if g > best_grade:
            best_grade = g

print(best_grade)