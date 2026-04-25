
import sys

def main():
    # Lê toda a entrada de uma vez para maior eficiência
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        n = int(next(iterator))
    except StopIteration:
        return

    # Dicionário para mapear o número esquerdo (E) para a letra (C) e número direito (D)
    # mapa[E] = (C, D)
    mapa = {}
    
    # Variáveis para armazenar a primeira peça (E == 0)
    primeira_letra = ''
    proximo_id = -1
    
    for _ in range(n):
        try:
            e = int(next(iterator))
            c = next(iterator)
            d = int(next(iterator))
        except StopIteration:
            break
            
        if e == 0:
            primeira_letra = c
            proximo_id = d
        else:
            mapa[e] = (c, d)
            
    # Lista para construir a string final de forma eficiente
    resultado = [primeira_letra]
    
    # Percorre a cadeia de peças
    # O loop continua enquanto o ID do próximo nó não for 1 (indicador de fim)
    while proximo_id != 1:
        letra, novo_id = mapa[proximo_id]
        resultado.append(letra)
        proximo_id = novo_id
        
    sys.stdout.write("".join(resultado) + "\n")

if __name__ == "__main__":
    main()
