
N = int(input())
divs = list(map(int, input().split()))

estoque = 0
for i in range(N):
    partes = divs[i]
    estoque += partes - 1
    if i < N - 1:
        estoque -= 1

print(estoque)
