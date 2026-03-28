import sys

# Define o limite de recursão para segurança, embora a solução seja iterativa.
sys.setrecursionlimit(200000)

def solve():
    # Lê toda a entrada de uma vez para maior performance
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    n = int(input_data[0])
    # Garante que pegamos apenas as N strings, ignorando possíveis quebras de linha extras
    strings = input_data[1:n+1]
    
    # Conjunto para armazenar strings completas já vistas (verificação de duplicatas)
    seen_strings = set()
    
    # Listas de conjuntos para armazenar sufixos e prefixos.
    # suffixes[l] armazena todos os sufixos de comprimento l das strings anteriores.
    # prefixes[l] armazena todos os prefixos de comprimento l das strings anteriores.
    # Os índices vão de 0 a 10. Usamos 1 a 10.
    suffixes = [set() for _ in range(11)]
    prefixes = [set() for _ in range(11)]
    
    for s in strings:
        # Verificação 1: A string atual é igual a alguma string anterior?
        # Se sim, Sk é substring de Sa (ou SaSa), o que invalida o código.
        if s in seen_strings:
            print(s)
            return
        
        # Verificação 2: A string atual é formada pela junção de um sufixo anterior
        # e um prefixo anterior?
        # Sk pode ser substring de SaSb se "cortar" a fronteira.
        # Sk = sufixo(Sa, L) + prefixo(Sb, 10-L)
        # L varia de 1 a 9 (se L=0 ou 10, cai no caso de strings iguais ou contidas).
        is_invalid = False
        for L in range(1, 10):
            # Verifica se o início de s (tamanho L) é um sufixo conhecido
            # E se o restante de s (tamanho 10-L) é um prefixo conhecido
            if s[:L] in suffixes[L] and s[L:] in prefixes[10-L]:
                is_invalid = True
                break
        
        if is_invalid:
            print(s)
            return
            
        # Se a string é válida, adiciona suas partes aos conjuntos para verificações futuras
        seen_strings.add(s)
        for length in range(1, 11):
            suffixes[length].add(s[-length:])
            prefixes[length].add(s[:length])
            
    # Se o loop terminar, nenhuma string invalidou o código
    print("ok")

if __name__ == '__main__':
    solve()