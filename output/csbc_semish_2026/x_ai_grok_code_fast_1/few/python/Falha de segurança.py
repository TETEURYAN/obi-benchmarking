import sys
from collections import Counter

input_data = sys.stdin.read().split()
N = int(input_data[0])
passwords = input_data[1:]

count = Counter(passwords)
num_contain = Counter()

for pwd in passwords:
    for i in range(len(pwd)):
        for j in range(i + 1, len(pwd) + 1):
            sub = pwd[i:j]
            if sub in count:
                num_contain[sub] += 1

total = 0
for s in count:
    total += num_contain[s] * count[s] - count[s]

print(total)