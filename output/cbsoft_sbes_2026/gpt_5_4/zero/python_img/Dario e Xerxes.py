n = int(input())

vence = {
    0: {1, 2},
    1: {2, 3},
    2: {3, 4},
    3: {4, 0},
    4: {0, 1},
}

dario = 0
xerxes = 0

for _ in range(n):
    d, x = map(int, input().split())
    if x in vence[d]:
        dario += 1
    else:
        xerxes += 1

print("dario" if dario > xerxes else "xerxes")