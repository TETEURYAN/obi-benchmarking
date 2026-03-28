
import sys

# Leitura rápida de todos os dados de entrada
input_data = sys.stdin.read().split()

if not input_data:
    exit()

# Utilização de um iterador para processar os dados sequencialmente
iterator = iter(input_data)

try:
    # T é o comprimento total da estrada (embora não seja usado na lógica central)
    T = int(next(iterator))
    # N é o número de cidades
    N = int(next(iterator))
    
    cities = []
    for _ in range(N):
        cities.append(int(next(iterator)))
except StopIteration:
    exit()

# Ordena as posições das cidades para processamento linear
cities.sort()

# Inicializa a menor vizinhança com um valor infinito
min_neighborhood = float('inf')

# Itera sobre as cidades para calcular a vizinhança
# A vizinhança de uma cidade 'i' é limitada pelos pontos médios entre ela e seus vizinhos.
# O limite esquerdo é (cities[i] + cities[i-1]) / 2
# O limite direito é (cities[i+1] + cities[i]) / 2
# O tamanho da vizinhança é a diferença entre esses limites.
# Simplificando: (cities[i+1] - cities[i-1]) / 2
for i in range(1, N - 1):
    dist_prev = cities[i] - cities[i-1]
    dist_next = cities[i+1] - cities[i]
    
    current_neighborhood = (dist_prev + dist_next) / 2.0
    
    if current_neighborhood < min_neighborhood:
        min_neighborhood = current_neighborhood

# Imprime o resultado com exatamente duas casas decimais
print(f"{min_neighborhood:.2f}")
