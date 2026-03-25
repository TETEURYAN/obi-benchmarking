import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])
s = input_data[1]

max_len = 1
for i in range(n):
    l, r = i, i
    while l >= 0 and r < n and s[l] == s[r]:
        if r - l + 1 > max_len:
            max_len = r - l + 1
        l -= 1
        r += 1
    
    l, r = i, i + 1
    while l >= 0 and r < n and s[l] == s[r]:
        if r - l + 1 > max_len:
            max_len = r - l + 1
        l -= 1
        r += 1

print(max_len)