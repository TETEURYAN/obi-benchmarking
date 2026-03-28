
def main():
    a, b, c, d = map(int, input().split())
    if (a == c and b == d) or (a == b and c == d):
        print('V')
    else:
        print('F')

if __name__ == "__main__":
    main()
