import sys

def main():
    data = sys.stdin.read().splitlines()
    if not data:
        print('N')
        return
    n = int(data[0])
    lines = data[1:1+n]
    balance = 0
    for line in lines:
        for c in line:
            if c == '{':
                balance += 1
            elif c == '}':
                balance -= 1
                if balance < 0:
                    print('N')
                    return
    print('S' if balance == 0 else 'N')

if __name__ == '__main__':
    main()