
def main():
    N = int(input())
    D = int(input())
    A = int(input())

    if D == A:
        print(0)
    else:
        diff = abs(D - A)
        if diff == N // 2 and N % 2 == 0:
            print(diff)
        else:
            print(min(diff, N - diff))

if __name__ == "__main__":
    main()
