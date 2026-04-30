t1 = int(input())
t2 = int(input())
t3 = int(input())

swimmers = [(t1, 1), (t2, 2), (t3, 3)]
swimmers.sort()

print(swimmers[0][1])
print(swimmers[1][1])
print(swimmers[2][1])