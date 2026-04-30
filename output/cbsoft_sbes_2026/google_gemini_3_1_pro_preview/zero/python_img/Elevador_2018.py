import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    weights = [int(x) for x in input_data[1:N+1]]
    
    weights.sort()
    
    if weights[0] > 8:
        print('N')
        return
        
    for i in range(1, N):
        if weights[i] - weights[i-1] > 8:
            print('N')
            return
            
    print('S')

if __name__ == '__main__':
    solve()