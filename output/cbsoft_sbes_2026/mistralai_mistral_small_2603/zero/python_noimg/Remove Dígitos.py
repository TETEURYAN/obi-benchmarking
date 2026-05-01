
def min_rounds(n):
    rounds = 0
    while n > 0:
        digits = [int(d) for d in str(n)]
        max_digit = max(digits)
        n -= max_digit
        rounds +=1
    return rounds

n = int(input())
print(min_rounds(n))
