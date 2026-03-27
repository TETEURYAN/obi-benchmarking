import sys

input_data = sys.stdin.read().split()
idx = 0
N = int(input_data[idx])
idx += 1
M = int(input_data[idx])
idx += 1
T = []
for _ in range(M):
    T.append(int(input_data[idx]))
    idx += 1

sc = [0] * (M + 1)
surviving = []
x = 1
while len(surviving) < 10000 and x <= N:
    pos = x
    survived = True
    for i in range(M):
        if pos % T[i] == 0:
            survived = False
            break
        sc[i + 1] += 1
        pos = sc[i + 1]
    if survived:
        surviving.append(x)
    x += 1

for num in surviving:
    print(num)