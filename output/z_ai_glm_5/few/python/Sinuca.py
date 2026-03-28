import sys

def main():
    # Leitura rápida de toda a entrada
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    n = int(input_data[0])
    # Converte a entrada para uma lista de inteiros
    balls = [int(x) for x in input_data[1:n+1]]
    
    # Simula o processo de formação do triângulo
    # A cada iteração, o tamanho da lista diminui em 1
    # Complexidade O(N^2), seguro para N <= 64
    while len(balls) > 1:
        next_row = []
        # Calcula a próxima fileira baseada na regra do produto
        # 1 * 1 = 1 (preta + preta = preta)
        # -1 * -1 = 1 (branca + branca = preta)
        # 1 * -1 = -1 (preta + branca = branca)
        for i in range(len(balls) - 1):
            next_row.append(balls[i] * balls[i+1])
        balls = next_row
    
    # Verifica o resultado final
    if balls[0] == 1:
        print("preta")
    else:
        print("branca")

if __name__ == "__main__":
    main()