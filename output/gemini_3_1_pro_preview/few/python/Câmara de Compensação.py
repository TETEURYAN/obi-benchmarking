import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    m = int(input_data[0])
    n = int(input_data[1])
    
    balances = [0] * (n + 1)
    original_total = 0
    
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        w = int(input_data[idx+2])
        
        balances[u] -= v
        balances[w] += v
        original_total += v
        
        idx += 3
        
    min_total = sum(b for b in balances if b > 0)
    
    if min_total < original_total:
        print('S')
    else:
        print('N')
    print(min_total)

if __name__ == '__main__':
    main()