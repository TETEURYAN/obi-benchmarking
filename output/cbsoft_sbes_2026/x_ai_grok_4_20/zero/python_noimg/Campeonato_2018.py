
pos = list(map(int, input().split()))
p1 = pos.index(1)
p9 = pos.index(9)

def get_phase(a, b):
    if a > b:
        a, b = b, a
    diff = b - a
    if diff == 1 and a % 2 == 0:
        return "oitavas"
    if diff == 3 and a % 4 == 0:
        return "quartas"
    if diff == 7 and a % 8 == 0:
        return "semifinal"
    return "final"

print(get_phase(p1, p9))
