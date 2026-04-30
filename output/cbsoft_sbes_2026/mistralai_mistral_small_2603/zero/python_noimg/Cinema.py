
idade1 = int(input())
idade2 = int(input())

total = 0

if idade1 >= 60:
    total += 20
elif idade1 >= 18:
    total += 25
elif idade1 >= 12:
    total += 15
else:
    total += 10

if idade2 >= 60:
    total += 20
elif idade2 >= 18:
    total += 25
elif idade2 >= 12:
    total += 15
else:
    total += 10

print(total)
