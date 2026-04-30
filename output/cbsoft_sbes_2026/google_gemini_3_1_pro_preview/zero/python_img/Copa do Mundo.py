import sys
from collections import deque

def solve():
    teams = deque(chr(ord('A') + i) for i in range(16))
    
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    idx = 0
    for _ in range(15):
        m = int(input_data[idx])
        n = int(input_data[idx+1])
        idx += 2
        
        t1 = teams.popleft()
        t2 = teams.popleft()
        
        if m > n:
            teams.append(t1)
        else:
            teams.append(t2)
            
    print(teams[0])

if __name__ == '__main__':
    solve()