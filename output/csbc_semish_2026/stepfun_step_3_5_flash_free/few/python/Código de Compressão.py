import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    s = data[1]
    result = []
    i = 0
    while i < n:
        j = i
        while j < n and s[j] == s[i]:
            j += 1
        result.append(str(j - i))
        result.append(s[i])
        i = j
    print(' '.join(result))

if __name__ == "__main__":
    main()