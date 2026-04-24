import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    idx = 0
    N = int(input_data[idx])
    idx += 1
    
    fila = []
    for _ in range(N):
        fila.append(int(input_data[idx]))
        idx += 1
        
    Q = int(input_data[idx])
    idx += 1
    
    output = []
    
    for _ in range(Q):
        tipo = int(input_data[idx])
        i = int(input_data[idx+1])
        x = int(input_data[idx+2])
        idx += 3
        
        if tipo == 0:
            fila.insert(i, x)
        else:
            h_i = fila[i-1]
            target = h_i + x
            found = 0
            for j in range(i - 2, -1, -1):
                if fila[j] > target:
                    found = j + 1
                    break
            output.append(str(found))
            
    sys.stdout.write("\n".join(output) + "\n")

if __name__ == '__main__':
    solve()