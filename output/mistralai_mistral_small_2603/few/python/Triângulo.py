
import sys

def main():
    a, b, c, d = map(int, sys.stdin.read().split())
    sides = [a, b, c, d]
    sides.sort()
    if sides[0] + sides[1] > sides[2] or sides[1] + sides[2] > sides[3]:
        print('S')
    else:
        print('N')

if __name__ == '__main__':
    main()
