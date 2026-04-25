import sys

# Alfabeto e vogais definidos no problema
ALFABETO = "abcdefghijklmnopqrstuvxz"
VOGAIS = "aeiou"

# Pré-computação das consoantes para acesso rápido e determinação da próxima
CONSOANTES = [c for c in ALFABETO if c not in VOGAIS]

def main():
    # Leitura da entrada
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    palavra = input_data[0]
    
    resultado = []
    
    for char in palavra:
        if char in VOGAIS:
            # Vogais não são modificadas
            resultado.append(char)
        else:
            # 1. Consoante original
            resultado.append(char)
            
            # 2. Vogal mais próxima
            idx_char = ALFABETO.index(char)
            melhor_vogal = ''
            menor_dist = 100 # Valor inicial alto o suficiente
            
            # Itera sobre as vogais para encontrar a de menor distância
            # Em caso de empate, a que aparece primeiro no alfabeto (iteração) vence
            for v in VOGAIS:
                idx_v = ALFABETO.index(v)
                dist = abs(idx_char - idx_v)
                if dist < menor_dist:
                    menor_dist = dist
                    melhor_vogal = v
            
            resultado.append(melhor_vogal)
            
            # 3. Próxima consoante
            idx_cons_atual = CONSOANTES.index(char)
            if idx_cons_atual + 1 < len(CONSOANTES):
                resultado.append(CONSOANTES[idx_cons_atual + 1])
            else:
                # Se for a última consoante ('z'), repete ela mesma
                resultado.append(char)
                
    print("".join(resultado))

if __name__ == "__main__":
    main()