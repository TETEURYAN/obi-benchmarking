import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    A = int(data[0])
    B = int(data[1])

    # Cadeira de Ana: começa em 1, conta A cadeiras no sentido anti-horário
    # As cadeiras são 0,1,2. Começando em 1, a sequência é 1,2,0,1,2,0,...
    # Para A=1 -> cadeira 1, A=2 -> cadeira 2, A=3 -> cadeira 0, etc.
    # Podemos calcular: (1 + A) % 3? Não, porque a contagem inclui a primeira cadeira.
    # Vamos simular: começando em 1, para i de 1 até A:
    #   posição inicial = 1
    #   para cada passo: próximo = (atual + 1) % 3
    # Mas como A pode ser até 1000, simulação é rápida.
    pos_ana = 1
    for _ in range(A):
        pos_ana = (pos_ana + 1) % 3

    # Cadeira de Beatriz: começa em 1, conta B cadeiras
    pos_beatriz = 1
    for _ in range(B):
        pos_beatriz = (pos_beatriz + 1) % 3

    # Se a cadeira final de Beatriz estiver ocupada por Ana, ela senta na próxima
    if pos_beatriz == pos_ana:
        pos_beatriz = (pos_beatriz + 1) % 3

    # Cadeira de Carolina: a única livre
    # As cadeiras são 0,1,2. Soma das ocupadas = pos_ana + pos_beatriz
    # A livre é 3 - (pos_ana + pos_beatriz) se forem diferentes, mas cuidado com módulo.
    # Podemos encontrar a livre por exclusão.
    ocupadas = {pos_ana, pos_beatriz}
    for cadeira in (0, 1, 2):
        if cadeira not in ocupadas:
            print(cadeira)
            return

if __name__ == "__main__":
    main()