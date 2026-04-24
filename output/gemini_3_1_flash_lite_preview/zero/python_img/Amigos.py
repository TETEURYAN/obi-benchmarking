import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    k = int(input_data[1])
    
    a = [int(x) for x in input_data[2:2+n]]
    b = [int(x) for x in input_data[2+n:2+2*n]]
    
    pos_a = [i for i, val in enumerate(a) if val == 1]
    pos_b = [i for i, val in enumerate(b) if val == 1]
    
    # O problema se resume a encontrar o deslocamento 's' tal que a soma das distâncias
    # |pos_a[i] - (pos_b[i] + s)| seja mínima.
    # Como queremos minimizar a soma de valores absolutos, a mediana é a solução ótima.
    # Seja d[i] = pos_a[i] - pos_b[i]. Queremos minimizar sum(|d[i] - s|).
    
    d = [pos_a[i] - pos_b[i] for i in range(k)]
    d.sort()
    
    # A mediana de d é d[k // 2]
    median = d[k // 2]
    
    ans = 0
    for val in d:
        ans += abs(val - median)
        
    print(ans)

if __name__ == '__main__':
    solve()