import sys
from collections import Counter

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])
passwords = input_data[1:]

freq = Counter(passwords)

total_pairs = 0
for p in passwords:
    subs = set()
    length = len(p)
    for i in range(length):
        for j in range(i + 1, length + 1):
            subs.add(p[i:j])
    
    for sub in subs:
        if sub in freq:
            total_pairs += freq[sub]
            
    total_pairs -= 1

print(total_pairs)