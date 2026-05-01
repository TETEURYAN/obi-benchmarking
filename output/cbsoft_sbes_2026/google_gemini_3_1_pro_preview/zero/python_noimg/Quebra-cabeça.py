import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    
    pieces = {}
    
    idx = 1
    for _ in range(N):
        E = int(input_data[idx])
        C = input_data[idx+1]
        D = int(input_data[idx+2])
        pieces[E] = (C, D)
        idx += 3
        
    curr = 0
    ans = []
    for _ in range(N):
        C, D = pieces[curr]
        ans.append(C)
        curr = D
        
    print("".join(ans))

if __name__ == '__main__':
    solve()