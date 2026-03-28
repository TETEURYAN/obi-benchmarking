
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        print('N')
        return

    k = int(data[0])
    n = int(data[1])
    alphabet = set(data[2])
    message = data[3]

    for char in message:
        if char not in alphabet:
            print('N')
            return

    print('S')

if __name__ == "__main__":
    main()
