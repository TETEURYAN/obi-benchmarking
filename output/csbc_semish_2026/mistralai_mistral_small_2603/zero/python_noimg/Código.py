
n = int(input().strip())
s = input().split()

count = 0
for i in range(n - 2):
    if s[i] == '1' and s[i+1] == '0' and s[i+2] == '0':
        count += 1
print(count)
