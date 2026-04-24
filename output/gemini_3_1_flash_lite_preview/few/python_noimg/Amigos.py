import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    k = int(input_data[1])
    
    a = input_data[2:2+n]
    b = input_data[2+n:2+2*n]
    
    pos_a = [i for i, val in enumerate(a) if val == '1']
    pos_b = [i for i, val in enumerate(b) if val == '1']
    
    # O problema pede que cada integrante do grupo esteja sentado de frente para outro integrante.
    # Como temos K integrantes em cada lado, e cada um deve ficar de frente para um integrante,
    # isso significa que o i-ésimo integrante do lado A deve ficar de frente para o i-ésimo integrante do lado B.
    # O custo para mover o i-ésimo integrante do lado A para a posição X e o i-ésimo do lado B para a posição X
    # é |pos_a[i] - X| + |pos_b[i] - X|.
    # A soma total é sum(|pos_a[i] - X_i| + |pos_b[i] - X_i|).
    # Para minimizar isso, X_i deve ser a mediana de pos_a[i] e pos_b[i], mas como X_i deve ser o mesmo
    # para ambos, a distância mínima entre dois pontos pos_a[i] e pos_b[i] é |pos_a[i] - pos_b[i]|.
    # O problema se reduz a minimizar a soma das distâncias |pos_a[i] - pos_b[i] - offset|.
    # Seja d_i = pos_a[i] - pos_b[i]. Queremos encontrar um deslocamento 's' tal que
    # sum(|d_i - s|) seja mínima. Isso ocorre quando 's' é a mediana dos valores d_i.
    
    d = [pos_a[i] - pos_b[i] for i in range(k)]
    d.sort()
    
    mediana = d[k // 2]
    
    ans = 0
    for val in d:
        ans += abs(val - mediana)
        
    print(ans)

if __name__ == '__main__':
    solve()