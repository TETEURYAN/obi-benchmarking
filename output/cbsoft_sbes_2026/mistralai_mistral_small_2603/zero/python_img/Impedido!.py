
def main():
    L, R, D = map(int, input().split())
    if R > 50 and L < R and R > D:
        print("S")
    else:
        print("N")

if __name__ == "__main__":
    main()
