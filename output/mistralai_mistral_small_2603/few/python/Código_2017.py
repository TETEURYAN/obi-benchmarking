
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        print("ok")
        return

    n = int(data[0])
    strings = data[1:n+1]

    if n <= 2:
        print("ok")
        return

    for k in range(2, n):
        sk = strings[k]
        for a in range(k):
            for b in range(k):
                if a == b:
                    continue
                concat = strings[a] + strings[b]
                if sk in concat:
                    print(sk)
                    return
    print("ok")

if __name__ == "__main__":
    main()
