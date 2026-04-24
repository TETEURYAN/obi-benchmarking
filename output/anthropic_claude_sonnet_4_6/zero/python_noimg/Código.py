
n = int(input())
seq = input().split()
count = 0
for i in range(n - 2):
    if seq[i] == '1' and seq[i+1] == '0' and seq[i+2] == '0':
        count += 1
print(count)
