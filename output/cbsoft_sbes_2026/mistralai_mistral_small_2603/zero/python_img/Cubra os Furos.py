
import sys
import math

def main():
    data = sys.stdin.read().split()
    index = 0
    test_case = 1
    while index < len(data):
        N = int(data[index])
        index += 1
        if N == 0:
            break
        holes = []
        for _ in range(N):
            x = int(data[index])
            y = int(data[index + 1])
            index += 2
            holes.append((x, y))
        max_dist = 0
        for i in range(N):
            x1, y1 = holes[i]
            for j in range(N):
                x2, y2 = holes[j]
                dx = x1 - x2
                dy = y1 - y2
                dist = math.sqrt(dx * dx + dy * dy)
                if dist > max_dist:
                    max_dist = dist
        diameter = int(round(max_dist)) + 5
        print(f"Teste {test_case}")
        print(diameter)
        print()
        test_case += 1

if __name__ == "__main__":
    main()
