import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return

    X = int(data[0])
    attempts = list(map(int, data[1:]))

    for T in attempts:
        if T == X:
            print("correto")
            break
        elif T > X:
            print("menor")
        else:
            print("maior")

if __name__ == "__main__":
    main()