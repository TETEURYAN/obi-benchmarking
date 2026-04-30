import sys

def main():
    lines = sys.stdin.read().split()
    if not lines:
        return
    
    ans = 0
    
    for i in range(7):
        for j in range(5):
            if lines[i][j:j+3] in ("oo.", ".oo"):
                ans += 1
                
    for j in range(7):
        col = "".join(lines[i][j] for i in range(7))
        for i in range(5):
            if col[i:i+3] in ("oo.", ".oo"):
                ans += 1
                
    print(ans)

if __name__ == '__main__':
    main()