import sys

data = sys.stdin.read().split()
if not data:
    exit()
n = int(data[0])
k = int(data[1])
grades = list(map(int, data[2:2+n]))
grades.sort(reverse=True)
print(grades[k-1])