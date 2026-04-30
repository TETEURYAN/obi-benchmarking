import sys

def solve():
    input_data = sys.stdin.read().split()
    if len(input_data) < 2:
        return
    
    k = int(input_data[0]) - 1
    l = int(input_data[1]) - 1
    
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