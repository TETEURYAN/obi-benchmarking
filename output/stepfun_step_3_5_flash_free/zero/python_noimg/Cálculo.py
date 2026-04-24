M, N = map(int, input().split())
X = list(map(int, input().split()))
Y = list(map(int, input().split()))
L = max(M, N)
carry = 0
bits = []
for i in range(L-1, -1, -1):
    bx = X[i] if i < M else 0
    by = Y[i] if i < N else 0
    s = bx + by + carry
    bits.append(s % 2)
    carry = s // 2
bits.reverse()
while bits and bits[-1] == 0:
    bits.pop()
print(' '.join(map(str, bits)))