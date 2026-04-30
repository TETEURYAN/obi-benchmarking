
import sys

def main():
    teste = 1
    while True:
        line = sys.stdin.readline().split()
        if not line:
            continue
        M = int(line[0])
        N = int(line[1])
        if M == 0 and N == 0:
            break

        image = []
        for _ in range(M):
            row = list(map(int, sys.stdin.readline().split()))
            image.append(row)

        total_x = 0
        total_y = 0
        while True:
            line = sys.stdin.readline().split()
            X = int(line[0])
            Y = int(line[1])
            if X == 0 and Y == 0:
                break
            total_x += X
            total_y += Y

        total_x %= N
        total_y %= M

        if total_x != 0:
            for i in range(M):
                image[i] = image[i][-total_x:] + image[i][:-total_x]

        if total_y != 0:
            image = image[-total_y:] + image[:-total_y]

        print(f"Teste {teste}")
        for row in image:
            print(' '.join(map(str, row)))
        print()
        teste += 1

if __name__ == "__main__":
    main()
