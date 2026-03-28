import sys

def solve():
    # Leitura da entrada. read().strip() lê a linha inteira e remove quebras de linha/espaços.
    placa = sys.stdin.read().strip()

    # Verificação do Antigo Padrão Brasileiro (LLL-DDDD)
    # Tamanho deve ser exatamente 8.
    if len(placa) == 8:
        # Verifica se os 3 primeiros são letras, o 4º é hífen e os 4 últimos são dígitos.
        # isupper() retorna True apenas para letras maiúsculas.
        if (placa[0].isupper() and placa[1].isupper() and placa[2].isupper() and
            placa[3] == '-' and
            placa[4].isdigit() and placa[5].isdigit() and placa[6].isdigit() and placa[7].isdigit()):
            print(1)
            return

    # Verificação do Novo Padrão Mercosul (LLLNLDD)
    # Tamanho deve ser exatamente 7.
    if len(placa) == 7:
        # Verifica: 3 letras, 1 dígito, 1 letra, 2 dígitos.
        if (placa[0].isupper() and placa[1].isupper() and placa[2].isupper() and
            placa[3].isdigit() and
            placa[4].isupper() and
            placa[5].isdigit() and placa[6].isdigit()):
            print(2)
            return

    # Se não se encaixar em nenhum dos padrões acima, é falsificada.
    print(0)

if __name__ == "__main__":
    solve()