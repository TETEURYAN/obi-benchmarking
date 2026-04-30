import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    dario_wins = 0
    xerxes_wins = 0
    
    idx = 1
    for _ in range(N):
        d = int(input_data[idx])
        x = int(input_data[idx+1])
        idx += 2
        
        if (x - d) % 5 in (1, 2):
            dario_wins += 1
        else:
            xerxes_wins += 1
            
    if dario_wins > xerxes_wins:
        print("dario")
    else:
        print("xerxes")

if __name__ == '__main__':
    solve()