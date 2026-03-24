import sys
from collections import deque

input_data = sys.stdin.read().split()
if not input_data:
    exit()

N = int(input_data[0])
D = int(input_data[1])
W = int(input_data[2])

p = [int(x) for x in input_data[3:]]

S = [0] * (N + 1)
for i in range(N):
    S[i+1] = S[i] + p[i]

A = [0] * (N - D + 1)
for i in range(N - D + 1):
    A[i] = S[i+D] - S[i]

Q = deque()
L = 0
ans = D

for R in range(D - 1, N):
    i = R - D + 1
    
    while Q and A[Q[-1]] <= A[i]:
        Q.pop()
    Q.append(i)
    
    while S[R+1] - S[L] - A[Q[0]] > W:
        if Q[0] == L:
            Q.popleft()
        L += 1
        
    length = R - L + 1
    if length > ans:
        ans = length

print(ans)