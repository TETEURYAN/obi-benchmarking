import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    seq = input_data[1:n+1]
    
    ans = 1
    last = seq[0]
    for i in range(1, n):
        if seq[i] != last:
            ans += 1
            last = seq[i]
            
    print(ans)

if __name__ == '__main__':
    solve()