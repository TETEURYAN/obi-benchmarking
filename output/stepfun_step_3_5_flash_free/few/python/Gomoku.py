import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        print(0)
        return
    nums = list(map(int, data))
    board = [nums[i*15:(i+1)*15] for i in range(15)]
    directions = [(0,1), (1,0), (1,1), (1,-1)]
    for i in range(15):
        for j in range(15):
            for dx, dy in directions:
                ni = i + 4*dx
                nj = j + 4*dy
                if 0 <= ni < 15 and 0 <= nj < 15:
                    val = board[i][j]
                    if val == 0:
                        continue
                    ok = True
                    for k in range(1,5):
                        if board[i + k*dx][j + k*dy] != val:
                            ok = False
                            break
                    if ok:
                        print(val)
                        return
    print(0)

if __name__ == "__main__":
    main()