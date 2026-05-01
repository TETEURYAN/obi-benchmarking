
def main():
    M, N = map(int, input().split())
    if M == 1 or N == 1:
        print(max(M, N))
    elif M == 2 or N == 2:
        max_val = max(M, N)
        if max_val % 4 == 0:
            print(max_val)
        elif max_val % 4 == 1:
            print(max_val + 1)
        else:
            print((max_val // 4) * 4 + 4)
    else:
        print((M * N + 1) // 2)

if __name__ == "__main__":
    main()
