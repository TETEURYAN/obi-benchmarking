import sys

# Aumentar o limite de recursão, embora não seja estritamente necessário para este problema iterativo
sys.setrecursionlimit(200000)

def solve():
    # Leitura rápida de toda a entrada
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    # Iterador para processar os tokens de entrada sequencialmente
    iterator = iter(input_data)
    
    try:
        # N é o número de rodadas
        n = int(next(iterator))
    except StopIteration:
        return

    dario_wins = 0
    xerxes_wins = 0

    # Processar cada rodada
    for _ in range(n):
        try:
            d = int(next(iterator))
            x = int(next(iterator))
        except StopIteration:
            break
        
        # A regra derivada do problema e casos de teste é:
        # A mão A vence a mão B se B for igual a (A+1)%5 ou (A+2)%5.
        # Isso equivale a dizer que A vence A+1 e A+2 (em módulo 5).
        # Exemplo: 0 vence 1 e 2. 3 vence 4 e 0 (confirmado pelo texto: "seta de 3 para 0").
        
        # Verificar se Dario vence
        # Dario vence se X for (D+1)%5 ou (D+2)%5
        if x == (d + 1) % 5 or x == (d + 2) % 5:
            dario_wins += 1
        else:
            # Como D != X e não há empate, se Dario não vence, Xerxes vence.
            # Verificação implícita: X vence se D for (X+1)%5 ou (X+2)%5
            xerxes_wins += 1

    # Determinar o vencedor final
    if dario_wins > xerxes_wins:
        print("dario")
    else:
        print("xerxes")

if __name__ == "__main__":
    solve()