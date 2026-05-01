import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    board = [list(map(int, data[i*15:(i+1)*15])) for i in range(15)]
    
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
    
    for i in range(15):
        for j in range(15):
            if board[i][j] == 0:
                continue
            color = board[i][j]
            for di, dj in directions:
                count = 1
                ni, nj = i + di, j + dj
                while 0 <= ni < 15 and 0 <= nj < 15 and board[ni][nj] == color:
                    count += 1
                    if count == 5:
                        # Verifica se não é parte de uma sequência maior
                        pi, pj = i - di, j - dj
                        if 0 <= pi < 15 and 0 <= pj < 15 and board[pi][pj] == color:
                            break
                        ni2, nj2 = ni + di, nj + dj
                        if 0 <= ni2 < 15 and 0 <= nj2 < 15 and board[ni2][nj2] == color:
                            break
                        print(color)
                        return
                    ni += di
                    nj += dj
    print(0)

if __name__ == "__main__":
    main()