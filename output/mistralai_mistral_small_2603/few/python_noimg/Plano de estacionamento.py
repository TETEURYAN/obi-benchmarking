
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        print(0)
        return

    n = int(data[0])
    m = int(data[1])
    v_list = list(map(int, data[2:2+m]))

    occupied = [False] * (n + 2)
    count = 0

    for v in v_list:
        found = False
        for pos in range(1, v + 1):
            if not occupied[pos]:
                occupied[pos] = True
                count += 1
                found = True
                break
        if not found:
            break

    print(count)

if __name__ == "__main__":
    main()
