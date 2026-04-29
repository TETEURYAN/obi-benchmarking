B = int(input().strip())
T = int(input().strip())

soma = B + T

if soma < 160:
    print(1)
elif soma > 160:
    print(2)
else:
    print(0)