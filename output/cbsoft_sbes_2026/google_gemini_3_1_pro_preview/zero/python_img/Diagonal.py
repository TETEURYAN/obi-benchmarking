
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    A = [int(x) for x in input_data[1:N+1]]
    
    events = []
    for i in range(N):
        if A[i] > 0:
            start = i + 2
            end = i + A[i] + 2
            events.append((start, 1))
            events.append((end, -1))
            
    events.sort()
    
    max_active = 0
    current_active = 0
    
    for pos, val in events:
        current_active += val
        if current_active > max_active:
            max_active = current_active
            
    print(max_active)

if __name__ == '__main__':
    solve()
