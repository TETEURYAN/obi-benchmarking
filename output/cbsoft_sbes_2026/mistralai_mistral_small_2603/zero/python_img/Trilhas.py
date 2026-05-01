
def main():
    import sys
    data = sys.stdin.read().split()
    ptr = 0
    N = int(data[ptr])
    ptr += 1

    best_effort = float('inf')
    best_id = None

    for id in range(1, N + 1):
        M = int(data[ptr])
        ptr += 1
        heights = list(map(int, data[ptr:ptr + M]))
        ptr += M

        effort1 = 0
        for i in range(1, M):
            diff = heights[i] - heights[i - 1]
            if diff > 0:
                effort1 += diff

        effort2 = 0
        for i in range(M - 1, 0, -1):
            diff = heights[i] - heights[i - 1]
            if diff > 0:
                effort2 += diff

        effort = min(effort1, effort2)

        if effort < best_effort:
            best_effort = effort
            best_id = id
        elif effort == best_effort and id < best_id:
            best_id = id

    print(best_id)

if __name__ == "__main__":
    main()
