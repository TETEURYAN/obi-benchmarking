import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    d = list(map(int, data[1:1+n]))
    last = d[-1]
    candidatos = []
    for i in range(n-1):
        if d[i] == 0 or d[i] == 5:
            candidatos.append(i)
    if not candidatos:
        print(-1)
        return
    if last > 5:
        i_escolhido = min(candidatos)
    else:
        zeros = [i for i in candidatos if d[i] == 0]
        if zeros:
            i_escolhido = min(zeros)
        else:
            i_escolhido = max(candidatos)
    d[i_escolhido], d[-1] = d[-1], d[i_escolhido]
    print(' '.join(map(str, d)))

if __name__ == "__main__":
    main()