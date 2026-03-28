
import sys

def main():
    vogais = {'a', 'e', 'i', 'o', 'u'}
    alfabeto = "abcdefghijklmnopqrstuvxz"
    vogais_ordenadas = ['a', 'e', 'i', 'o', 'u']
    consoantes = [c for c in alfabeto if c not in vogais]

    def encontrar_vogal_proxima(consoante):
        idx = alfabeto.index(consoante)
        vogais_proximas = []
        for v in vogais_ordenadas:
            dist = abs(alfabeto.index(v) - idx)
            vogais_proximas.append((dist, v))
        vogais_proximas.sort()
        return vogais_proximas[0][1]

    def processar_consoante(c):
        vogal = encontrar_vogal_proxima(c)
        idx_consoante = alfabeto.index(c)
        prox_consoante = alfabeto[(idx_consoante + 1) % len(alfabeto)]
        return f"{c}{vogal}{prox_consoante}"

    palavra = sys.stdin.readline().strip()
    resultado = []
    for char in palavra:
        if char in vogais:
            resultado.append(char)
        else:
            resultado.append(processar_consoante(char))
    print(''.join(resultado))

if __name__ == "__main__":
    main()
