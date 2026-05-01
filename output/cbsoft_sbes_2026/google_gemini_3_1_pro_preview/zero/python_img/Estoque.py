import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    M = int(input_data[0])
    N = int(input_data[1])
    
    idx = 2
    matrix = []
    for i in range(M):
        row = []
        for j in range(N):
            row.append(int(input_data[idx]))
            idx += 1
        matrix.append(row)
        
    P = int(input_data[idx])
    idx += 1
    
    sold = 0
    for _ in range(P):
        I = int(input_data[idx])
        J = int(input_data[idx+1])
        idx += 2
        
        if matrix[I-1][J-1] > 0:
            matrix[I-1][J-1] -= 1
            sold += 1
            
    print(sold)

if __name__ == '__main__':
    solve()