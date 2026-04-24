import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    m = int(input_data[0])
    n = int(input_data[1])
    
    x = [int(i) for i in input_data[2:2+m]]
    y = [int(i) for i in input_data[2+m:2+m+n]]
    
    max_len = max(m, n)
    res = [0] * max_len
    
    carry = 0
    for i in range(max_len - 1, -1, -1):
        val_x = x[i] if i < m else 0
        val_y = y[i] if i < n else 0
        
        soma = val_x + val_y + carry
        res[i] = soma % 2
        carry = soma // 2
        
    if carry:
        res.append(1)
        
    while res and res[-1] == 0:
        res.pop()
        
    print(*(res))

if __name__ == '__main__':
    solve()