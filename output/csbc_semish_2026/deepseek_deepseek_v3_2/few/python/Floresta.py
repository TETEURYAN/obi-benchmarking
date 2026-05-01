import sys

def count_arrangements(N):
    # N = carvalhos + eucaliptos
    # carvalhos = (x+1)*(y+1)  (vértices do retângulo)
    # eucaliptos = x*y         (centros dos quadrados)
    # total = (x+1)*(y+1) + x*y = x*y + x + y + 1 + x*y = 2*x*y + x + y + 1
    # Rearranjando: 2*x*y + x + y + 1 = N
    # => 2*x*y + x + y = N - 1
    # => (2x + 1)(2y + 1) = 2N - 1
    # Seja M = 2N - 1
    # Precisamos contar pares (a,b) ímpares positivos com a*b = M e a <= b
    # E depois mapear para x = (a-1)//2, y = (b-1)//2
    
    M = 2 * N - 1
    if M <= 0:
        return 0
    
    # Contar divisores ímpares de M
    count = 0
    i = 1
    while i * i <= M:
        if M % i == 0:
            # Ambos divisores devem ser ímpares
            if i % 2 == 1 and (M // i) % 2 == 1:
                count += 1 if i * i == M else 2
        i += 2  # Apenas ímpares
    
    # Cada par (a,b) com a <= b corresponde a uma solução
    # Como contamos ambos os divisores simetricamente, o número de pares distintos é count/2
    return count // 2

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    N = int(data[0])
    print(count_arrangements(N))

if __name__ == "__main__":
    main()