n = int(input())
divisoes = list(map(int, input().split()))
estoque = 0
for d in divisoes:
    estoque += d - 1
print(estoque)