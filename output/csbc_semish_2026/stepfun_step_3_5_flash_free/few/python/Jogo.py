import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    x = int(data[0])
    for t_str in data[1:]:
        t = int(t_str)
        if t < x:
            print("maior")
        elif t > x:
            print("menor")
        else:
            print("correto")

if __name__ == "__main__":
    main()