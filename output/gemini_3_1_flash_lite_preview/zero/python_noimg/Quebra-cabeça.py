import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    adj = {}
    
    idx = 1
    for _ in range(n):
        e = int(input_data[idx])
        c = input_data[idx+1]
        d = int(input_data[idx+2])
        adj[e] = (c, d)
        idx += 3
        
    resultado = []
    atual = 0
    
    for _ in range(n):
        letra, proximo = adj[atual]
        resultado.append(letra)
        atual = proximo
        
    sys.stdout.write("".join(resultado) + "\n")

if __name__ == '__main__':
    solve()