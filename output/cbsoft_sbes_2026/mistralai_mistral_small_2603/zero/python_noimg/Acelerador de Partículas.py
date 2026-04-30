
D = int(input().strip())

if D < 10:
    print(1)
elif D < 18:
    print(2)
else:
    resto = (D - 10) % 8
    if resto < 5:
        print(2)
    else:
        print(3)
