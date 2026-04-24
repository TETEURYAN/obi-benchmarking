import sys

# Aumentar o limite de recursão é uma boa prática em problemas de OBI/ICPC,
# embora este problema específico use uma solução iterativa.
sys.setrecursionlimit(200000)

def solve():
    # Lê todo o conteúdo da entrada padrão de uma vez.
    # Isso é mais eficiente que ler linha por linha com input() para arquivos grandes.
    data = sys.stdin.read()
    
    balance = 0
    
    # Itera sobre cada caractere do texto lido.
    # Como a primeira linha contém apenas o número N (sem chaves), 
    # processá-la não afeta o balanceamento.
    for char in data:
        if char == '{':
            balance += 1
        elif char == '}':
            if balance == 0:
                # Encontrou um fechamento '}' sem uma abertura correspondente.
                print('N')
                return
            balance -= 1
    
    # Se ao final o balanceamento for 0, as chaves estão corretas.
    if balance == 0:
        print('S')
    else:
        # Sobraram aberturas '{' sem fechamento.
        print('N')

if __name__ == '__main__':
    solve()