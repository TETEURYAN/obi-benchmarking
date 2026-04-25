import sys

def main():
    D = int(sys.stdin.read())
    pontos = [0, 400, 800, 1200, 1600, 2000]
    min_dist = float('inf')
    for ponto in pontos:
        dist = abs(D - ponto)
        if dist < min_dist:
            min_dist = dist
    print(min_dist)

if __name__ == '__main__':
    main()