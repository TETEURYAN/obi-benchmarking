import sys

def main():
    input = sys.stdin.readline
    n = int(input())
    
    children = [[] for _ in range(n + 1)]
    root = -1
    
    for _ in range(n):
        i, j = map(int, input().split())
        if j == 0:
            root = i
        else:
            children[j].append(i)
    
    sys.setrecursionlimit(20000)
    balanced = True
    
    def dfs(u):
        nonlocal balanced
        if not balanced:
            return 0
        
        sizes = []
        total = 1
        
        for v in children[u]:
            s = dfs(v)
            sizes.append(s)
            total += s
        
        if sizes:
            first = sizes[0]
            for s in sizes[1:]:
                if s != first:
                    balanced = False
                    break
        
        return total
    
    dfs(root)
    print("bem" if balanced else "mal")

if __name__ == "__main__":
    main()
