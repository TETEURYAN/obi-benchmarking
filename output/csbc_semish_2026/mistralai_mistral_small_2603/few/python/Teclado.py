
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        print(0)
        return

    n = data[0]
    m = int(data[1])
    strings = data[2:2+m]

    digit_map = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    count = 0
    for s in strings:
        if len(s) != len(n):
            continue
        valid = True
        for i in range(len(s)):
            if s[i] not in digit_map.get(n[i], ''):
                valid = False
                break
        if valid:
            count += 1
    print(count)

if __name__ == "__main__":
    main()
