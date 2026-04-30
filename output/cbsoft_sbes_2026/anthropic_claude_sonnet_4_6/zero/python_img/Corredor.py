n = int(input())
a = list(map(int, input().split()))

# Maximum subarray sum (Kadane's algorithm)
max_sum = float('-inf')
current = 0
for x in a:
    current += x
    if current > max_sum:
        max_sum = current
    if current < 0:
        current = 0

print(max_sum)