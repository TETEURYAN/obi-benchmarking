
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    s = data[1:n+1]
    count = 0
    for i in range(n - 2):
        if s[i] == '1' and s[i+1] == '0' and s[i+2] == '0':
            count += 1
    print(count)

if __name__ == "__main__":
    main()
