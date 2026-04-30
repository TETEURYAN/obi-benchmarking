
import sys

def main():
    data = sys.stdin.read().split()
    ptr = 0
    L = int(data[ptr])
    ptr += 1
    C = int(data[ptr])
    ptr += 1

    original = [[0] * C for _ in range(L)]
    current = [[0] * C for _ in range(L)]

    for i in range(L):
        for j in range(C):
            num = int(data[ptr])
            ptr += 1
            original[i][j] = i * C + j + 1
            current[i][j] = num

    moves = []

    # Process rows
    for i in range(L):
        for j in range(C):
            if current[i][j] != original[i][j]:
                target_val = original[i][j]
                target_i, target_j = divmod(target_val - 1, C)
                current_target_val = current[target_i][target_j]

                if current_target_val != original[target_i][target_j]:
                    # Find where target_val is currently
                    for x in range(L):
                        for y in range(C):
                            if current[x][y] == target_val:
                                moves.append(('L', i + 1, x + 1))
                                current[i][j], current[x][y] = current[x][y], current[i][j]
                                break
                    break

    # Process columns
    for j in range(C):
        for i in range(L):
            if current[i][j] != original[i][j]:
                target_val = original[i][j]
                target_i, target_j = divmod(target_val - 1, C)
                current_target_val = current[target_i][target_j]

                if current_target_val != original[target_i][target_j]:
                    # Find where target_val is currently
                    for x in range(L):
                        for y in range(C):
                            if current[x][y] == target_val:
                                moves.append(('C', j + 1, y + 1))
                                current[i][j], current[x][y] = current[x][y], current[i][j]
                                break
                    break

    # Verify if more moves are needed
    for i in range(L):
        for j in range(C):
            if current[i][j] != original[i][j]:
                # Find the correct position for current[i][j]
                target_val = original[i][j]
                target_i, target_j = divmod(target_val - 1, C)
                current_target_val = current[target_i][target_j]

                if current_target_val == target_val:
                    # Need to swap rows or columns
                    # Try to find a row swap
                    for x in range(i + 1, L):
                        if current[x][j] == target_val:
                            moves.append(('L', i + 1, x + 1))
                            current[i][j], current[x][j] = current[x][j], current[i][j]
                            break
                    else:
                        # Try to find a column swap
                        for y in range(j + 1, C):
                            if current[i][y] == target_val:
                                moves.append(('C', j + 1, y + 1))
                                current[i][j], current[i][y] = current[i][y], current[i][j]
                                break

    # Final verification
    for i in range(L):
        for j in range(C):
            if current[i][j] != original[i][j]:
                # Find the correct position for current[i][j]
                target_val = original[i][j]
                target_i, target_j = divmod(target_val - 1, C)
                current_target_val = current[target_i][target_j]

                if current_target_val == target_val:
                    # Swap rows
                    moves.append(('L', i + 1, target_i + 1))
                    current[i][j], current[target_i][j] = current[target_i][j], current[i][j]
                else:
                    # Swap columns
                    moves.append(('C', j + 1, target_j + 1))
                    current[i][j], current[i][target_j] = current[i][target_j], current[i][j]

    print(len(moves))
    for move in moves:
        print(f"{move[0]} {move[1]} {move[2]}")

if __name__ == "__main__":
    main()
