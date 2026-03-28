import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    N = int(data[0])
    G = int(data[1])
    M = int(data[2])
    total_pedacos = 8 * G + 6 * M
    if total_pedacos > N:
        print(total_pedacos - N)
    else:
        print(0)

if __name__ == "__main__":
    main()