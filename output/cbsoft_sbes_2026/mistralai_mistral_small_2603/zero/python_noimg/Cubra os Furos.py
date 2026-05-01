
import math

def main():
    teste = 1
    while True:
        N = int(input().strip())
        if N == 0:
            break
        furos = []
        for _ in range(N):
            x, y = map(int, input().split())
            furos.append((x, y))
        if N == 1:
            print(f"Teste {teste}")
            print(5)
            print()
            teste += 1
            continue
        max_dist = 0
        for i in range(N):
            x1, y1 = furos[i]
            for j in range(i + 1, N):
                x2, y2 = furos[j]
                dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
                if dist > max_dist:
                    max_dist = dist
        diametro = int(round(max_dist + 5))
        print(f"Teste {teste}")
        print(diametro)
        print()
        teste += 1

if __name__ == "__main__":
    main()
