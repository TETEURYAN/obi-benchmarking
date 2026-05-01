
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    weights = list(map(int, data[1:n+1]))
    weights.sort()
    total = sum(weights)
    possible = True
    for i in range(n):
        if weights[i] > 8:
            possible = False
            break
    if possible:
        print('S')
        return
    if n == 1:
        print('S')
        return
    if n == 2:
        if abs(weights[0] - weights[1]) <= 8:
            print('S')
        else:
            print('N')
        return
    left = 0
    right = n - 1
    current_sum = 0
    while left <= right:
        if current_sum <= weights[right]:
            current_sum += weights[left]
            left += 1
        else:
            current_sum -= weights[right]
            right -= 1
        if abs(current_sum - weights[right]) > 8 and current_sum != 0:
            print('N')
            return
    print('S')

if __name__ == '__main__':
    main()
