import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    H, P, F, D = map(int, data)
    n = 16

    if D == -1:  # horário: decrementa
        pos = F
        while True:
            pos = (pos - 1) % n
            if pos == H:
                print("S")
                return
            if pos == P:
                print("N")
                return
    else:  # anti-horário: incrementa
        pos = F
        while True:
            pos = (pos + 1) % n
            if pos == H:
                print("S")
                return
            if pos == P:
                print("N")
                return

if __name__ == "__main__":
    main()