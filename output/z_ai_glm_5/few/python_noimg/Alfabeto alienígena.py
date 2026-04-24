import sys

def solve():
    # Leitura rápida de toda a entrada
    input_data = sys.stdin.read().split()
    
    # Verificação de segurança caso a entrada esteja vazia
    if not input_data:
        return

    # Parse dos inteiros K e N
    # input_data[0] é K, input_data[1] é N
    k = int(input_data[0])
    n = int(input_data[1])
    
    # input_data[2] contém os K caracteres do alfabeto (contíguos, sem espaços)
    # input_data[3] contém os N caracteres da mensagem (contíguos, sem espaços)
    # Convertemos o alfabeto para um set para busca O(1)
    alphabet_set = set(input_data[2])
    message = input_data[3]
    
    # Verifica cada caractere da mensagem
    for char in message:
        if char not in alphabet_set:
            print("N")
            return
            
    # Se o loop terminou, todos os caracteres são válidos
    print("S")

if __name__ == "__main__":
    solve()