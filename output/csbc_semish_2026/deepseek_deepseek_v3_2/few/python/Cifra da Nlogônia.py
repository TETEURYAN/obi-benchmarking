import sys

def cifra(palavra):
    alfabeto = "abcdefghijklmnopqrstuvxz"
    vogais = "aeiou"
    resultado = []
    
    mapa_consoante_para_seguinte = {}
    for i, letra in enumerate(alfabeto):
        if letra not in vogais:
            if letra == 'z':
                mapa_consoante_para_seguinte[letra] = 'z'
            else:
                proxima_consoante = alfabeto[i+1]
                while proxima_consoante in vogais:
                    i += 1
                    proxima_consoante = alfabeto[i+1]
                mapa_consoante_para_seguinte[letra] = proxima_consoante
    
    def vogal_mais_proxima(consoante):
        pos_consoante = alfabeto.index(consoante)
        distancias = []
        for vogal in vogais:
            pos_vogal = alfabeto.index(vogal)
            distancia = abs(pos_consoante - pos_vogal)
            distancias.append((distancia, vogal))
        distancias.sort(key=lambda x: (x[0], alfabeto.index(x[1])))
        return distancias[0][1]
    
    for letra in palavra:
        if letra in vogais:
            resultado.append(letra)
        else:
            resultado.append(letra)
            resultado.append(vogal_mais_proxima(letra))
            resultado.append(mapa_consoante_para_seguinte[letra])
    
    return ''.join(resultado)

if __name__ == "__main__":
    palavra = sys.stdin.readline().strip()
    print(cifra(palavra))