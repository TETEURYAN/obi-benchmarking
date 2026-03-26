import sys

def main():
    # Leitura rápida de toda a entrada
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    t = int(input_data[0])
    
    # Mapeamento dos fechamentos para aberturas para acesso O(1)
    matching = {')': '(', ']': '[', '}': '{'}
    open_brackets = {'(', '[', '{'}
    
    results = []
    
    # Iterar sobre as T cadeias
    # As cadeias começam no índice 1 do input_data
    for i in range(1, t + 1):
        s = input_data[i]
        stack = []
        is_valid = True
        
        for char in s:
            if char in open_brackets:
                stack.append(char)
            else:
                # É um caractere de fechamento
                if not stack:
                    is_valid = False
                    break
                
                top = stack.pop()
                # Verifica se o topo da pilha corresponde ao fechamento atual
                if matching[char] != top:
                    is_valid = False
                    break
        
        # A cadeia é válida se o loop terminou sem erros e a pilha está vazia
        if is_valid and not stack:
            results.append('S')
        else:
            results.append('N')
            
    # Imprimir resultados
    sys.stdout.write('\n'.join(results) + '\n')

if __name__ == '__main__':
    main()