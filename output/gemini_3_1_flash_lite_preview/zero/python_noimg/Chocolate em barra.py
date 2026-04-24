import sys

def solve():
    try:
        line1 = sys.stdin.readline()
        if not line1:
            return
        n = int(line1.strip())
        x1, y1 = map(int, sys.stdin.readline().split())
        x2, y2 = map(int, sys.stdin.readline().split())
    except ValueError:
        return

    meio = n // 2

    corte_horizontal = (x1 <= meio and x2 > meio) or (x1 > meio and x2 <= meio)
    corte_vertical = (y1 <= meio and y2 > meio) or (y1 > meio and y2 <= meio)

    if corte_horizontal or corte_vertical:
        print("S")
    else:
        print("N")

if __name__ == '__main__':
    solve()