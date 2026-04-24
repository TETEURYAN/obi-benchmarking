import sys

input_data = sys.stdin.read().split()
N = int(input_data[0])
K = int(input_data[1])
A = [i+1 for i in range(N) if int(input_data[2+i]) == 1]
B = [i+1 for i in range(N) if int(input_data[2+N+i]) == 1]
A.sort()
B.sort()
ans = 0
for i in range(K):
    ans += abs(A[i] - B[i])
print(ans)