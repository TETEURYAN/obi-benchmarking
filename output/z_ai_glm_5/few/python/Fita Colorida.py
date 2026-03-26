import sys

def solve():
    # Leitura rápida de todos os dados de entrada
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    # O primeiro elemento é N, o tamanho da fita
    n = int(input_data[0])
    
    # Os próximos N elementos são os valores da fita (-1 ou 0)
    # Convertendo para inteiros
    tape = list(map(int, input_data[1:n+1]))
    
    # Inicializa o vetor de distâncias com um valor grande (maior que N)
    # Usamos n + 1 para garantir que seja maior que qualquer distância possível na fita
    distances = [n + 1] * n
    
    # Primeira passagem: da esquerda para a direita
    # Armazena a distância até o '0' mais recente à esquerda
    last_zero = -1
    for i in range(n):
        if tape[i] == 0:
            last_zero = i
            distances[i] = 0
        elif last_zero != -1:
            distances[i] = i - last_zero
            
    # Segunda passagem: da direita para a esquerda
    # Compara a distância atual com a distância até o '0' mais recente à direita
    last_zero = -1
    for i in range(n - 1, -1, -1):
        if tape[i] == 0:
            last_zero = i
        elif last_zero != -1:
            # A distância é o mínimo entre a já calculada (vinda da esquerda) e a vinda da direita
            distances[i] = min(distances[i], last_zero - i)
            
    # Aplica o limite de tom 9 (distância >= 9 vira 9)
    # Imprime o resultado formatado com espaços
    output = []
    for d in distances:
        if d > 9:
            output.append('9')
        else:
            output.append(str(d))
            
    print(' '.join(output))

if __name__ == "__main__":
    solve()