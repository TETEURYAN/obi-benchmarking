import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    
    pos1 = data.index('1')
    pos9 = data.index('9')
    
    if pos1 // 2 == pos9 // 2:
        print("oitavas")
    elif pos1 // 4 == pos9 // 4:
        print("quartas")
    elif pos1 // 8 == pos9 // 8:
        print("semifinal")
    else:
        print("final")

if __name__ == '__main__':
    solve()