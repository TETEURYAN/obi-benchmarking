import sys

def solve():
    # Leitura rápida de toda a entrada
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    # O primeiro elemento é a quantidade de números
    n = int(input_data[0])
    
    # Usaremos uma lista como pilha para manter os números ativos
    stack = []
    
    # Processamos os próximos N números (índices 1 a N na lista input_data)
    # O problema garante que a entrada contém N números após o primeiro.
    for i in range(1, n + 1):
        num = int(input_data[i])
        
        if num == 0:
            # "Zero" significa cancelar o último número.
            # Verificamos se a pilha não está vazia antes de remover.
            if stack:
                stack.pop()
        else:
            # Número válido é adicionado à pilha
            stack.append(num)
            
    # A soma total é a soma dos elementos restantes na pilha
    print(sum(stack))

if __name__ == "__main__":
    solve()