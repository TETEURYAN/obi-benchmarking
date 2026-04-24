import sys

def main():
    # Leitura rápida de toda a entrada
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    # O primeiro número é a quantidade de consultas C
    # As restrições garantem C >= 1, mas a verificação acima já cobre o vazio.
    # Converter para inteiro não é estritamente necessário para o slice, mas bom para clareza.
    # No entanto, como input_data[0] é string, podemos usá-lo diretamente se precisássemos apenas iterar.
    # Aqui usamos para definir o limite do loop.
    
    try:
        c = int(input_data[0])
    except ValueError:
        return

    stock = set()
    manufactured_count = 0
    
    # Processamos as consultas que começam no índice 1 até c+1
    # Usar range e acessar via índice é levemente mais rápido que iterar sobre o slice direto em alguns casos,
    # mas iterar sobre o slice é mais 'pythonico'. 
    # Dado C <= 10^5, qualquer um serve. Vamos de slice para simplicidade e velocidade.
    queries = input_data[1 : c + 1]
    
    for q_str in queries:
        length = int(q_str)
        if length in stock:
            stock.remove(length)
        else:
            stock.add(length)
            manufactured_count += 2
            
    print(manufactured_count)

if __name__ == "__main__":
    main()