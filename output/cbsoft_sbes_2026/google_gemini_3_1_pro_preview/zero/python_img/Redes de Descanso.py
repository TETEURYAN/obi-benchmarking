import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    counts = [0] * 100005
    
    for i in range(1, n + 1):
        counts[int(input_data[i])] += 1
        
    ans = sum(v // 2 for v in counts)
    print(ans)

if __name__ == '__main__':
    solve()