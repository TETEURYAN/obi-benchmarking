
import sys

input = sys.stdin.read
data = input().split()

index = 0
N = int(data[index])
index += 1
heights = []
for i in range(N):
    heights.append(int(data[index]))
    index += 1
Q = int(data[index])
index += 1
for _ in range(Q):
    T = int(data[index])
    index += 1
    I = int(data[index])
    index += 1
    X = int(data[index])
    index += 1
    if T == 0:
        if I == 0:
            heights.insert(0, X)
        else:
            heights.insert(I, X)
    else:
        val = heights[I - 1] + X
        found = False
        for j in range(I - 2, -1, -1):
            if heights[j] > val:
                print(j + 1)
                found = True
                break
        if not found:
            print(0)
