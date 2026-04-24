import sys

data = sys.stdin.read().split()
A = int(data[0])
B = int(data[1])

# Numbers that are both perfect square and perfect cube are perfect 6th powers
# n^6 for n = 1, 2, 3, ...
# Max value is 100,000,000
# 10^(8/6) ~ 10^1.333 ~ 21.5, so n up to 21

count = 0
n = 1
while True:
    val = n ** 6
    if val > B:
        break
    if val >= A:
        count += 1
    n += 1

print(count)