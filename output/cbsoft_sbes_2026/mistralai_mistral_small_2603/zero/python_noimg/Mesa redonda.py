
A = int(input())
B = int(input())

cadeiras = [0, 1, 2]
ana = cadeiras[A % 3]
cadeiras.remove(ana)

if B % 3 == 0:
    beatriz = cadeiras[0]
else:
    beatriz = cadeiras[B % 3]

if beatriz in cadeiras:
    cadeiras.remove(beatriz)

carolina = cadeiras[0]
print(carolina)
