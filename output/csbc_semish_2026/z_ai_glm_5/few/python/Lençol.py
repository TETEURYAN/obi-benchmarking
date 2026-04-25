import sys

def get_max_extent(x, y, fixed_dim):
    """
    Retorna a dimensão máxima possível na direção perpendicular a 'fixed_dim'
    para um retângulo x por y.
    Se o retângulo puder ter um lado de tamanho 'fixed_dim', o outro lado
    será a extensão máxima.
    """
    res = 0
    if x >= fixed_dim:
        res = y
    if y >= fixed_dim:
        if x > res:
            res = x
    return res

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    A1, B1, A2, B2, A, B = map(int, input_data)
    
    # Verificação de área: a área total disponível deve ser pelo menos a área do lençol.
    # Embora a lógica das dimensões cubra isso, é uma verificação barata e rápida.
    if A1 * B1 + A2 * B2 < A * B:
        print("N")
        return

    # Tentativa 1: O lençol tem dimensões A x B.
    # Caso 1.1: Costura paralela ao lado A (altura A).
    # Precisamos que a soma das larguras (contribuições) seja >= B.
    w1 = get_max_extent(A1, B1, A)
    w2 = get_max_extent(A2, B2, A)
    if w1 + w2 >= B:
        print("S")
        return
        
    # Caso 1.2: Costura paralela ao lado B (largura B).
    # Precisamos que a soma das alturas seja >= A.
    h1 = get_max_extent(A1, B1, B)
    h2 = get_max_extent(A2, B2, B)
    if h1 + h2 >= A:
        print("S")
        return

    # Tentativa 2: O lençol tem dimensões B x A (girado).
    # Isso é matematicamente equivalente a verificar se podemos formar B x A.
    # Caso 2.1: Costura paralela ao lado B (altura B).
    # Precisamos soma das larguras >= A.
    # Nota: Isso é idêntico à verificação de "largura B" do caso 1.2.
    # w1_rot = get_max_extent(A1, B1, B) # que é h1
    # w2_rot = get_max_extent(A2, B2, B) # que é h2
    # if w1_rot + w2_rot >= A: ... (já verificado acima)
    
    # Caso 2.2: Costura paralela ao lado A (largura A).
    # Precisamos soma das alturas >= B.
    # Nota: Isso é idêntico à verificação de "altura A" do caso 1.1.
    # h1_rot = get_max_extent(A1, B1, A) # que é w1
    # h2_rot = get_max_extent(A2, B2, A) # que é w2
    # if h1_rot + h2_rot >= B: ... (já verificado acima)

    # Como as verificações para B x A são simétricas e já cobertas pelas duas verificações de A x B
    # (uma verificação de costura vertical em A x B é o mesmo que costura horizontal em B x A, e vice-versa),
    # se chegamos aqui, nenhuma configuração funciona.
    print("N")

if __name__ == "__main__":
    solve()