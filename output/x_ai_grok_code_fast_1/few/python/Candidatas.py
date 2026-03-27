import sys
import math

input_data = sys.stdin.read().split()
idx = 0
N = int(input_data[idx])
idx += 1
M = int(input_data[idx])
idx += 1
S = [int(input_data[idx + i]) for i in range(N)]
idx += N
operations = []
for _ in range(M):
    T = int(input_data[idx])
    idx += 1
    if T == 1:
        I = int(input_data[idx])
        idx += 1
        V = int(input_data[idx])
        idx += 1
        operations.append((1, I - 1, V))
    else:
        E = int(input_data[idx])
        idx += 1
        D = int(input_data[idx])
        idx += 1
        operations.append((2, E - 1, D))
for op in operations:
    if op[0] == 1:
        S[op[1]] = op[2]
    else:
        L = op[1]
        R = op[2]
        count = 0
        left = L
        current_gcd = 0
        for right in range(L, R + 1):
            current_gcd = math.gcd(current_gcd, S[right])
            if current_gcd > 1:
                count += right - left + 1
            else:
                while current_gcd == 1 and left <= right:
                    left += 1
                    if left <= right:
                        current_gcd = S[right]
                    else:
                        current_gcd = 0
                if current_gcd > 1:
                    count += right - left + 1
        print(count)