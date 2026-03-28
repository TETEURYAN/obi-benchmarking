import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    A = list(map(int, data[1:1+n]))
    
    events = {}
    events[A[0]] = events.get(A[0], 0) - 1
    
    for i in range(1, n):
        if A[i-1] < A[i]:
            events[A[i-1]] = events.get(A[i-1], 0) + 1
            events[A[i]] = events.get(A[i], 0) - 1
    
    keys = sorted(events.keys())
    count = 1
    max_count = 1
    for x in keys:
        count += events[x]
        if count > max_count:
            max_count = count
    
    print(1 + max_count)

if __name__ == "__main__":
    main()