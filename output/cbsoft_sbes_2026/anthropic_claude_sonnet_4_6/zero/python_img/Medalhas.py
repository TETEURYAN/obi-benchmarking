t1 = int(input())
t2 = int(input())
t3 = int(input())

swimmers = [(t1, 1), (t2, 2), (t3, 3)]
swimmers.sort()

for s in swimmers:
    print(s[1])