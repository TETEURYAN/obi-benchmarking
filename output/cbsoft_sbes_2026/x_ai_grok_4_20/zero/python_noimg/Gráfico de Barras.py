
N = int(input())
X = list(map(int, input().split()))
H = max(X)

for h in range(H - 1, -1, -1):
    linha = []
    for x in X:
        if x > h:
            linha.append('1')
        else:
            linha.append('0')
    print(' '.join(linha))
