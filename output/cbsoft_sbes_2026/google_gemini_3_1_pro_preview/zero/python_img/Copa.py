import sys

def solve():
    lines = sys.stdin.read().split()
    if len(lines) < 2:
        return
    k = int(lines[0]) - 1
    l = int(lines[1]) - 1
    
    if k // 2 == l // 2:
        print("oitavas")
    elif k // 4 == l // 4:
        print("quartas")
    elif k // 8 == l // 8:
        print("semifinal")
    else:
        print("final")

if __name__ == '__main__':
    solve()