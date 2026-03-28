import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])
r = [int(x) for x in input_data[1:]]

r.sort(reverse=True)

fi = 0
for i in range(n):
    if r[i] >= i + 1:
        fi = i + 1
    else:
        break

print(fi)