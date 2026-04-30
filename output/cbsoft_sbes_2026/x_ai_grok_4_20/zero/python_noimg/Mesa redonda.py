
A = int(input())
B = int(input())

pos_ana = (A - 1) % 3

pos_beatriz = (B - 1) % 3

if pos_beatriz == pos_ana:
    pos_beatriz = (pos_beatriz + 1) % 3

cadeiras = {0, 1, 2}
cadeiras.discard(pos_ana)
cadeiras.discard(pos_beatriz)

print(cadeiras.pop())
