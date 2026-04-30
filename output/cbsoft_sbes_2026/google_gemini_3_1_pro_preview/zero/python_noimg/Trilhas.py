import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    idx = 1
    
    best_trail = -1
    min_effort = float('inf')
    
    for i in range(1, N + 1):
        M = int(input_data[idx])
        altitudes = [int(x) for x in input_data[idx + 1 : idx + 1 + M]]
        idx += M + 1
        
        forward_effort = 0
        for j in range(M - 1):
            diff = altitudes[j+1] - altitudes[j]
            if diff > 0:
                forward_effort += diff
                
        backward_effort = 0
        for j in range(M - 1, 0, -1):
            diff = altitudes[j-1] - altitudes[j]
            if diff > 0:
                backward_effort += diff
                
        effort = min(forward_effort, backward_effort)
        
        if effort < min_effort:
            min_effort = effort
            best_trail = i
            
    print(best_trail)

if __name__ == '__main__':
    solve()