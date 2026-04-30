
positions = list(map(int, input().split()))
pos1 = positions.index(1)
pos9 = positions.index(9)

def get_phase(a, b):
    if a > b:
        a, b = b, a
    diff = b - a
    if diff == 1 and a % 2 == 0:
        return "oitavas"
    if diff <= 3 and (a // 4 == b // 4):
        return "quartas"
    if diff <= 7 and (a // 8 == b // 8):
        return "semifinal"
    return "final"

print(get_phase(pos1, pos9))
