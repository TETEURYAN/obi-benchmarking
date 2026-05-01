
N = int(input())
A = list(map(int, input().split()))

tem_valle = False
for i in range(1, N-1):
    if A[i-1] > A[i] < A[i+1]:
        tem_valle = True
        break

print("S" if tem_valle else "N")
