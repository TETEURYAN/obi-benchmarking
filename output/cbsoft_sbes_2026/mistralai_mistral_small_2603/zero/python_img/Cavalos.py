
def main():
    M, N = map(int, input().split())
    if M == 1 or N == 1:
        print(max(M, N))
    elif M == 2 or N == 2:
        max_dim = max(M, N)
        if max_dim % 4 == 0:
            print(max_dim)
        elif max_dim % 4 == 1:
            print(max_dim + 1)
        else:
            print((max_dim // 4) * 4 + (max_dim % 4) * 2)
    else:
        print((M * N + 1) // 2)

if __name__ == "__main__":
    main()
