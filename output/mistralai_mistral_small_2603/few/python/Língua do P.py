
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    encoded = ' '.join(data)
    decoded = []
    i = 0
    n = len(encoded)
    while i < n:
        if encoded[i] == 'p':
            i += 1
        else:
            decoded.append(encoded[i])
            i += 1
    print(''.join(decoded))

if __name__ == '__main__':
    main()
