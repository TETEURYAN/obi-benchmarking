import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return

    E, M, D = map(int, data[:3])
    idx = 3

    likes = set()
    dislikes = set()

    for _ in range(M):
        x = int(data[idx])
        y = int(data[idx+1])
        idx += 2
        likes.add((min(x, y), max(x, y)))

    for _ in range(D):
        u = int(data[idx])
        v = int(data[idx+1])
        idx += 2
        dislikes.add((min(u, v), max(u, v)))

    groups = []
    group_map = {}
    for g in range(E // 3):
        i = int(data[idx])
        j = int(data[idx+1])
        k = int(data[idx+2])
        idx += 3
        members = [i, j, k]
        groups.append(members)
        for student in members:
            group_map[student] = g

    violations = 0

    # Check likes
    for pair in likes:
        a, b = pair
        if group_map[a] != group_map[b]:
            violations += 1

    # Check dislikes
    for pair in dislikes:
        a, b = pair
        if group_map[a] == group_map[b]:
            violations += 1

    print(violations)

if __name__ == "__main__":
    main()