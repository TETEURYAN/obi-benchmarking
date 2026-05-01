n = int(input().strip())

zero = max(0, (n - 2) ** 3)
one = 6 * max(0, (n - 2) ** 2)
two = 12 * max(0, n - 2)
three = 8

print(zero)
print(one)
print(two)
print(three)