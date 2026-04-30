import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    board = [int(x) for x in input_data[1:n+1]]
    
    for i in range(n):
        count = board[i]
        if i > 0:
            count += board[i-1]
        if i < n - 1:
            count += board[i+1]
        print(count)

if __name__ == '__main__':
    main()