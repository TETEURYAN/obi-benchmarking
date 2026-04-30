
import sys

input = sys.stdin.read
data = input().split()

index = 0
test = 1
while True:
    S = int(data[index])
    index += 1
    if S == 0:
        break
    X = []
    Y = []
    for i in range(S):
        X.append(int(data[index]))
        Y.append(int(data[index + 1]))
        index += 2
    X.sort()
    Y.sort()
    mx = X[S // 2]
    my = Y[S // 2]
    print(f"Teste {test}")
    print(mx, my)
    print()
    test += 1
