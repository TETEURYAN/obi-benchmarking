import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    x = int(data[0])
    y = int(data[1])
    if -8 <= x <= 8 and -4 <= y <= 4:
        print('S')
    else:
        print('N')

if __name__ == '__main__':
    main()