import sys

def main():
    # Ler toda a entrada de uma vez para performance
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    test_case_num = 1
    output_lines = []

    while True:
        try:
            n_str = next(iterator)
            m_str = next(iterator)
        except StopIteration:
            break
        
        n = int(n_str)
        m = int(m_str)

        if n == 0 and m == 0:
            break

        # Ler as temperaturas
        temps = []
        for _ in range(n):
            temps.append(int(next(iterator)))

        # Sliding Window para calcular a soma
        # Inicializa a soma com os primeiros M elementos
        current_sum = sum(temps[:m])
        
        # A média deve ser truncada (parte inteira).
        # Em Python, int(x) trunca em direção a zero, o que é o comportamento esperado
        # para o problema (ex: -8.5 vira -8, e não -9 como na divisão inteira //).
        min_avg = int(current_sum / m)
        max_avg = int(current_sum / m)

        # Desliza a janela
        for i in range(m, n):
            current_sum += temps[i] - temps[i - m]
            current_avg = int(current_sum / m)
            
            if current_avg < min_avg:
                min_avg = current_avg
            if current_avg > max_avg:
                max_avg = current_avg

        output_lines.append(f"Teste {test_case_num}")
        output_lines.append(f"{min_avg} {max_avg}")
        output_lines.append("") # Linha em branco
        
        test_case_num += 1

    # Imprimir resultado
    sys.stdout.write("\n".join(output_lines))

if __name__ == "__main__":
    main()