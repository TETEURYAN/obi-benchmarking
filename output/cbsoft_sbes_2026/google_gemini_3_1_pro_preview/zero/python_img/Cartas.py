import sys

def main():
    data = sys.stdin.read().split()
    if len(data) >= 3:
        a = int(data[0])
        b = int(data[1])
        c = int(data[2])
        print(a ^ b ^ c)

if __name__ == '__main__':
    main()