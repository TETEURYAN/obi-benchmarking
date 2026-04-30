import sys
input = sys.stdin.readline

def main():
    n = int(input())
    pos = [0] * (n + 1)
    for i in range(1, n + 1):
        atleta = int(input())
        pos[atleta] = i
    out = []
    for i in range(1, n + 1):
        out.append(str(pos[i]))
    print('\n'.join(out))

main()