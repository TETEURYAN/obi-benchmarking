import sys

def main():
    s = sys.stdin.readline().rstrip('\n')
    result = []
    i = 0
    n = len(s)
    while i < n:
        if s[i] == ' ':
            result.append(' ')
            i += 1
        else:
            result.append(s[i+1])
            i += 2
    print(''.join(result))

if __name__ == "__main__":
    main()