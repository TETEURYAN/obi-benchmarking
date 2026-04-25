import sys

input_data = sys.stdin.read().split()
if input_data:
    n = int(input_data[0])
    if n < 4:
        print('N')
    else:
        limit = int(n**0.5)
        ans = 'N'
        for i in range(2, limit + 1):
            if n % i == 0:
                ans = 'S'
                break
        print(ans)