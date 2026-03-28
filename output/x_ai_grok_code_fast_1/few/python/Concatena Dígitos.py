import sys

input_data = sys.stdin.read().split()

N = int(input_data[0])
Q = int(input_data[1])
digits = list(map(int, input_data[2:2+N]))
prefix = [0] * (N+1)
for i in range(1, N+1):
    prefix[i] = prefix[i-1] + digits[i-1]
queries = input_data[2+N:]
for i in range(Q):
    L = int(queries[2*i])
    R = int(queries[2*i+1])
    K = R - L + 1
    sum_dig = prefix[R] - prefix[L-1]
    pot = (K - 1) * sum_dig * 11
    print(pot)