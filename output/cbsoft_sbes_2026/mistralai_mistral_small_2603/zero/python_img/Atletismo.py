
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    arrival_order = list(map(int, data[1:n+1]))

    position = [0] * (n + 1)
    for idx, athlete in enumerate(arrival_order, start=1):
        position[athlete] = idx

    for i in range(1, n + 1):
        print(position[i])

if __name__ == "__main__":
    main()
