import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    total_clicks = 0
    
    idx = 1
    for _ in range(N):
        c = int(input_data[idx])
        s = int(input_data[idx+1])
        idx += 2
        
        diff = abs(c - s)
        total_clicks += min(diff, 10 - diff)
        
    print(total_clicks)

if __name__ == '__main__':
    solve()