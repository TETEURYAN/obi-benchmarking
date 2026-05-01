
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    pos = [0] * (n + 1)
    
    for i in range(1, n + 1):
        pos[int(input_data[i])] = i
        
    rounds = 1
    for i in range(1, n):
        if pos[i + 1] < pos[i]:
            rounds += 1
            
    print(rounds)

if __name__ == '__main__':
    solve()
