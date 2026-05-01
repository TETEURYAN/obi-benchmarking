
from collections import deque

def main():
    C = int(input().strip())
    cores = list(map(int, input().split()))

    if C == 1:
        print(0)
        return

    if cores[0] == 0 or cores[-1] == 0:
        print(-1)
        return

    dist = [-1] * C
    dist[0] = 0
    fila = deque()
    fila.append(0)

    while fila:
        atual = fila.popleft()
        for passo in [1, 2]:
            proximo = atual + passo
            if proximo < C and cores[proximo] == 1 and dist[proximo] == -1:
                dist[proximo] = dist[atual] + 1
                fila.append(proximo)

    print(dist[-1])

if __name__ == "__main__":
    main()
