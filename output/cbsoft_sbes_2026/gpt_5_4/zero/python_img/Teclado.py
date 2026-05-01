import sys

def main():
    input = sys.stdin.readline
    
    n = input().strip()
    m = int(input())
    
    mp = {
        'a': '2', 'b': '2', 'c': '2',
        'd': '3', 'e': '3', 'f': '3',
        'g': '4', 'h': '4', 'i': '4',
        'j': '5', 'k': '5', 'l': '5',
        'm': '6', 'n': '6', 'o': '6',
        'p': '7', 'q': '7', 'r': '7', 's': '7',
        't': '8', 'u': '8', 'v': '8',
        'w': '9', 'x': '9', 'y': '9', 'z': '9',
    }
    
    ans = 0
    ln = len(n)
    
    for _ in range(m):
        s = input().strip()
        if len(s) != ln:
            continue
        ok = True
        for i, ch in enumerate(s):
            if mp[ch] != n[i]:
                ok = False
                break
        if ok:
            ans += 1
    
    print(ans)

if __name__ == "__main__":
    main()
