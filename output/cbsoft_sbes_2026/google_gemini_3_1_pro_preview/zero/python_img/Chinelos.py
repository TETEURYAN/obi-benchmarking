import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    estoque = [0] * (n + 1)
    
    for i in range(1, n + 1):
        estoque[i] = int(input_data[i])
        
    p = int(input_data[n + 1])
    
    vendidos = 0
    for i in range(n + 2, n + 2 + p):
        pedido = int(input_data[i])
        if estoque[pedido] > 0:
            estoque[pedido] -= 1
            vendidos += 1
            
    print(vendidos)

if __name__ == '__main__':
    solve()