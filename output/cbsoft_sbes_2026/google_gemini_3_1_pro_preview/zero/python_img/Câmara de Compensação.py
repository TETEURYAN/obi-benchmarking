import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    M = int(input_data[0])
    N = int(input_data[1])
    
    net_balances = [0] * (N + 1)
    original_total = 0
    
    idx = 2
    for _ in range(M):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        w = int(input_data[idx+2])
        idx += 3
        
        net_balances[u] -= v
        net_balances[w] += v
        original_total += v
        
    min_total = sum(b for b in net_balances if b > 0)
    
    if min_total < original_total:
        print('S')
    else:
        print('N')
    print(min_total)

if __name__ == '__main__':
    main()