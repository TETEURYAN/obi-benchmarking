import sys

def solve():
    # Lê a linha inteira de entrada. 
    # sys.stdin.read() lê tudo, strip() remove a quebra de linha final.
    texto = sys.stdin.read().strip()
    
    # Conjunto das letras obrigatórias para o pangrama (sem k, w, y)
    alfabeto_alvo = set("abcdefghijlmnopqrstuvxz")
    
    # Conjunto das letras presentes no texto de entrada
    letras_presentes = set(texto)
    
    # Removemos os caracteres que não são letras (espaço, vírgula, dois pontos)
    # O problema garante que não há outros caracteres, então basta remover estes.
    letras_presentes.discard(' ')
    letras_presentes.discard(',')
    letras_presentes.discard(':')
    
    # Verifica se o conjunto de letras presentes é igual ao alfabeto alvo
    # Poderia ser alfabeto_alvo.issubset(letras_presentes) também
    if letras_presentes == alfabeto_alvo:
        print("S")
    else:
        print("N")

if __name__ == "__main__":
    solve()