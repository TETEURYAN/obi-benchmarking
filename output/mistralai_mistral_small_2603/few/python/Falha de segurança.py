
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        print(0)
        return
    n = int(data[0])
    passwords = data[1:n+1]

    count = 0
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if passwords[i] in passwords[j]:
                count += 1
    print(count)

if __name__ == "__main__":
    main()
