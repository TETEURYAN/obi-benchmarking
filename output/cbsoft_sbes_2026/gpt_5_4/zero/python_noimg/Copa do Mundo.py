teams = [chr(ord('A') + i) for i in range(16)]

for _ in range(4):
    next_round = []
    for i in range(0, len(teams), 2):
        m, n = map(int, input().split())
        if m > n:
            next_round.append(teams[i])
        else:
            next_round.append(teams[i + 1])
    teams = next_round

print(teams[0])