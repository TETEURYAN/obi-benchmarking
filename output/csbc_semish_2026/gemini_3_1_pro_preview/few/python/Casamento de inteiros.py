import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

A = input_data[0]
B = input_data[1]

max_len = max(len(A), len(B))
A = A.zfill(max_len)
B = B.zfill(max_len)

resA = []
resB = []

for a, b in zip(A, B):
    if a > b:
        resA.append(a)
    elif a < b:
        resB.append(b)
    else:
        resA.append(a)
        resB.append(b)

strA = "".join(resA)
strB = "".join(resB)

valA = int(strA) if strA else -1
valB = int(strB) if strB else -1

print(*sorted([valA, valB]))