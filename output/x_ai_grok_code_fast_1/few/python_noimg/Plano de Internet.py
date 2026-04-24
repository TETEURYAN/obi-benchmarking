import sys

input_data = sys.stdin.read().split()
X = int(input_data[0])
N = int(input_data[1])
M = [int(input_data[i + 2]) for i in range(N)]

quota_atual = X
for m in M:
    sobra = quota_atual - m
    quota_atual = X + sobra

print(quota_atual)