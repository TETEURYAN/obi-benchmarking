import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    K = int(data[0])
    L = int(data[1])
    if (K - 1) // 2 == (L - 1) // 2:
        print("oitavas")
    elif (K - 1) // 4 == (L - 1) // 4:
        print("quartas")
    elif (K - 1) // 8 == (L - 1) // 8:
        print("semifinal")
    else:
        print("final")

if __name__ == "__main__":
    main()