import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    min_cost = float('inf')
    
    idx = 1
    for _ in range(n):
        p = float(input_data[idx])
        g = float(input_data[idx+1])
        idx += 2
        
        cost = (p / g) * 1000.0
        if cost < min_cost:
            min_cost = cost
            
    print(f"{min_cost:.2f}")

if __name__ == '__main__':
    solve()