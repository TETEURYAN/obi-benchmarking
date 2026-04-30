
N = int(input())
divs = list(map(int, input().split()))

estoque = 0
for i in range(N):
    estoque += divs[i] - 1

print(estoque + 1)
