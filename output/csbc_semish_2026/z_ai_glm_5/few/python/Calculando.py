import sys

def solve():
    # Lê toda a entrada de uma vez para eficiência
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    idx = 0
    test_case_count = 1
    output_lines = []
    
    while idx < len(input_data):
        # Lê o número de operandos
        m = int(input_data[idx])
        idx += 1
        
        # Condição de parada
        if m == 0:
            break
        
        # Lê a expressão (que não contém espaços, então é um token único)
        expression = input_data[idx]
        idx += 1
        
        # Avaliação da expressão (Parsing manual)
        # Como só há + e -, a precedência é a mesma (da esquerda para direita).
        # Podemos iterar caractere por caractere.
        current_val = 0
        result = 0
        sign = 1  # 1 para positivo, -1 para negativo
        
        for char in expression:
            if char.isdigit():
                current_val = current_val * 10 + int(char)
            else:
                # Encontrou um operador, adiciona o número acumulado ao resultado
                result += sign * current_val
                current_val = 0 # Reseta o acumulador
                
                if char == '+':
                    sign = 1
                elif char == '-':
                    sign = -1
        
        # Adiciona o último número da expressão
        result += sign * current_val
        
        # Formata a saída
        output_lines.append(f"Teste {test_case_count}")
        output_lines.append(str(result))
        output_lines.append("") # Linha em branco
        
        test_case_count += 1
    
    # Imprime tudo de uma vez
    sys.stdout.write("\n".join(output_lines))

if __name__ == "__main__":
    solve()
    
```python
import sys

def solve():
    # Lê toda a entrada de uma vez para eficiência
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    idx = 0
    test_case_count = 1
    output_lines = []
    
    while idx < len(input_data):
        # Lê o número de operandos
        m = int(input_data[idx])
        idx += 1
        
        # Condição de parada
        if m == 0:
            break
        
        # Lê a expressão (que não contém espaços, então é um token único)
        expression = input_data[idx]
        idx += 1
        
        # Avaliação da expressão (Parsing manual)
        # Como só há + e -, a precedência é a mesma (da esquerda para direita).
        # Podemos iterar caractere por caractere.
        current_val = 0
        result = 0
        sign = 1  # 1 para positivo, -1 para negativo
        
        for char in expression:
            if char.isdigit():
                current_val = current_val * 10 + int(char)
            else:
                # Encontrou um operador, adiciona o número acumulado ao resultado
                result += sign * current_val
                current_val = 0 # Reseta o acumulador
                
                if char == '+':
                    sign = 1
                elif char == '-':
                    sign = -1
        
        # Adiciona o último número da expressão
        result += sign * current_val
        
        # Formata a saída
        output_lines.append(f"Teste {test_case_count}")
        output_lines.append(str(result))
        output_lines.append("") # Linha em branco
        
        test_case_count += 1
    
    # Imprime tudo de uma vez
    sys.stdout.write("\n".join(output_lines))

if __name__ == "__main__":
    solve()
```