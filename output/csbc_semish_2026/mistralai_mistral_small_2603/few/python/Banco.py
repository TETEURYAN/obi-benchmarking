
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return

    idx = 0
    C = int(data[idx])
    idx += 1
    N = int(data[idx])
    idx += 1

    clients = []
    for _ in range(N):
        T = int(data[idx])
        D = int(data[idx+1])
        clients.append((T, D))
        idx += 2

    free_time = [0] * C
    late_clients = 0

    for T, D in clients:
        earliest_free = min(free_time)
        box_idx = free_time.index(earliest_free)
        start_time = max(T, earliest_free)
        free_time[box_idx] = start_time + D
        if start_time - T > 20:
            late_clients += 1

    print(late_clients)

if __name__ == "__main__":
    main()
