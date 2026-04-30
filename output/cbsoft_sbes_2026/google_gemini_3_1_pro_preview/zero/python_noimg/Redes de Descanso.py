import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    
    counts = {}
    for i in range(1, n + 1):
        h = input_data[i]
        counts[h] = counts.get(h, 0) + 1
        
    ans = sum(count // 2 for count in counts.values())
    
    print(ans)

if __name__ == '__main__':
    solve()