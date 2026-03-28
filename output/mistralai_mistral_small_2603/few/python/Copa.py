
import sys

def main():
    K = int(sys.stdin.readline())
    L = int(sys.stdin.readline())
    pos = [K, L]
    pos.sort()
    K, L = pos

    if L - K == 1:
        if K <= 2:
            print("oitavas")
        elif K <= 6:
            print("quartas")
        elif K <= 14:
            print("semifinal")
        else:
            print("final")
    else:
        if K <= 4:
            print("quartas")
        elif K <= 12:
            print("semifinal")
        else:
            print("final")

if __name__ == "__main__":
    main()
