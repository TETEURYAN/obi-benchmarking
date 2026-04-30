
def main():
    import sys
    data = sys.stdin.read().split()
    N = int(data[0])
    M = int(data[1])

    if M == 1:
        print("Paula")
        return

    if N % (M + 1) == 0:
        print("Carlos")
    else:
        print("Paula")

if __name__ == "__main__":
    main()
