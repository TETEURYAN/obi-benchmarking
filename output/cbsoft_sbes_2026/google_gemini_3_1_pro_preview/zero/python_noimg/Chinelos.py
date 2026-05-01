import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    
    estoque = [0] * (N + 1)
    for i in range(1, N + 1):
        estoque[i] = int(input_data[i])
        
    P = int(input_data[N + 1])
    
    vendidos = 0
    for i in range(N + 2, N + 2 + P):
        pedido = int(input_data[i])
        if estoque[pedido] > 0:
            estoque[pedido] -= 1
            vendidos += 1
            
    print(vendidos)

if __name__ == '__main__':
    main()