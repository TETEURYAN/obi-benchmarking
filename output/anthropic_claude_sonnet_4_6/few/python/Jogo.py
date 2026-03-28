import sys

data = sys.stdin.read().split()
X = int(data[0])
results = []
for i in range(1, len(data)):
    T = int(data[i])
    if T > X:
        results.append("menor")
    elif T < X:
        results.append("maior")
    else:
        results.append("correto")
        break
print('\n'.join(results))