
equipes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']
vencedores = [None] * 16

for jogo in range(15):
    m, n = map(int, input().split())
    if m > n:
        vencedores[jogo] = 0
    else:
        vencedores[jogo] = 1

jogo_atual = 0
for rodada in range(4):
    for i in range(0, 8 - 2*rodada, 2):
        if vencedores[jogo_atual] == 0:
            vencedores[jogo_atual + 1] = vencedores[jogo_atual]
        else:
            vencedores[jogo_atual + 1] = vencedores[jogo_atual + 1]
        jogo_atual += 1

jogo_atual = 8
for rodada in range(2):
    for i in range(0, 4 - 2*rodada, 2):
        if vencedores[jogo_atual] == 0:
            vencedores[jogo_atual + 1] = vencedores[jogo_atual]
        else:
            vencedores[jogo_atual + 1] = vencedores[jogo_atual + 1]
        jogo_atual += 1

jogo_atual = 12
if vencedores[jogo_atual] == 0:
    vencedores[14] = vencedores[jogo_atual]
else:
    vencedores[14] = vencedores[jogo_atual + 1]

campeao = vencedores[14]
print(equipes[campeao])
