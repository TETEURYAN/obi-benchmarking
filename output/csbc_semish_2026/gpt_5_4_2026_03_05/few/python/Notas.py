import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

n = data[0]
grades = data[1:1 + n]

freq = [0] * 101
for g in grades:
    freq[g] += 1

best_grade = 0
best_count = -1

for grade in range(101):
    if freq[grade] > best_count or (freq[grade] == best_count and grade > best_grade):
        best_count = freq[grade]
        best_grade = grade

print(best_grade)