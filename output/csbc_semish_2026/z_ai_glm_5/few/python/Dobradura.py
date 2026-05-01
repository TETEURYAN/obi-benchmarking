import sys

def solve():
    # Leitura rápida de toda a entrada
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    test_case_number = 1
    output_lines = []
    
    for token in input_data:
        n = int(token)
        
        # Verifica condição de parada
        if n == -1:
            break
            
        # Cálculo do resultado: (2^N + 1)^2
        # Usando bit shift para potência de 2: 1 << n é igual a 2^n
        side_length = (1 << n) + 1
        result = side_length * side_length
        
        # Formatação da saída
        output_lines.append(f"Teste {test_case_number}")
        output_lines.append(str(result))
        output_lines.append("") # Linha em branco
        
        test_case_number += 1
        
    # Imprime tudo de uma vez para eficiência
    sys.stdout.write('\n'.join(output_lines))

if __name__ == "__main__":
    solve()