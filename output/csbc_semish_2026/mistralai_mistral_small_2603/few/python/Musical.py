
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    energies = list(map(int, data[1:n+1]))
    energies.sort()
    total = 0
    for i in range(n):
        total += abs(energies[i] - energies[(i+1) % n])
    print(total)

if __name__ == "__main__":
    main()
