import sys

input_data = sys.stdin.read().split()
age1 = int(input_data[0])
age2 = int(input_data[1])

def price(age):
    if age <= 17:
        return 15
    elif age <= 59:
        return 30
    else:
        return 20

total = price(age1) + price(age2)
print(total)