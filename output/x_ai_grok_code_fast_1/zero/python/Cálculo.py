
import sys

input = sys.stdin.read
data = input().split()

M = int(data[0])
N = int(data[1])
X = list(map(int, data[2:2+M]))
Y = list(map(int, data[2+M:2+M+N]))

max_len = max(M, N)
x_padded = X + [0] * (max_len - M)
y_padded = Y + [0] * (max_len - N)

result = []
carry = 0
for i in range(max_len - 1, -1, -1):
    s = x_padded[i] + y_padded[i] + carry
    result.append(s % 2)
    carry = s // 2

result = result[::-1]

while result and result[-1] == 0:
    result.pop()

print(' '.join(map(str, result)))
