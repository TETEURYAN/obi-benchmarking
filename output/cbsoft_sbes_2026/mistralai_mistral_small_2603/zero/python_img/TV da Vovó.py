
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

        commands = []
        while True:
            line = sys.stdin.readline().split()
            X = int(line[0])
            Y = int(line[1])
            if X == 0 and Y == 0:
                break
            commands.append((X, Y))

        for X, Y in commands:
            if Y != 0:
                image = image[-Y:] + image[:-Y]
            if X != 0:
                new_image = []
                for row in image:
                    new_row = row[-X:] + row[:-X]
                    new_image.append(new_row)
                image = new_image

        print(f"Teste {teste}")
        for row in image:
            print(' '.join(map(str, row)))
        print()
        teste += 1

if __name__ == "__main__":
    main()
