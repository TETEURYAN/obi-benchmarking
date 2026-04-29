A = int(input().strip())
B = int(input().strip())

ana = A % 3
beatriz = B % 3

if beatriz == ana:
    beatriz = (beatriz + 1) % 3

carolina = 3 - ana - beatriz
print(carolina)