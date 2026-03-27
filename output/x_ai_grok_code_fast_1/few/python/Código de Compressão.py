import sys

data = sys.stdin.read().split()
N = int(data[0])
S = data[1]

result = []
i = 0
while i < N:
    char = S[i]
    count = 1
    i += 1
    while i < N and S[i] == char:
        count += 1
        i += 1
    result.append(str(count) + " " + char)

print(" ".join(result))