import sys

def main():
    H = int(sys.stdin.readline())
    M = int(sys.stdin.readline())
    S = int(sys.stdin.readline())
    T = int(sys.stdin.readline())

    total_seconds = H * 3600 + M * 60 + S + T
    total_seconds %= 86400  # 86400 segundos em um dia

    new_H = total_seconds // 3600
    remaining_seconds = total_seconds % 3600
    new_M = remaining_seconds // 60
    new_S = remaining_seconds % 60

    print(new_H)
    print(new_M)
    print(new_S)

if __name__ == '__main__':
    main()