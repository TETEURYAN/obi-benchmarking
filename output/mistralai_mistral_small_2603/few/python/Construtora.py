
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    a = list(map(int, data[1:n+1]))

    max_val = max(a)
    operations = 0

    while True:
        if all(x == max_val for x in a):
            break
        # Find the first segment that can be increased
        i = 0
        while i < n:
            if a[i] < max_val:
                j = i
                while j < n and a[j] < max_val and a[j] == a[i]:
                    j += 1
                # We can increase from i to j-1
                for k in range(i, j):
                    a[k] += 1
                operations += 1
                break
            i += 1
        else:
            # If no segment found, increase max_val
            max_val += 1

    print(operations)

if __name__ == "__main__":
    main()
