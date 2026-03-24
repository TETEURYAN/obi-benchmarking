import sys

data = sys.stdin.read().split()
a = int(data[0])
b = int(data[1])

def price(age):
    if age <= 17:
        return 15
    if age <= 59:
        return 30
    return 20

print(price(a) + price(b))