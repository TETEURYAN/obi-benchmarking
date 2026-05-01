import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])
word1 = input_data[1]
m = int(input_data[2])
word2 = input_data[3]

limit = min(n, m)
ans = 0
for i in range(limit):
    if word1[i] == word2[i]:
        ans += 1
    else:
        break

print(ans)