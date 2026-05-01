import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    D = int(input_data[0])
    rem = D % 400
    ans = min(rem, 400 - rem)
    print(ans)

if __name__ == '__main__':
    main()