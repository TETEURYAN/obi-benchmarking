import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    energies = list(map(int, data[1:1+n]))
    min_e = min(energies)
    max_e = max(energies)
    result = 2 * (max_e - min_e)
    print(result)

if __name__ == "__main__":
    main()