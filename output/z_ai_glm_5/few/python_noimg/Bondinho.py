import sys

def main():
    # Leitura rápida de todos os dados de entrada
    data = sys.stdin.read().split()
    
    # Verificação de segurança para garantir que há dados suficientes
    if len(data) < 2:
        return

    # Conversão dos valores de entrada
    a = int(data[0])
    m = int(data[1])
    
    # Verificação da condição: capacidade máxima de 50 pessoas
    if a + m <= 50:
        print('S')
    else:
        print('N')

if __name__ == "__main__":
    main()