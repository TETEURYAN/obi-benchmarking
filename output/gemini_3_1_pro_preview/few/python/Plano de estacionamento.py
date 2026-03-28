import sys

sys.setrecursionlimit(200000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    parent = list(range(n + 1))
    
    def find(i):
        root = i
        while parent[root] != root:
            root = parent[root]
        curr = i
        while curr != root:
            nxt = parent[curr]
            parent[curr] = root
            curr = nxt
        return root

    ans = 0
    for i in range(m):
        v = int(input_data[2 + i])
        available = find(v)
        if available > 0:
            ans += 1
            parent[available] = available - 1
        else:
            break
            
    print(ans)

if __name__ == '__main__':
    solve()