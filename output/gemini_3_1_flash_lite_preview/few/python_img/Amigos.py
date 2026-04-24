import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    k = int(input_data[1])
    
    pos_a = []
    for i in range(n):
        if input_data[2 + i] == '1':
            pos_a.append(i)
            
    pos_b = []
    for i in range(n):
        if input_data[2 + n + i] == '1':
            pos_b.append(i)
            
    # O problema pede para que cada integrante do grupo esteja em frente a outro.
    # Isso significa que, após as trocas, o conjunto de posições ocupadas pelos 
    # amigos no lado superior deve ser idêntico ao conjunto de posições ocupadas 
    # pelos amigos no lado inferior.
    # O custo para mover um conjunto de posições {a1, a2, ..., ak} para {b1, b2, ..., bk}
    # é a soma das distâncias |ai - bi|.
    
    ans = 0
    for i in range(k):
        ans += abs(pos_a[i] - pos_b[i])
        
    print(ans)

if __name__ == '__main__':
    solve()