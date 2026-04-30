
def main():
    N, M = map(int, input().split())
    if N % (M + 1) == 0:
        print("Carlos")
    else:
        print("Paula")

if __name__ == "__main__":
    main()
