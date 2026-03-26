import sys

def main():
    # Lê todo o conteúdo da entrada padrão
    data = sys.stdin.read().split()
    
    if not data:
        return

    # O primeiro elemento é N, o tamanho da sequência
    n = int(data[0])
    
    # Os elementos seguintes são a sequência de 0s e 1s
    # Como data é uma lista de strings, podemos pegar a fatia correspondente
    sequence = data[1:n+1]
    
    count = 0
    
    # Itera pela sequência verificando o padrão "100"
    # O loop vai até n-2 para evitar acesso a índices inválidos (i, i+1, i+2)
    for i in range(n - 2):
        if sequence[i] == '1' and sequence[i+1] == '0' and sequence[i+2] == '0':
            count += 1
            
    print(count)

if __name__ == "__main__":
    main()