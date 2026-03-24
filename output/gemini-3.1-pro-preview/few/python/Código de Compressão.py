import sys

input_data = sys.stdin.read().split()
if len(input_data) < 2:
    exit()

n = int(input_data[0])
s = input_data[1]

ans = []
count = 1
prev = s[0]

for i in range(1, len(s)):
    if s[i] == prev:
        count += 1
    else:
        ans.append(f"{count} {prev}")
        prev = s[i]
        count = 1
ans.append(f"{count} {prev}")

print(" ".join(ans))